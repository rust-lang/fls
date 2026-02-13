.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Ferrocene Developers
   SPDX-FileCopyrightText: The Rust Project Contributors

=====
Tools
=====

HTML diff verifier
==================

``tools/verify-html-diff.py`` exports and compares rendered HTML trees under a
configured comparison policy.

Comparison policy
-----------------

The verifier compares ``build/html/**`` with strict byte-for-byte checks and
two explicit exceptions:

* ``paragraph-ids.json`` compares normalized logical content (sorted
  structure), not raw byte order.
* ``.buildinfo`` requires matching ``config`` and ignores ``tags``
  differences.
* Build commit identity is normalized by intercepting ``git rev-parse HEAD``
  during verification builds and returning a fixed commit value.
* ``_sources/`` entries are excluded from the comparison set because they are
  source snapshots and not part of rendered output semantics.

Modes
-----

* ``--mode export-ref`` builds one git ref in an isolated worktree, exports
  ``build/html`` to ``--output-dir``, and writes ``manifest.sha256``.
* ``--mode compare-dirs`` compares two exported HTML directories.
* ``--mode refs`` builds two refs and compares their HTML output.
* ``--mode repro`` builds one ref twice and compares both outputs.

Exit codes
----------

* ``0``: success, no differences under configured comparison policy.
* ``1``: differences found.
* ``2``: operational/tooling failure.

Report location
---------------

If ``--report`` is omitted, reports default to
``$OPENCODE_CONFIG_DIR/reports/`` (or ``build/html-diff/`` when
``OPENCODE_CONFIG_DIR`` is unset).

Examples
--------

Run a reproducibility check for ``HEAD``::

   ./tools/verify-html-diff.py --mode repro --ref HEAD

Export two refs and compare them::

   ./tools/verify-html-diff.py --mode export-ref --ref <sha1> --output-dir /tmp/html-a
   ./tools/verify-html-diff.py --mode export-ref --ref <sha2> --output-dir /tmp/html-b
   ./tools/verify-html-diff.py --mode compare-dirs --left-dir /tmp/html-a --right-dir /tmp/html-b

Compare refs directly::

   ./tools/verify-html-diff.py --mode refs --left-ref <sha1> --right-ref <sha2>
