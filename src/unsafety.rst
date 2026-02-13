.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Ferrocene Developers

.. default-domain:: spec

.. _fls_jep7p27kaqlp:

Unsafety
========

.. rubric:: Legality Rules

.. glossary-entry:: unsafety
   :glossary-dp: fls_pst7yov6vnr9
   
   :glossary:
     :dp:`fls_742ycx5181n`
     :dt:`Unsafety` is the presence of :t:`[unsafe operation]s` in program text.
   :chapter:
     :dp:`fls_8kqo952gjhaf`
     :t:`Unsafety` is the presence of :t:`[unsafe operation]s` and :t:`[unsafe trait
     implementation]s` in program text.

.. glossary-entry:: unsafe operation
   :glossary-dp: fls_e2wyfbem6vwn
   
   :glossary:
     :dp:`fls_34h60ubicgsj`
     An :dt:`unsafe operation` is an operation that may result in
     :t:`undefined behavior` that is not diagnosed as a static error.
     :t:`[Unsafe operation]s` are referred to as :t:`unsafe Rust`.
   :chapter:
     :dp:`fls_ovn9czwnwxue`
     An :t:`unsafe operation` is an operation that may result in
     :t:`undefined behavior` that is not diagnosed as a static error.
     :t:`[Unsafe operation]s` are referred to as :t:`unsafe Rust`.

.. glossary-entry:: unsafe Rust
   :glossary-dp: fls_4f6mppoenj3b
   
   :glossary:
     :dp:`fls_30asi010yf1a`
     For :dt:`unsafe Rust`, see :t:`[unsafe operation]s`.

:dp:`fls_pfhmcafsjyf7`
The :t:`[unsafe operation]s` are:

* :dp:`fls_jd1inwz7ulyw`
  Dereferencing a :t:`value` of a :t:`raw pointer type`.

* :dp:`fls_3ra8s1v1vbek`
  Reading or writing an :t:`external static`.

* :dp:`fls_6ipl0xo5qjyl`
  Reading or writing a :t:`mutable static`.

* :dp:`fls_ucghxcnpaq2t`
  Accessing a :t:`field` of a :t:`union`, other than to assign to it.

* :dp:`fls_ljocmnaz2m49`
  Calling an :t:`unsafe function`.

* :dp:`fls_s5nfhBFOk8Bu`
  Calling :t:`macro` :std:`core::arch::asm`.

.. glossary-entry:: unsafe context
   :glossary-dp: fls_5m85wlr2qw78
   
   :glossary:
     :dp:`fls_qn1s845ejbu0`
     An :dt:`unsafe context` is either an :t:`unsafe block` or an
     :t:`unsafe function`.
   :chapter:
     :dp:`fls_jb6krd90tjmc`
     An :t:`unsafe context` is either an :t:`unsafe block` or an
     :t:`unsafe function`.

:dp:`fls_ybnpe7ppq1vh`
An :t:`unsafe operation` shall be used only within an :t:`unsafe context`.
