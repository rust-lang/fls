.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Ferrocene Developers

.. default-domain:: spec

.. _fls_hdwwrsyunir:

Program Structure and Compilation
=================================

.. _fls_s35hob3i7lr:

Source Files
------------

.. rubric:: Syntax

.. syntax::

   SourceFile ::=
       ZeroWidthNoBreakSpace?
       Shebang?
       InnerAttributeOrDoc*
       Item*

   ZeroWidthNoBreakSpace ::=
       $$\u{FEFF}$$

   Shebang ::=
       $$#!$$ ~[NewLine]*

   NewLine ::=
       $$\n$$

.. rubric:: Legality Rules

.. glossary-entry:: source file
   :glossary-dp: fls_wlwwxzpnhk6i
   
   :glossary:
     :dp:`fls_nh737q4mn27u`
     A :dt:`source file` contains the program text of :t:`[inner attribute]s`,
     :t:`[inner doc comment]s`, and :t:`[item]s`.
     
     :dp:`fls_zgh1m5357ex1`
     See :s:`SourceFile`.
   :chapter:
     :dp:`fls_4vicosdeaqmp`
     A :t:`source file` contains the program text consisting of :t:`[inner
     attribute]s`, :t:`[inner doc comment]s`, and :t:`[item]s`. The location of a
     :t:`source file` is tool defined.

:dp:`fls_ann3cha1xpek`
A :s:`Shebang` does not have an effect on the compilation.

.. _fls_e9hwvqsib5d5:

Modules
-------

.. rubric:: Syntax

.. syntax::

   ModuleDeclaration ::=
       $$unsafe$$? $$mod$$ Name ModuleSpecification

   ModuleSpecification ::=
       InlineModuleSpecification
     | OutlineModuleSpecification

   InlineModuleSpecification ::=
       $${$$
         InnerAttributeOrDoc*
         Item*
       $$}$$

   OutlineModuleSpecification ::=
       $$;$$

.. rubric:: Legality Rules

.. glossary-entry:: module
   :glossary-dp: fls_kbxk78vm564e
   
   :glossary:
     :dp:`fls_ujlsg58bskl5`
     A :dt:`module` is a container for zero or more :t:`[item]s`.
     
     :dp:`fls_os60q6vvm71c`
     See :s:`ModuleDeclaration`.
   :chapter:
     :dp:`fls_odd1hj3y1mgu`
     A :t:`module` is a container for zero or more :t:`[item]s`.

:dp:`fls_whgv72emrm47`
The ``unsafe`` :t:`keyword` of a :t:`module` is rejected, but may still
be consumed by :t:`[macro]s`.

.. glossary-entry:: inline module
   :glossary-dp: fls_c54lmkluwbwr
   
   :glossary:
     :dp:`fls_tbldwtisl9vc`
     An :dt:`inline module` is a :t:`module` with an :s:`InlineModuleSpecification`.
     
     :dp:`fls_8bmjz8o3xu60`
     See :s:`InlineModuleSpecification`.
   :chapter:
     :dp:`fls_qypjjpcf8uwq`
     An :t:`inline module` is a :t:`module` with an :s:`InlineModuleSpecification`.

.. glossary-entry:: outline module
   :glossary-dp: fls_de935b1pzd28
   
   :glossary:
     :dp:`fls_xhe5gmr0r9zn`
     An :dt:`outline module` is a :t:`module` with an
     :s:`OutlineModuleSpecification`.
     
     :dp:`fls_wu5wqylzx9ke`
     See :s:`OutlineModuleSpecification`.
   :chapter:
     :dp:`fls_cavwpr1ybk37`
     An :t:`outline module` is a :t:`module` with an :s:`OutlineModuleSpecification`.
     
     :dp:`fls_plepew2319g4`
     An :t:`outline module` loads a :t:`source file` and considers the text of the
     :t:`source file` to be inlined within the context of the :t:`outline module`.

:dp:`fls_1aruwps62c4p`
The location of a :t:`module` :t:`source file` can be specified using
:t:`attribute` :c:`path`.

.. rubric:: Examples

.. code-block:: rust

   #[path = "path/to/module"]
   pub mod module {
   	#![allow(dead_code)]

        struct Struct;
        pub mod other;
   }

.. _fls_maw4u1o8q37u:

Crates
------

.. rubric:: Legality Rules

.. glossary-entry:: crate
   :glossary-dp: fls_kf8yukhxudw8
   
   :glossary:
     :dp:`fls_qplsjzb2uyim`
     A :dt:`crate` is a unit of compilation and linking that contains a tree of
     nested :t:`[module]s`.
   :chapter:
     :dp:`fls_qwghk79ok5h0`
     A :t:`crate` is a unit of compilation and linking that contains a tree of
     nested :t:`[module]s`.

.. glossary-entry:: crate type
   :glossary-dp: fls_lVpE4uFDsXH4
   
   :glossary:
     :dp:`fls_eaxsgPMFNH7f`
     The :dt:`crate type` of a :t:`crate` is the value of the :t:`attribute`
     ``crate_type`` of a :t:`crate` or the value of ``--crate-type`` flag passed to
     the tool compiling the :t:`crate`.
   :chapter:
     :dp:`fls_unxalgMqIr3v`
     The :t:`crate type` of a :t:`crate` is the value of the :t:`attribute`
     ``crate_type`` of a :t:`crate` or the value of ``--crate-type`` flag passed to
     the tool compiling the :t:`crate`.

:dp:`fls_e7jGvXvTsFpC`
The :t:`crate type` of a :t:`crate` if not specified is ``bin``.

:dp:`fls_kQiJPwb2Hjcc`
A :t:`crate` may be subject to multiple :t:`[crate type]s`, treating each type
as a separate :t:`crate`.

.. glossary-entry:: binary crate
   :glossary-dp: fls_kahj3y4rvmvb
   
   :glossary:
     :dp:`fls_8gfe7hajxkd7`
     A :dt:`binary crate` is a :t:`crate` whose :t:`crate type` is ``bin``.
   :chapter:
     :dp:`fls_9ub6ks8qrang`
     A :t:`binary crate` is a :t:`crate` whose :t:`crate type` is ``bin``.

:dp:`fls_OyFwBtDGVimT`
A :t:`binary crate` that is not subject to :t:`attribute` ``no_main`` shall have
a :t:`function` in scope of its :t:`crate root module` under the :t:`name`
``main`` with a :t:`main function signature`.

:dp:`fls_jQqXxPyND1ds`
The :t:`function` in scope of a :t:`binary crate`'s :t:`crate root module` under
the :t:`name` ``main`` with a :t:`main function signature` is the :t:`binary
crate`'s :t:`program entry point`.

.. glossary-entry:: library crate
   :glossary-dp: fls_r1sk7vdgckym
   
   :glossary:
     :dp:`fls_3m8lg4mdc2x0`
     A :dt:`library crate` is a :t:`crate` whose :t:`crate type` is ``lib``, ``rlib``,
     ``staticlib``, ``dylib``, or ``cdylib``.
   :chapter:
     :dp:`fls_d9nn4yuiw1ja`
     A :t:`library crate` is a :t:`crate` whose :t:`crate type` is ``lib``, ``rlib``,
     ``staticlib``, ``dylib``, or ``cdylib``.

.. glossary-entry:: proc-macro crate
   :glossary-dp: fls_kCA6SW8bUq5x
   
   :glossary:
     .. _fls_AjjdLZWiL9Tq:
     
     :dp:`fls_DfTszT1PjV7o`
     A :dt:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.
   :chapter:
     :dp:`fls_Mf62VqAhoZ3c`
     A :t:`proc-macro crate` is a :t:`crate` whose :t:`crate type` is ``proc-macro``.

:dp:`fls_RJJmN4tP7j4m`
A :t:`proc-macro crate` shall not declare :t:`[item]s` in its :t:`crate root
module` with  :t:`public visibility` unless the :t:`item` is a :t:`procedural
macro`.

:dp:`fls_h93C3wfbAoz1`
Only a :t:`proc-macro crate` shall declare :t:`[procedural macro]s`.

.. _fls_gklst7joeo33:

Crate Imports
-------------

.. rubric:: Syntax

.. syntax::

   ExternalCrateImport ::=
       $$extern$$ $$crate$$ CrateIndication Renaming? $$;$$

   CrateIndication ::=
       Identifier
     | $$self$$

.. rubric:: Legality Rules

.. glossary-entry:: crate import
   :glossary-dp: fls_xwbmmcbbowtu
   
   :glossary:
     :dp:`fls_y91ja1a87g7a`
     A :dt:`crate import` specifies a dependency on an external :t:`crate`.
     
     :dp:`fls_nmdxagg39hz6`
     See :s:`ExternalCrateImport`.
   :chapter:
     :dp:`fls_d0pa807s5d5h`
     A :t:`crate import` specifies a required dependency on an external :t:`crate`.

.. glossary-entry:: crate indication
   :glossary-dp: fls_CXvNvsO10pLL
   
   :glossary:
     :dp:`fls_XUSFUErxQRRA`
     A :dt:`crate indication` is a :t:`construct` that indicates a :t:`crate`.
     
     :dp:`fls_s1eFklbzjLxQ`
     See :s:`CrateIndication`.
   :chapter:
     :dp:`fls_vfam3wzeAiah`
     A :t:`crate indication` is a :t:`construct` that indicates a :t:`crate`.

:dp:`fls_ft860vkz0lkc`
A :t:`crate import` binds an external :t:`crate` to its :t:`crate indication`.

:dp:`fls_k90qtnf8kgu1`
:t:`Crate indication` ``self`` shall require a :t:`renaming`.

:dp:`fls_siv8bl6s2ndu`
A :t:`crate import` with a :t:`renaming` with an :t:`identifier` binds the
external :t:`crate` to a local :t:`name` and introduces the local :t:`name` into
the enclosing :t:`scope`.

:dp:`fls_7vz5n3x6jo1s`
If a :t:`crate import` appears at the :t:`crate root module`, then the
:t:`crate indication` is added to the :t:`external prelude`.

:dp:`fls_3bgpc8m8yk4p`
A :t:`crate indication` shall resolve to an external :t:`crate`. The process of
resolving a :t:`crate indication` to an external :t:`crate` is tool-defined.

.. _fls_5w50kf83oo1u:

Compilation Roots
-----------------

.. rubric:: Legality Rules

.. glossary-entry:: crate root
   :glossary-dp: fls_hv9zyxb72soh
   
   :glossary:
     :dp:`fls_yxcgiuybqqy8`
     A :dt:`crate root` is an entry point into a :t:`crate`.

.. glossary-entry:: crate root module
   :glossary-dp: fls_iucxone5ta26
   
   :glossary:
     :dp:`fls_oo4nmqv78wno`
     A :dt:`crate root module` is the root of the nested :t:`module` tree of a
     :t:`crate`.
   :chapter:
     :dp:`fls_fhiqvgdamq5`
     A :t:`crate root module` is the root of the nested :t:`module` tree of a
     :t:`crate`.

:dp:`fls_tk8tl2e0a34`
A tool can define a :t:`crate root module` for a single :t:`crate`.

.. glossary-entry:: compilation root
   :glossary-dp: fls_riwule1euzlj
   
   :glossary:
     :dp:`fls_stwsfyvov2fx`
     A :dt:`compilation root` is an input to a compilation performed by a tool.
   :chapter:
     :dp:`fls_bsyfxdk3ap1t`
     A :t:`compilation root` is an input to a compilation performed by a tool. A
     :t:`crate root module` is a :t:`compilation root`.

.. _fls_u1afezy1ye99:

Conditional Compilation
-----------------------

.. rubric:: Legality Rules

:dp:`fls_9stc6nul6vq9`
:t:`Conditionally-compiled source code` is source code that may or may
not be considered a part of a Rust program depending on
:t:`[configuration predicate]s`.

:dp:`fls_a0u9nnaf6drz`
:t:`Conditional compilation` is the process of compiling
:t:`conditionally-compiled source code`.

:dp:`fls_pf1v89h7pjhh`
A :t:`construct` subject to :t:`attribute` :c:`cfg` where the related
:t:`configuration predicate` evaluates to ``false`` is not considered part of a
Rust program.

:dp:`fls_y56RGw3cbFex`
A :t:`crate root module` subject to :t:`attribute` :c:`cfg` where the related
:t:`configuration predicate` evaluates to ``false`` is considered empty except
for all :t:`[attribute]s` up to the invoked :t:`attribute` :c:`cfg`.

:dp:`fls_h6b1fuw4nvi1`
An :t:`attribute` :c:`cfg_attr` where the related :t:`configuration predicate`
evaluates to ``false`` is not considered part of a Rust program.


.. _fls_8JB3SJqamdpU:

Program Entry Point
-------------------

.. rubric:: Legality Rules

.. glossary-entry:: program entry point
   :glossary-dp: fls_SIFecOZqloyx
   
   :glossary:
     :dp:`fls_9m37hN9zgEQf`
     A :dt:`program entry point` is a :t:`function` that is invoked at the start of
     a Rust program.
   :chapter:
     :dp:`fls_dp64b08em9BJ`
     A :t:`program entry point` is a :t:`function` that is invoked at the start of
     a Rust program.

.. glossary-entry:: main function signature
   :glossary-dp: fls_MJ1YWiOpxAa8
   
   :glossary:
     :dp:`fls_QijObGZEIykU`
     A :dt:`main function signature` is a :t:`function signature` subject to specific
     restrictions.
   :chapter:
     :dp:`fls_sbGnkm8Ephiu`
     A :t:`main function signature` is a :t:`function signature` subject to the
     following restrictions:
     
     * :dp:`fls_o4fxok23134r`
       It lacks :t:`[function qualifier]s` ``async`` and ``unsafe``,
     
     * :dp:`fls_bk755pvc1l53`
       Its :t:`ABI` is Rust,
     
     * :dp:`fls_a3je4wc53bmo`
       It lacks :t:`[generic parameter]s`,
     
     * :dp:`fls_w8q15zp7kyl0`
       It lacks :t:`[function parameter]s`,
     
     * :dp:`fls_4psnfphsgdek`
       It lacks a :t:`return type`,
     
     * :dp:`fls_m7xfrhqif74`
       It lacks a :t:`where clause`,
     
     * :dp:`fls_qq9fzrw4aykd`
       It has a :t:`function body`.
