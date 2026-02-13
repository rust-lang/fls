#!/usr/bin/env -S uv run
# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Ferrocene Developers

from __future__ import annotations

import argparse
import filecmp
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

EXIT_SUCCESS = 0
EXIT_DIFFERENCES = 1
EXIT_ERROR = 2
FIXED_BUILD_COMMIT = "0000000000000000000000000000000000000000"


def main() -> int:
    try:
        repo_root = find_repo_root(Path(__file__).resolve().parent)
        if repo_root is None:
            print("error: make.py not found in repo root", file=sys.stderr)
            return EXIT_ERROR

        parser = argparse.ArgumentParser(
            description=(
                "Build and compare rendered HTML output under configured " "policy"
            ),
        )
        parser.add_argument(
            "--mode",
            choices=["export-ref", "compare-dirs", "refs", "repro"],
            default="repro",
            help="Operation mode",
        )
        parser.add_argument("--ref", help="Git reference for export-ref/repro")
        parser.add_argument("--left-ref", help="Left Git reference for refs mode")
        parser.add_argument("--right-ref", help="Right Git reference for refs mode")
        parser.add_argument("--output-dir", help="Output directory for export-ref mode")
        parser.add_argument("--left-dir", help="Left directory for compare-dirs mode")
        parser.add_argument("--right-dir", help="Right directory for compare-dirs mode")
        parser.add_argument("--report", help="Path to write comparison report")
        args = parser.parse_args()

        report_root = default_report_root(repo_root)
        report_root.mkdir(parents=True, exist_ok=True)

        if args.mode == "export-ref":
            ref = require_value(args.ref, "--ref is required for --mode export-ref")
            output_dir = resolve_path(
                require_value(
                    args.output_dir,
                    "--output-dir is required for --mode export-ref",
                ),
                repo_root,
            )
            export_ref(repo_root, ref, output_dir, report_root)
            print(f"exported HTML for {ref} to {output_dir}")
            return EXIT_SUCCESS

        if args.mode == "compare-dirs":
            left_dir = resolve_path(
                require_value(
                    args.left_dir,
                    "--left-dir is required for --mode compare-dirs",
                ),
                repo_root,
            )
            right_dir = resolve_path(
                require_value(
                    args.right_dir,
                    "--right-dir is required for --mode compare-dirs",
                ),
                repo_root,
            )
            report_path = resolve_report_path(
                args.report,
                repo_root,
                report_root,
                "verify-html-diff-compare-dirs.txt",
            )
            return run_comparison_mode(
                mode="compare-dirs",
                left_label=str(left_dir),
                right_label=str(right_dir),
                left_dir=left_dir,
                right_dir=right_dir,
                report_path=report_path,
            )

        if args.mode == "refs":
            left_ref = args.left_ref or "HEAD"
            right_ref = args.right_ref or "HEAD"
            report_path = resolve_report_path(
                args.report,
                repo_root,
                report_root,
                f"verify-html-diff-refs-{sanitize_label(left_ref)}-vs-"
                f"{sanitize_label(right_ref)}.txt",
            )
            with tempfile.TemporaryDirectory(
                prefix="verify-html-diff-refs-",
                dir=str(report_root),
            ) as tmp_dir:
                temp_root = Path(tmp_dir)
                left_dir = temp_root / "left"
                right_dir = temp_root / "right"
                worktree_dir = temp_root / "worktree"
                export_ref(repo_root, left_ref, left_dir, report_root, worktree_dir)
                export_ref(repo_root, right_ref, right_dir, report_root, worktree_dir)
                return run_comparison_mode(
                    mode="refs",
                    left_label=left_ref,
                    right_label=right_ref,
                    left_dir=left_dir,
                    right_dir=right_dir,
                    report_path=report_path,
                )

        ref = args.ref or "HEAD"
        report_path = resolve_report_path(
            args.report,
            repo_root,
            report_root,
            f"verify-html-diff-repro-{sanitize_label(ref)}.txt",
        )
        with tempfile.TemporaryDirectory(
            prefix="verify-html-diff-repro-",
            dir=str(report_root),
        ) as tmp_dir:
            temp_root = Path(tmp_dir)
            left_dir = temp_root / "first"
            right_dir = temp_root / "second"
            worktree_dir = temp_root / "worktree"
            export_ref(repo_root, ref, left_dir, report_root, worktree_dir)
            export_ref(repo_root, ref, right_dir, report_root, worktree_dir)
            return run_comparison_mode(
                mode="repro",
                left_label=f"{ref} (run 1)",
                right_label=f"{ref} (run 2)",
                left_dir=left_dir,
                right_dir=right_dir,
                report_path=report_path,
            )
    except subprocess.CalledProcessError as exc:
        command = " ".join(str(part) for part in exc.cmd or [])
        if command:
            print(
                f"error: command failed with exit code {exc.returncode}: {command}",
                file=sys.stderr,
            )
        else:
            print(
                f"error: command failed with exit code {exc.returncode}",
                file=sys.stderr,
            )
        return EXIT_ERROR
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return EXIT_ERROR


def run_comparison_mode(
    mode: str,
    left_label: str,
    right_label: str,
    left_dir: Path,
    right_dir: Path,
    report_path: Path,
) -> int:
    diff = diff_trees(left_dir, right_dir)
    write_report(report_path, mode, left_label, right_label, diff)
    if has_differences(diff):
        print(
            "differences found under configured comparison policy; "
            f"report written to {report_path}"
        )
        return EXIT_DIFFERENCES
    print(
        "no differences under configured comparison policy; "
        f"report written to {report_path}"
    )
    return EXIT_SUCCESS


def require_value(value: str | None, error_message: str) -> str:
    if value is None:
        raise RuntimeError(error_message)
    return value


def resolve_path(value: str, repo_root: Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = repo_root / path
    return path.resolve()


def resolve_report_path(
    report: str | None,
    repo_root: Path,
    report_root: Path,
    default_name: str,
) -> Path:
    if report is None:
        path = report_root / default_name
    else:
        path = resolve_path(report, repo_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def default_report_root(repo_root: Path) -> Path:
    config_dir = os.environ.get("OPENCODE_CONFIG_DIR")
    if config_dir:
        return Path(config_dir).resolve() / "reports"
    return repo_root / "build" / "html-diff"


def sanitize_label(value: str) -> str:
    sanitized = []
    for char in value:
        if char.isalnum() or char in {"-", "_", "."}:
            sanitized.append(char)
        else:
            sanitized.append("-")
    return "".join(sanitized).strip("-") or "ref"


def export_ref(
    repo_root: Path,
    ref: str,
    output_dir: Path,
    report_root: Path,
    worktree_dir: Path | None = None,
) -> None:
    clean_dir(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    worktree_root = report_root / "verify-html-diff-worktrees"
    worktree_root.mkdir(parents=True, exist_ok=True)

    cleanup_worktree_path = False
    if worktree_dir is None:
        worktree_dir = Path(
            tempfile.mkdtemp(prefix="worktree-", dir=str(worktree_root))
        )
        cleanup_worktree_path = True
    else:
        worktree_dir.parent.mkdir(parents=True, exist_ok=True)
        clean_dir(worktree_dir)

    worktree_added = False
    try:
        run_best_effort(
            ["git", "worktree", "remove", "--force", str(worktree_dir)],
            cwd=repo_root,
        )
        run(
            ["git", "worktree", "add", "--detach", str(worktree_dir), ref],
            cwd=repo_root,
        )
        worktree_added = True
        git_wrapper_dir = worktree_dir / "build" / "verify-tools-bin"
        git_wrapper = git_wrapper_dir / "git"
        git_wrapper_dir.mkdir(parents=True, exist_ok=True)
        real_git = shutil.which("git")
        if real_git is None:
            raise RuntimeError("missing git executable")
        git_wrapper.write_text(
            "#!/bin/sh\n"
            'if [ "$1" = "rev-parse" ] && [ "$2" = "HEAD" ] && [ -z "$3" ]; then\n'
            f"  printf '%s\\n' '{FIXED_BUILD_COMMIT}'\n"
            "  exit 0\n"
            "fi\n"
            f'exec {real_git} "$@"\n',
            encoding="utf-8",
        )
        git_wrapper.chmod(0o755)

        env = os.environ.copy()
        env["PATH"] = f"{git_wrapper_dir}:{env.get('PATH', '')}"
        run(["./make.py", "--clear"], cwd=worktree_dir, env=env)

        html_dir = worktree_dir / "build" / "html"
        if not html_dir.is_dir():
            raise RuntimeError(f"missing build output at {html_dir}")
        copy_tree(html_dir, output_dir)
        write_manifest(output_dir)
    finally:
        if worktree_added:
            try:
                run(
                    ["git", "worktree", "remove", "--force", str(worktree_dir)],
                    cwd=repo_root,
                )
            except subprocess.CalledProcessError:
                pass
        if cleanup_worktree_path:
            shutil.rmtree(worktree_dir, ignore_errors=True)


def run(command: list[str], cwd: Path, env: dict[str, str] | None = None) -> None:
    subprocess.run(command, check=True, cwd=cwd, env=env)


def run_best_effort(command: list[str], cwd: Path) -> None:
    try:
        run(command, cwd=cwd)
    except subprocess.CalledProcessError:
        return


def find_repo_root(start: Path) -> Path | None:
    for candidate in (start, *start.parents):
        if (candidate / "make.py").is_file():
            return candidate
    return None


def clean_dir(path: Path) -> None:
    if path.exists():
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()


def copy_tree(source: Path, destination: Path) -> None:
    if not source.is_dir():
        raise RuntimeError(f"missing build output at {source}")
    shutil.copytree(source, destination, dirs_exist_ok=True)


def write_manifest(root: Path) -> None:
    entries: list[str] = []
    for rel_path, file_path in list_files(root).items():
        if rel_path == "manifest.sha256":
            continue
        digest = hashlib.sha256(file_path.read_bytes()).hexdigest()
        entries.append(f"{digest}  {rel_path}")
    manifest = root / "manifest.sha256"
    manifest.write_text("\n".join(entries) + "\n", encoding="utf-8")


def diff_trees(left: Path, right: Path) -> dict[str, list[str]]:
    left_files = list_files(left)
    right_files = list_files(right)

    only_left: list[str] = []
    only_right: list[str] = []
    changed: list[str] = []
    comparisons: list[str] = []

    compared_paths = sorted((set(left_files) | set(right_files)) - {"manifest.sha256"})
    for rel in compared_paths:
        if rel.startswith("_sources/"):
            continue
        if rel not in right_files:
            only_left.append(rel)
            continue
        if rel not in left_files:
            only_right.append(rel)
            continue

        special = compare_special(rel, left_files[rel], right_files[rel])
        if special is not None:
            comparisons.append(str(special["message"]))
            if not special["equal"]:
                changed.append(rel)
            continue

        if not filecmp.cmp(left_files[rel], right_files[rel], shallow=False):
            changed.append(rel)

    return {
        "only_left": only_left,
        "only_right": only_right,
        "changed": changed,
        "comparisons": comparisons,
    }


def has_differences(diff: dict[str, list[str]]) -> bool:
    return bool(diff["only_left"] or diff["only_right"] or diff["changed"])


def compare_special(rel: str, left: Path, right: Path) -> dict[str, object] | None:
    name = os.path.basename(rel)
    if name == "paragraph-ids.json":
        return compare_paragraph_ids(left, right)
    if name == "searchindex.js":
        return compare_searchindex(left, right)
    if name == ".buildinfo":
        return compare_buildinfo(left, right)
    return None


def compare_paragraph_ids(left: Path, right: Path) -> dict[str, object]:
    left_data = normalize_paragraph_ids(left)
    right_data = normalize_paragraph_ids(right)
    if left_data == right_data:
        return {
            "equal": True,
            "message": "paragraph-ids.json: normalized content matches",
        }
    return {
        "equal": False,
        "message": "paragraph-ids.json: normalized content differs",
    }


def normalize_paragraph_ids(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    normalized = dict(data)

    documents = []
    for doc in data.get("documents", []):
        doc_data = dict(doc)
        sections = []
        for section in doc.get("sections", []):
            section_data = dict(section)
            paragraphs = section_data.get("paragraphs", [])
            section_data["paragraphs"] = sorted(
                paragraphs,
                key=lambda paragraph: json.dumps(paragraph, sort_keys=True),
            )
            sections.append(section_data)
        sections.sort(key=lambda item: item.get("id", ""))
        doc_data["sections"] = sections
        documents.append(doc_data)
    documents.sort(key=lambda item: item.get("link", ""))
    normalized["documents"] = documents
    return normalized


def compare_buildinfo(left: Path, right: Path) -> dict[str, object]:
    left_info = read_buildinfo(left)
    right_info = read_buildinfo(right)

    if left_info.get("config") != right_info.get("config"):
        return {"equal": False, "message": ".buildinfo: config hash differs"}

    if left_info.get("tags") != right_info.get("tags"):
        return {
            "equal": True,
            "message": ".buildinfo: config matches; tags differ (ignored)",
        }

    return {"equal": True, "message": ".buildinfo: config matches"}


def compare_searchindex(left: Path, right: Path) -> dict[str, object]:
    left_data = normalize_searchindex(read_searchindex_payload(left))
    right_data = normalize_searchindex(read_searchindex_payload(right))
    if left_data == right_data:
        return {
            "equal": True,
            "message": (
                "searchindex.js: normalized content matches "
                "(ferrocene_spec envversion ignored)"
            ),
        }
    return {
        "equal": False,
        "message": "searchindex.js: normalized content differs",
    }


def read_searchindex_payload(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8").strip()
    prefix = "Search.setIndex("
    if not text.startswith(prefix):
        raise RuntimeError(f"unexpected searchindex format in {path}")
    payload = text[len(prefix) :]
    if payload.endswith(");"):
        payload = payload[:-2]
    elif payload.endswith(")"):
        payload = payload[:-1]
    else:
        raise RuntimeError(f"unexpected searchindex terminator in {path}")
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise RuntimeError(f"unexpected searchindex payload type in {path}")
    return data


def normalize_searchindex(data: dict[str, object]) -> dict[str, object]:
    normalized = dict(data)
    envversion = normalized.get("envversion")
    if isinstance(envversion, dict) and "ferrocene_spec" in envversion:
        envversion_normalized = dict(envversion)
        envversion_normalized["ferrocene_spec"] = "<ignored>"
        normalized["envversion"] = envversion_normalized
    return normalized


def read_buildinfo(path: Path) -> dict[str, str]:
    info: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        info[key.strip()] = value.strip()
    return info


def list_files(root: Path) -> dict[str, Path]:
    files: dict[str, Path] = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        filenames.sort()
        base = Path(dirpath)
        for filename in filenames:
            path = base / filename
            rel = str(path.relative_to(root))
            files[rel] = path
    return files


def write_report(
    path: Path,
    mode: str,
    left_label: str,
    right_label: str,
    diff: dict[str, list[str]],
) -> None:
    no_diff = not has_differences(diff)

    lines: list[str] = []
    lines.append("verify-html-diff report")
    lines.append("")
    lines.append(f"mode: {mode}")
    lines.append(f"left: {left_label}")
    lines.append(f"right: {right_label}")
    lines.append("")
    if no_diff:
        lines.append("result: no differences under configured comparison policy.")
    else:
        lines.append("result: differences found under configured comparison policy.")
    lines.append("")
    lines.append("policy:")
    lines.append("- strict byte-for-byte file comparison")
    lines.append(
        "- paragraph-ids.json compared by normalized logical content (sorted structure)"
    )
    lines.append(
        "- searchindex.js compared by normalized JSON payload "
        "(ferrocene_spec envversion ignored)"
    )
    lines.append("- .buildinfo compares config; tags differences are ignored")
    lines.append("")
    lines.append("only in left:")
    lines.extend(format_list(diff["only_left"]))
    lines.append("")
    lines.append("only in right:")
    lines.extend(format_list(diff["only_right"]))
    lines.append("")
    lines.append("changed files:")
    lines.extend(format_list(diff["changed"]))
    lines.append("")
    lines.append("special comparisons:")
    lines.extend(format_list(diff["comparisons"]))
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def format_list(values: list[str]) -> list[str]:
    if not values:
        return ["- (none)"]
    return [f"- {value}" for value in values]


if __name__ == "__main__":
    raise SystemExit(main())
