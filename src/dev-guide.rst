.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Ferrocene Developers
   SPDX-FileCopyrightText: The Rust Project Contributors

.. default-domain:: spec

.. informational-page::

Developer's Guide
=================

This document outlines the various formats, processes, and procedures associated with the maintenance of the FLS.

Changelog maintenance
---------------------

The Changelog is located in ``src/changelog.rst``.
It should be updated using one of the sentence patterns outlined below.
Note that this is not an exhaustive list, and special cases would need to use their own wording.

Glossary entries
~~~~~~~~~~~~~~~~

When working with glossary entries, use the following sintence pattern for a single glossary entry::

    <Action> glossary entry: :t:`term`

Use the following sentence pattern for multiple paragraphs::

    <Action> glossary entries:
    - :t:`term`
    - :t:`term`

``<Action>`` must denote either ``Changed``, ``New``, or ``Removed``.

No change
~~~~~~~~~

Use the following sentence patterns when a PR included in a release does not require a change in the FLS::

    No change: <Reason> is outside the scope of the FLS

or::

    No change: <Reasons> are outside the scope of the FLS

Paragraphs
~~~~~~~~~~

When working with paragraphs, use the following sentence pattern for a single paragraph::

    <Action> paragraph: :p:`fls_paragraph_id`

Use the following sentence pattern for multiple paragraphs::

    <Action> paragraphs:
    - :p:`fls_paragraph_id`
    - :p:`fls_paragraph_id`

``<Action>`` must denote either ``Changed``, ``Moved``, ``New``, or ``Removed``.

Sections
~~~~~~~~

When working with sections, use the following sentence pattern for a single section::

    <Action> section :ref:`fls_section_id`

Use the following sentence pattern for multiple sections::

    <Action> sections:
    - :ref:`fls_section_id`
    - :ref:`fls_section_id`

``<Action>`` must denote either ``Moved``, ``New``, or ``Removed``.

Syntax
~~~~~~

When working with syntax, use the following sentence pattern for a single syntax category::

    <Action> syntax: :s:`syntax_category`

Use the following sentence pattern for multiple syntax categories::

    <Action> syntax:
    - :s:`syntax_category`
    - :s:`syntax_category`

``<Action>`` must denote either ``Changed``, ``New``, or ``Removed``.