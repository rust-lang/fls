#!/usr/bin/env -S uv run
# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Ferrocene Developers
# SPDX-FileCopyrightText: The Rust Project Contributors

import os
import sys
from pathlib import Path
import argparse
import shlex
import subprocess
import shutil
import threading
import time

# Automatically watch the following extra directories when --serve is used.
EXTRA_WATCH_DIRS = ["exts", "themes"]


def run_with_log(command, log_path):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    command = [str(part) for part in command]
    with log_path.open("w", encoding="utf-8") as log_file:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        try:
            assert process.stdout is not None
            for line in process.stdout:
                sys.stdout.write(line)
                sys.stdout.flush()
                log_file.write(line)
            return process.wait()
        except KeyboardInterrupt:
            process.terminate()
            process.wait()
            raise


def generate_glossary_command(root, tags):
    command = [sys.executable, str(root / "generate-glossary.py")]
    for tag in tags:
        command += ["-t", tag]
    return command


def run_generate_glossary(root, tags):
    subprocess.run(generate_glossary_command(root, tags), check=True)


def supports_pre_build():
    try:
        result = subprocess.run(
            ["sphinx-autobuild", "--help"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False
    return "--pre-build" in result.stdout


def iter_glossary_sources(root):
    src_dir = root / "src"
    yield from src_dir.rglob("*.rst")
    yield from src_dir.rglob("*.rst.inc")


def snapshot_glossary_sources(root):
    snapshot = {}
    for path in iter_glossary_sources(root):
        try:
            snapshot[path] = path.stat().st_mtime
        except FileNotFoundError:
            continue
    return snapshot


def start_glossary_watcher(root, tags, stamp_path, stop_event):
    def watcher():
        previous = snapshot_glossary_sources(root)
        while not stop_event.is_set():
            time.sleep(0.5)
            current = snapshot_glossary_sources(root)
            if current == previous:
                continue
            previous = current
            try:
                run_generate_glossary(root, tags)
                stamp_path.touch()
            except subprocess.CalledProcessError:
                print(
                    "warning: glossary generator failed during serve", file=sys.stderr
                )

    thread = threading.Thread(target=watcher, daemon=True)
    thread.start()
    return thread


def build_docs(root, builder, clear, serve, debug, tags):
    dest = root / "build"
    dest.mkdir(parents=True, exist_ok=True)
    output_dir = dest / builder

    args = ["-b", builder, "-d", dest / "doctrees"]
    if debug:
        # Disable parallel builds and show exceptions in debug mode.
        #
        # We can't show exceptions in parallel mode because in parallel mode
        # all exceptions will be swallowed up by Python's multiprocessing.
        # That's also why we don't show exceptions outside of debug mode.
        args += ["-j", "1", "-T"]
    else:
        # Enable parallel builds:
        args += ["-j", "auto"]
    if clear:
        if output_dir.exists():
            shutil.rmtree(output_dir)
        # Using a fresh environment
        args.append("-E")
    for tag in tags:
        args += ["-t", tag]
    if serve:
        for extra_watch_dir in EXTRA_WATCH_DIRS:
            extra_watch_dir = root / extra_watch_dir
            if extra_watch_dir.exists():
                args += ["--watch", extra_watch_dir]
    else:
        # Error out at the *end* of the build if there are warnings:
        args += ["-W", "--keep-going"]

    commit = current_git_commit(root)
    if commit is not None:
        args += ["-D", f"html_theme_options.commit={commit}"]

    run_generate_glossary(root, tags)

    watcher_thread = None
    watcher_stop = None
    if serve:
        pre_build_command = shlex.join(generate_glossary_command(root, tags))
        if supports_pre_build():
            args += ["--pre-build", pre_build_command]
        else:
            stamp_dir = dest / "glossary-watch"
            stamp_dir.mkdir(parents=True, exist_ok=True)
            stamp_path = stamp_dir / "glossary.stamp"
            stamp_path.touch()
            args += ["--watch", stamp_dir]
            watcher_stop = threading.Event()
            watcher_thread = start_glossary_watcher(
                root, tags, stamp_path, watcher_stop
            )

    log_path = dest / "sphinx-build.log"
    try:
        returncode = run_with_log(
            [
                "sphinx-autobuild" if serve else "sphinx-build",
                *args,
                root / "src",
                output_dir,
            ],
            log_path,
        )
    except KeyboardInterrupt:
        if watcher_stop is not None:
            watcher_stop.set()
        exit(1)
    finally:
        if watcher_stop is not None:
            watcher_stop.set()
        if watcher_thread is not None:
            watcher_thread.join()
    if returncode != 0:
        print("\nhint: if you see an exception, pass --debug to see the full traceback")
        exit(1)

    return dest / builder


def build_linkchecker(root):
    repo = root / ".linkchecker"
    src = repo / "src" / "tools" / "linkchecker"
    bin = src / "target" / "release" / "linkchecker"

    if not src.is_dir():
        subprocess.run(["git", "init", repo], check=True)

        def git(args):
            subprocess.run(["git", *args], cwd=repo, check=True)

        # Avoid fetching blobs unless needed by the sparse checkout
        git(["remote", "add", "origin", "https://github.com/rust-lang/rust"])
        git(["config", "remote.origin.promisor", "true"])
        git(["config", "remote.origin.partialCloneFilter", "blob:none"])

        # Checkout only the linkchecker tool rather than the whole repo
        git(["config", "core.sparsecheckout", "true"])
        with open(repo / ".git" / "info" / "sparse-checkout", "w") as f:
            f.write("/src/tools/linkchecker/")

        # Avoid fetching the whole history
        git(["fetch", "--depth=1", "origin", "main"])
        git(["checkout", "main"])

    if not bin.is_file():
        subprocess.run(["cargo", "build", "--release"], cwd=src, check=True)

    return bin


def current_git_commit(root):
    try:
        return (
            subprocess.run(
                ["git", "rev-parse", "HEAD"],
                check=True,
                stdout=subprocess.PIPE,
            )
            .stdout.decode("utf-8")
            .strip()
        )
    # `git` executable missing from the system
    except FileNotFoundError:
        print("warning: failed to detect git commit: missing executable git")
        return
    # `git` returned an error (git will print the actual error to stderr)
    except subprocess.CalledProcessError:
        print("warning: failed to detect git commit: git returned an error")
        return


def main(root):
    root = Path(root)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--clear", help="disable incremental builds", action="store_true"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-s",
        "--serve",
        help="start a local server with live reload",
        action="store_true",
    )
    group.add_argument(
        "--check-links", help="Check whether all links are valid", action="store_true"
    )
    group.add_argument(
        "--xml", help="Generate Sphinx XML rather than HTML", action="store_true"
    )
    group.add_argument(
        "--debug",
        help="Debug mode for the extensions, showing exceptions",
        action="store_true",
    )
    parser.add_argument(
        "-t",
        "--tag",
        action="append",
        default=[],
        help="Sphinx tag (repeatable)",
    )
    args = parser.parse_args()

    tags = list(dict.fromkeys(args.tag))

    rendered = build_docs(
        root,
        "xml" if args.xml else "html",
        args.clear,
        args.serve,
        args.debug,
        tags,
    )

    if args.check_links:
        linkchecker = build_linkchecker(root)
        if subprocess.run([linkchecker, rendered]).returncode != 0:
            print("error: linkchecker failed")
            exit(1)


main(os.path.abspath(os.path.dirname(__file__)))
