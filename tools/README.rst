.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Ferrocene Developers
   SPDX-FileCopyrightText: The Rust Project Contributors

=====
Tools
=====

HTML diff verifier
==================

``tools/verify-html-diff.py`` compares a baseline HTML build with a build that
uses the generated glossary, to ensure the generated output matches the static
glossary. It is a quick sanity check used alongside CI.

Run it from the repo root::

   ./tools/verify-html-diff.py

By default it writes output under ``build/html-diff/`` and reports a non-zero
exit code if any differences are found (see ``build/html-diff/html-diff.txt``).
Use ``--keep-output`` to reuse existing output directories and ``--output-dir``
to customize the location.
