#!/usr/bin/env -S uv run
# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Ferrocene Developers

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import sys

from sphinx.application import Sphinx

ROOT = Path(__file__).resolve().parent
GLOSSARY_ANCHOR = ".. _fls_bc2qwbfibrcs:"


def load_glossary_ext():
    exts_path = str(ROOT / "exts")
    if exts_path not in sys.path:
        sys.path.append(exts_path)
    from ferrocene_spec import glossary as glossary_ext

    return glossary_ext


@dataclass
class GlossaryPrelude:
    lines: list[str]
    trailing_newline: bool


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", default="src", help="Source directory")
    parser.add_argument(
        "--prelude",
        default="src/glossary.prelude.rst.inc",
        help="Glossary prelude file",
    )
    parser.add_argument(
        "--output",
        default="build/generated.glossary.rst",
        help="Generated glossary output file",
    )
    parser.add_argument(
        "-t",
        "--tag",
        action="append",
        default=[],
        help="Sphinx tag (repeatable)",
    )
    args = parser.parse_args()

    src_dir = (ROOT / args.src).resolve()
    prelude_path = (ROOT / args.prelude).resolve()
    output_path = (ROOT / args.output).resolve()

    if not prelude_path.is_file():
        print(f"error: missing glossary prelude at {prelude_path}", file=sys.stderr)
        return 1

    prelude = load_prelude(prelude_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    tags = list(dict.fromkeys(args.tag))
    if "use_generated_glossary" in tags:
        write_lines(output_path, prelude.lines, prelude.trailing_newline)

    glossary_ext = load_glossary_ext()
    app = build_sphinx_app(src_dir, ROOT, tags)
    entries = list(glossary_ext.get_storage(app.env).values())

    exported = []
    glossary_dp_index: dict[str, str] = {}
    errors: list[str] = []

    for entry in entries:
        block = glossary_ext.select_glossary_block(entry)
        if block is None:
            if entry.chapter_lines is not None and not entry.propagate:
                warn(
                    entry.source,
                    entry.line,
                    f"glossary-entry for {entry.term} not exported",
                )
            continue

        if entry.glossary_dp is None:
            errors.append(f"missing :glossary-dp: for {entry.term}")
            continue

        existing = glossary_dp_index.get(entry.glossary_dp)
        if existing is not None:
            errors.append(
                "duplicate :glossary-dp: "
                f"{entry.glossary_dp} for {entry.term} and {existing}"
            )
            continue

        glossary_dp_index[entry.glossary_dp] = entry.term
        exported.append((entry, block))

    if errors:
        for message in errors:
            print(f"error: {message}", file=sys.stderr)
        return 1

    exported.sort(
        key=lambda item: (glossary_ext.natural_sort_key(item[0].term), item[0].term)
    )

    output_lines = list(prelude.lines)
    for entry, block in exported:
        output_lines.extend(
            glossary_ext.render_glossary_entry(entry.term, entry.glossary_dp, block)
        )
    output_lines = glossary_ext.trim_trailing_blanks(output_lines)

    write_lines(output_path, output_lines, prelude.trailing_newline)

    return 0


def build_sphinx_app(src_dir: Path, root: Path, tags: list[str]) -> Sphinx:
    build_dir = root / "build" / "glossary-env"
    out_dir = build_dir / "out"
    doctree_dir = build_dir / "doctrees"
    out_dir.mkdir(parents=True, exist_ok=True)
    doctree_dir.mkdir(parents=True, exist_ok=True)

    app = Sphinx(
        srcdir=str(src_dir),
        confdir=str(src_dir),
        outdir=str(out_dir),
        doctreedir=str(doctree_dir),
        buildername="dummy",
        status=sys.stdout,
        warning=sys.stderr,
        freshenv=True,
        warningiserror=False,
    )
    for tag in tags:
        app.tags.add(tag)
    app.build(force_all=True)
    return app


def load_prelude(prelude_path: Path) -> GlossaryPrelude:
    lines, trailing_newline = read_lines(prelude_path)
    try:
        anchor_index = lines.index(GLOSSARY_ANCHOR)
    except ValueError:
        print(
            f"error: glossary anchor {GLOSSARY_ANCHOR} not found in {prelude_path}",
            file=sys.stderr,
        )
        raise SystemExit(1)

    cursor = anchor_index + 1
    while cursor < len(lines) and lines[cursor].strip() == "":
        cursor += 1
    if cursor + 1 >= len(lines):
        print(f"error: glossary title missing in {prelude_path}", file=sys.stderr)
        raise SystemExit(1)

    title = lines[cursor].strip()
    if not title:
        print(f"error: glossary title missing in {prelude_path}", file=sys.stderr)
        raise SystemExit(1)

    after = cursor + 2
    while after < len(lines) and lines[after].strip() == "":
        after += 1

    prelude: list[str] = []
    prelude.extend(lines[:anchor_index])
    prelude.append(lines[anchor_index])
    prelude.extend(lines[anchor_index + 1 : cursor])
    prelude.append(title)
    prelude.append("=" * len(title))
    prelude.extend(lines[cursor + 2 : after])
    if not prelude or prelude[-1].strip() != "":
        prelude.append("")
    return GlossaryPrelude(lines=prelude, trailing_newline=trailing_newline)


def read_lines(path: Path) -> tuple[list[str], bool]:
    data = path.read_text(encoding="utf-8")
    return data.splitlines(), data.endswith("\n")


def write_lines(path: Path, lines: list[str], trailing_newline: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(lines)
    if trailing_newline:
        text += "\n"
    path.write_text(text, encoding="utf-8")


def warn(source: str | None, line: int | None, message: str) -> None:
    location = ""
    if source and line:
        location = f"{source}:{line}: "
    print(f"warning: {location}{message}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
