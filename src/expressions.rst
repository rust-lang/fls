.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Ferrocene Developers

.. default-domain:: spec

.. _fls_ckvjj4tt1hh2:

Expressions
===========

.. rubric:: Syntax

.. syntax::

   Expression ::=
       ExpressionWithBlock
     | ExpressionWithoutBlock

   ExpressionWithBlock ::=
       OuterAttributeOrDoc* (
           AsyncBlockExpression
         | BlockExpression
         | ConstBlockExpression
         | IfExpression
         | IfLetExpression
         | LoopExpression
         | MatchExpression
         | UnsafeBlockExpression
         | NamedBlockExpression
       )

   ExpressionWithoutBlock ::=
       OuterAttributeOrDoc* (
           ArrayExpression
         | AwaitExpression
         | BreakExpression
         | CallExpression
         | ClosureExpression
         | ContinueExpression
         | FieldAccessExpression
         | IndexExpression
         | LiteralExpression
         | MethodCallExpression
         | MacroInvocation
         | OperatorExpression
         | ParenthesizedExpression
         | PathExpression
         | RangeExpression
         | ReturnExpression
         | StructExpression
         | TupleExpression
         | UnderscoreExpression
       )

   ExpressionList ::=
       Expression ($$,$$ Expression)* $$,$$?

   Operand ::=
       Expression

   LeftOperand ::=
       Operand

   RightOperand ::=
       Operand

.. glossary-entry:: subject expression
   :glossary-dp: fls_wee9stfk0abp
   
   :glossary:
     :dp:`fls_xisqke87ert`
     A :dt:`subject expression` is an :t:`expression` that controls
     :t:`[for loop]s`, :t:`[if expression]s`, and :t:`[match expression]s`.
     
     :dp:`fls_gph5doham4js`
     See :s:`SubjectExpression`.
   :chapter:
     :dp:`fls_pwut2jbmk66k`
     A :ds:`SubjectExpression` is any expression in category :s:`Expression`, except
     :s:`StructExpression`.

.. glossary-entry:: subject let expression
   :glossary-dp: fls_dc5ibvnnhs7e
   
   :glossary:
     :dp:`fls_b3ckv6zgnaeb`
     A :dt:`subject let expression` is an :t:`expression` that controls
     :t:`[if let expression]s` and :t:`[while let loop]s`.
     
     :dp:`fls_vnzaargh5yok`
     See :s:`SubjectLetExpression`.
   :chapter:
     :dp:`fls_361q9ljc6ybz`
     A :ds:`SubjectLetExpression` is any expression in category
     :s:`SubjectExpression`, except :s:`LazyBooleanExpression`.

.. glossary-entry:: subexpression
   :glossary-dp: fls_feZ3iDff05Cb
   
   :glossary:
     :dp:`fls_bNSHwD4Kpfm0`
     A :dt:`subexpression` is an :t:`expression` nested within another
     :t:`expression`.

.. rubric:: Legality Rules

.. glossary-entry:: expression
   :glossary-dp: fls_q8ofwncggngd
   
   :glossary:
     :dp:`fls_f7iuwgbs1lql`
     An :dt:`expression` is a :t:`construct` that produces a :t:`value`, and may
     have side effects at run-time.
     
     :dp:`fls_8l9hru1x586q`
     See :s:`Expression`.
   :chapter:
     :dp:`fls_h5o6tgul4yor`
     An :t:`expression` is a :t:`construct` that produces a :t:`value`, and may have
     side effects at run-time.

.. glossary-entry:: expression-with-block
   :glossary-dp: fls_u6huewic8650
   
   :glossary:
     :dp:`fls_ujlm50le5dnj`
     An :dt:`expression-with-block` is an :t:`expression` whose structure involves a
     :t:`block expression`.
     
     :dp:`fls_iwheys965ml3`
     See :s:`ExpressionWithBlock`.
   :chapter:
     :dp:`fls_xmklb3070sp`
     An :t:`expression-with-block` is an :t:`expression` whose structure involves a
     :t:`block expression`.

.. glossary-entry:: expression-without-block
   :glossary-dp: fls_378e2xhxzk26
   
   :glossary:
     :dp:`fls_xfh9xmsphzqb`
     An :dt:`expression-without-block` is an :t:`expression` whose structure does
     not involve a :t:`block expression`.
     
     :dp:`fls_miaphjnikd51`
     See :s:`ExpressionWithoutBlock`.
   :chapter:
     :dp:`fls_p15oeage4j0e`
     An :t:`expression-without-block` is an :t:`expression` whose structure does not
     involve a :t:`block expression`.

.. glossary-entry:: operand
   :glossary-dp: fls_pv4lok5qcn8y
   
   :glossary:
     :dp:`fls_3mnn1au9ob6q`
     An :dt:`operand` is an :t:`expression` nested within an expression.
     
     :dp:`fls_8299xfhdsd1`
     See :s:`Operand`.
   :chapter:
     :dp:`fls_gwgttltgjma4`
     An :t:`operand` is an :t:`expression` nested within an :t:`expression`.

.. glossary-entry:: binary operator
   :glossary-dp: fls_xydujcfvvb8p
   
   :glossary:
     :dp:`fls_v0he0zp9ph7a`
     A :dt:`binary operator` is an operator that operates on two :t:`[operand]s`.

.. glossary-entry:: left operand
   :glossary-dp: fls_x6vo9pysmex2
   
   :glossary:
     :dp:`fls_m821x5195ac9`
     A :dt:`left operand` is an :t:`operand` that appears on the left-hand side of a
     :t:`binary operator`.
     
     :dp:`fls_ghlbsklg7wdb`
     See :s:`LeftOperand`.
   :chapter:
     :dp:`fls_1r29rtnjlkql`
     A :t:`left operand` is an :t:`operand` that appears on the left-hand side of a
     :t:`binary operator`.

.. glossary-entry:: right operand
   :glossary-dp: fls_76o7m8vny72n
   
   :glossary:
     :dp:`fls_e1j9s4odze9b`
     A :dt:`right operand` is an :t:`operand` that appears on the right-hand side of
     a :t:`binary operator`.
     
     :dp:`fls_hq7x1t5dmdlp`
     See :s:`RightOperand`.
   :chapter:
     :dp:`fls_qxdpyf4u3hbz`
     A :t:`right operand` is an :t:`operand` that appears on the right-hand side of a
     :t:`binary operator`.

:dp:`fls_2j132xueobfv`
A :t:`subject expression` is an :t:`expression` that controls :t:`[for loop]s`,
:t:`[if expression]s`, and :t:`[match expression]s`.

:dp:`fls_a243nclqqjlu`
A :t:`subject let expression` is an :t:`expression` that controls
:t:`[if let expression]s` and :t:`[while let loop]s`.

.. rubric:: Dynamic Semantics

.. glossary-entry:: evaluation
   :glossary-dp: fls_p3gre0895k2u
   
   :glossary:
     :dp:`fls_8zmtio6razl1`
     :dt:`Evaluation` is the process by which an :t:`expression` achieves its
     runtime effects.
   :chapter:
     :dp:`fls_1223lwh4nq49`
     :t:`Evaluation` is the process by which an :t:`expression` achieves its runtime
     effects.

.. glossary-entry:: evaluated
   :glossary-dp: fls_pefe9ng1mm81
   
   :glossary:
     :dp:`fls_769tm6hn9g5e`
     See :t:`evaluation`.

.. _fls_isyftqu120l:

Expression Classification
-------------------------

.. _fls_3ut3biyra4r9:

Assignee Expressions
~~~~~~~~~~~~~~~~~~~~

.. rubric:: Legality Rules

.. glossary-entry:: assignee expression
   :glossary-dp: fls_m1mim5qdzf2u
   
   :glossary:
     :dp:`fls_wpmcexvbynbu`
     An :dt:`assignee expression` is an :t:`expression` that appears as the
     :t:`left operand` of an :t:`assignment expression`.
   :chapter:
     :dp:`fls_oqj7s9fi3j3j`
     An :t:`assignee expression` is an :t:`expression` that appears as the
     :t:`left operand` of an :t:`assignment expression`. The following
     :t:`[expression]s` are :t:`[assignee expression]s`:

* :dp:`fls_skopz71arbwa`
  :t:`[Place expression]s`,

* :dp:`fls_vxrg6preh46x`
  :t:`[Underscore expression]s`,

* :dp:`fls_yso6dmog0an2`
  :t:`[Array expression]s` of :t:`[assignee expression]s`,

* :dp:`fls_1tsdlpgkgb2u`
  :t:`[Struct expression]s` of :t:`[assignee expression]s`.

* :dp:`fls_hier3b8knpuq`
  :t:`[Tuple expression]s` of :t:`[assignee expression]s`,

* :dp:`fls_horl3qcfdb0k`
  :t:`[Tuple struct call expression]s` of :t:`[assignee expression]s`,

:dp:`fls_1smb3tj9pxsq`
:t:`[Parenthesized expression]s` are allowed to appear anywhere in
:t:`[assignee expression]s`.

.. _fls_66m4rnbssgig:

Constant Expressions
~~~~~~~~~~~~~~~~~~~~

.. rubric:: Legality Rules

.. glossary-entry:: constant expression
   :glossary-dp: fls_iofbib2gavnv
   
   :glossary:
     :dp:`fls_rmn8w4rh3juf`
     A :dt:`constant expression` is an :t:`expression` that can be evaluated
     statically.
   :chapter:
     :dp:`fls_1ji7368ieg0b`
     A :t:`constant expression` is an :t:`expression` that can be evaluated
     statically. The following :t:`[construct]s` are :t:`[constant expression]s` as
     long as their :t:`[operand]s` are also :t:`[constant expression]s` and do not
     involve :t:`[type]s` that require :t:`destruction`:

* :dp:`fls_y6ore0iwx7e0`
  :t:`[Arithmetic expression]s` of :t:`[scalar type]s`,

* :dp:`fls_xguga84v3j8u`
  :t:`[Array expression]s`,

* :dp:`fls_idxf02p7jogu`
  :t:`[Assignment expression]s`,

* :dp:`fls_6z45ss502alt`
  :t:`[Bit expression]s` of :t:`[scalar type]s`,

* :dp:`fls_wqs0792nud4e`
  :t:`[Block expression]s`,

* :dp:`fls_490a1b74fut6`
  :t:`[Call expression]s` where the callee is a :t:`constant function`,

* :dp:`fls_8nyu6phm1nji`
  :t:`[Closure expression]s` that do not :t:`capture <capturing>`,

* :dp:`fls_8wux08bmpse`
  :t:`[Comparison expression]s` of :t:`[scalar type]s`,

* :dp:`fls_v1bnk7neb82a`
  :t:`[Compound assignment expression]s`,

* :dp:`fls_6fq6bvxxvhsr`
  :t:`[Constant parameter]s`,

* :dp:`fls_to4e7imq2c0w`
  :t:`[Dereference expression]s`,

* :dp:`fls_krtbrpwf3mh0`
  :t:`[Expression statement]s`,

* :dp:`fls_3etom5uu8y4u`
  :t:`[Field access expression]s` that do not invoke the :std:`core::ops::Deref`
  :t:`trait`,

* :dp:`fls_qls0wj8bmupz`
  :t:`[If expression]s`,

* :dp:`fls_b5fraqx07wuo`
  :t:`[If let expression]s`,

* :dp:`fls_rpapnm3afan8`
  :t:`[Index expression]s`,

* :dp:`fls_fc62yaqyjpl2`
  :t:`[Infinite loop expression]s`,

* :dp:`fls_kwg8a351vc7`
  :t:`[Lazy boolean expression]s` of :t:`[scalar type]s`,

* :dp:`fls_7mjv1xd45qr4`
  :t:`[Let statement]s`,

* :dp:`fls_g7hoyfqy9mu1`
  :t:`[Literal expression]s`,

* :dp:`fls_br4g7qwfczig`
  :t:`[Match expression]s`,

* :dp:`fls_w4lpq9bs8tsc`
  :t:`[Method call expression]s` where the callee is a :t:`constant function` or
  do not invoke the :std:`core::ops::Deref` :t:`trait`,

* :dp:`fls_y1ezabo61nyk`
  :t:`[Negation expression]s` of :t:`[scalar type]s`,

* :dp:`fls_6tb74n6lu0wf`
  :t:`[Parenthesized expression]s`,

* :dp:`fls_axwrv7b3zt55`
  :t:`[Path expression]s` that resolve to :t:`[associated constant]s`,
  :t:`[constant]s`, :t:`[constant parameter]s`, :t:`[function]s`,
  :t:`[static]s`, :t:`[tuple struct]s`, and  :t:`[unit struct]s`,

* :dp:`fls_3bucpdj828bq`
  :t:`[Range expression]s`,

* :dp:`fls_fobs8ebt7dhc`
  :t:`[Struct expression]s`,

* :dp:`fls_dyo3o1h3keqr`
  :t:`[Tuple expression]s`,

* :dp:`fls_e0a1e8ddph7`
  :t:`[Type cast expression]s` that are not :t:`[pointer-to-address cast]s`,
  :t:`[function-pointer-to-address cast]s`, and :t:`[unsized coercion]s` that
  involve a :t:`trait object type`,

* :dp:`fls_zcuzhw7qkzkr`
  :t:`[Unsafe block expression]s`,

* :dp:`fls_pbpzkfo1fgtz`
  :t:`[While let loop expression]s`,

* :dp:`fls_qvofy4wkql0s`
  :t:`[While loop expression]s`.

* :dp:`fls_zyuxqty09SDO`
  All forms of :t:`[borrow]s` except those of expressions that are subject to
  :t:`drop scope extension` to the end of the program
  and which are either :t:`[mutable borrow]s`
  or borrows of expressions that result in values with :t:`interior mutability`.

:dp:`fls_3i7efddbsmn0`
An :t:`expression` is not considered a :t:`constant expression` when it
explicitly invokes an :t:`associated trait function` or uses
:t:`[arithmetic operator]s` of non-builtin :t:`[type]s` that invoke
:std:`core::ops` :t:`[trait]s`.

:dp:`fls_fmqar6o1bwqk`
It is a static error if the :t:`size operand` of an
:t:`array repetition constructor` or an :t:`array type` depends on
:t:`[generic parameter]s`.

.. glossary-entry:: constant context
   :glossary-dp: fls_mtbhv6e9izzm
   
   :glossary:
     :dp:`fls_9j6mc4i1t73z`
     A :dt:`constant context` is a :t:`construct` that requires a
     :t:`constant expression`.
   :chapter:
     :dp:`fls_kjhma680hz3g`
     A :t:`constant context` is a :t:`construct` that requires a
     :t:`constant expression`. The following :t:`[construct]s` are
     :t:`[constant context]s`:

* :dp:`fls_ljc6jq5ksbcs`
  The :t:`constant initializer` of an :t:`associated constant` or a
  :t:`constant`,

* :dp:`fls_3of516eo0kkx`
  The :t:`constant argument` for a :t:`constant parameter`,

* :dp:`fls_yiks5bvojncc`
  The default :t:`value` of a :t:`constant parameter`,

* :dp:`fls_66m2hwkju0vv`
  The :t:`discriminant initializer` of an :t:`enum variant`,

* :dp:`fls_fsn32kmwg65u`
  The :t:`size operand` of an :t:`array repetition constructor`,

* :dp:`fls_j6kffhbxdm7o`
  The :t:`size operand` of an :t:`array type`,

* :dp:`fls_ib8p7dfwddx2`
  The :t:`static initializer` of a :t:`static`.

* :dp:`fls_ucFupTeCyylb`
  The :t:`block expression` of a :t:`const block expression`.

:dp:`fls_od0h3v40kjp6`
An invocation of the :std:`core::ptr::addr_of` :t:`macro` expands to a
:t:`constant expression` allowed in any :t:`constant context` and
:t:`constant function`, subject to the same restrictions as a
:t:`immutable borrow expression`.

:dp:`fls_6sc556tz4oxd`
An invocation of the :std:`core::panic` :t:`macro` expands to a
:t:`constant expression` allowed in any :t:`constant context` and
:t:`constant function`, as long as the :t:`macro` is either invoked without
arguments, or with a single :t:`string literal` that does not
:t:`capture <capturing>` formatting arguments.

:dp:`fls_b1vfpvsdv38`
A :t:`constant expression` is evaluated statically whenever its :t:`value` is
needed.

:dp:`fls_b46nyamfqxdu`
The :t:`evaluation` of a :t:`constant expression` that results in
:t:`arithmetic overflow` :t:`[panic]s`.

:dp:`fls_ms9vey2wymqp`
It is a static error if a :t:`constant expression` either :t:`[panic]s` or
control reaches the invocation of :t:`macro` :std:`core::panic`.

:dp:`fls_XopG4yS9Q4q1`
It is a static error if the evaluation of a :t:`constant expression` results in
a :t:`value` that is unaligned.

.. rubric:: Dynamic Semantics

:dp:`fls_tg0kya5125jt`
The invocation of a :t:`constant function` follows the dynamic semantics of a
:t:`non-[constant function]` invocation.

.. _fls_zJOAmSr3Dbqk:

Diverging Expressions
~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Legality Rules

.. glossary-entry:: diverging expression
   :glossary-dp: fls_gDFsAj1Bvx7A
   
   :glossary:
     :dp:`fls_fLlNzmB34cj9`
     A :dt:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
     program flow to diverge from the normal :t:`evaluation` order.
   :chapter:
     :dp:`fls_oth9vFtcb9l4`
     A :t:`diverging expression` is an :t:`expression` whose :t:`evaluation` causes
     program flow to diverge from the normal :t:`evaluation` order.

:dp:`fls_cmBVodJMjZi7`
:t:`[Diverging expression]s` are:

* :dp:`fls_xsOgdiIzysP1`
  :t:`[Break expression]s`,

* :dp:`fls_xqxdHziqgWf5`
  :t:`[Return expression]s`,

* :dp:`fls_fU91m6DCB0ip`
  :t:`[Loop expression]s` that are not the target of any
  :t:`[break expression]s`,

* :dp:`fls_4wDpAHhnWZAB`
  :t:`[Call expression]s` and :t:`[method call expression]s` if the :t:`return
  type` of the :t:`call operand` is the :t:`never type`,

* :dp:`fls_7HA5UThwjbQj`
  Invocations of the :std:`core::panic` :t:`macro`,

* :dp:`fls_pdDr8Lk1GQ0T`
  Any :t:`expression` whose :t:`evaluation` requires the :t:`evaluation` of a
  diverging :t:`subexpression` on all reachable control flow paths.

.. _fls_6ydylimiv553:

Place Expressions
~~~~~~~~~~~~~~~~~

.. rubric:: Legality Rules

.. glossary-entry:: place
   :glossary-dp: fls_5zjHBZMsCqJZ
   
   :glossary:
     :dp:`fls_uCTiUBWHMPY9`
     A :dt:`place` is a location where a :t:`value` resides.

.. glossary-entry:: place expression
   :glossary-dp: fls_7x6jhh0sz2f
   
   :glossary:
     :dp:`fls_z6mgu2mk142r`
     A :dt:`place expression` is an :t:`expression` that represents a memory
     location.
   :chapter:
     :dp:`fls_qbrcg3cl9td`
     A :t:`place expression` is an :t:`expression` that represents a memory
     location. The following :t:`[expression]s` are :t:`[place expression]s`:

* :dp:`fls_jpmhibm4omm7`
  :t:`[Dereference expression]s`,

* :dp:`fls_none1dykbn8c`
  :t:`[Field access expression]s`,

* :dp:`fls_lj7x5dgbmg9i`
  :t:`[Index expression]s`,

* :dp:`fls_anzidgx02lly`
  :t:`[Parenthesized expression]s` where the :t:`operand` is a
  :t:`place expression`,

* :dp:`fls_ya05djl1d154`
  :t:`[Path expression]s` that resolve to a :t:`static` or a :t:`variable`.

* :dp:`fls_gv4M0DE3OMwk`
  A :t:`temporary`.

.. glossary-entry:: mutable place expression
   :glossary-dp: fls_7eyza445ew53
   
   :glossary:
     :dp:`fls_kq877s3vij70`
     A :dt:`mutable place expression` is a :t:`place expression` whose memory
     location can be modified.
   :chapter:
     :dp:`fls_ku38h562vfyl`
     A :t:`mutable place expression` is a :t:`place expression` whose memory
     location can be modified. The following :t:`[place expression]s` are
     :t:`[mutable place expression]s`:

* :dp:`fls_1tq2o2huda9l`
  A :t:`dereference expression` whose :t:`operand`'s :t:`type` implements the
  :std:`core::ops::DerefMut` :t:`trait`,

* :dp:`fls_6b4rwkrc1ap6`
  A :t:`dereference expression` whose :t:`operand`'s :t:`type` is a
  :t:`mutable raw pointer type`,

* :dp:`fls_s4bhrpykzmm7`
  A :t:`dereference expression` whose :t:`operand`'s :t:`type` is a
  :t:`mutable reference type`,

* :dp:`fls_xm0gm2q27x2e`
  A :t:`field access expression` where the :t:`container operand` is a
  :t:`mutable place expression`,

* :dp:`fls_bt50fltfqcvn`
  An :t:`index expression` whose :t:`type` implements the
  :std:`core::ops::IndexMut` :t:`trait`,

* :dp:`fls_Sgfxp186GMvz`
  :t:`[Parenthesized expression]s` where the :t:`operand` is a
  :t:`mutable place expression`,

* :dp:`fls_ilaqmj3hc5uv`
  A :t:`path expression` that resolves to a :t:`mutable static`,

* :dp:`fls_m0gbw9myylv2`
  A :t:`path expression` that resolves to a :t:`mutable variable` that is not
  currently borrowed,

* :dp:`fls_dcm3yr3y9y0a`
  A :t:`temporary`.

.. glossary-entry:: immutable place expression
   :glossary-dp: fls_TXQzFM77s4uj
   
   :glossary:
     :dp:`fls_MXBEZjzBxw5Z`
     An :dt:`immutable place expression` is a :t:`place expression` whose memory
     location cannot be modified.
   :chapter:
     :dp:`fls_cPEMHZtPkctX`
     An :t:`immutable place expression` is a :t:`place expression` whose memory
     location cannot be modified. All :t:`[place expression]s` that are not
     :t:`[mutable place expression]s` are :t:`[immutable place expression]s`.

.. glossary-entry:: place expression context
   :glossary-dp: fls_tshbqttxdox1
   
   :glossary:
     :dp:`fls_fqcx8suiy5k`
     A :dt:`place expression context` is a :t:`construct` that may evaluate its
     operand as a memory location.
   :chapter:
     :dp:`fls_4vxi1ji93dxb`
     A :t:`place expression context` is a :t:`construct` that may evaluate its
     :t:`operand` as a memory location.

:dp:`fls_fzsrdrHnndRd`
The following :t:`[construct]s` are :t:`[place expression context]s`:

* :dp:`fls_ZED5wJQVO6nf`
  The :t:`assignee operand` of an :t:`assignment expression` or a
  :t:`compound assignment expression`,

* :dp:`fls_Ufz9W5vyZkv3`
  The :t:`operand` of a :t:`borrow expression`,

* :dp:`fls_K7SbApHPmwjM`
  The :t:`operand` of a :t:`raw borrow expression`,

* :dp:`fls_KxWIzoh9WwK7`
  The :t:`operand` of a :t:`dereference expression`,

* :dp:`fls_oV9Hd6OiFAZX`
  The :t:`container operand` of a :t:`field access expression`,

* :dp:`fls_NnGiNsH6Zgmp`
  The initialization :t:`expression` of a :t:`let statement`,

* :dp:`fls_jLZlxIHr4w2v`
  The :t:`operand` of an :t:`implicit borrow`,

* :dp:`fls_giZ7w1G02JSg`
  The :t:`indexed operand` of an :t:`index expression`,

* :dp:`fls_5yXuTLQOQ3cc`
  The :t:`subject let expression` of an :t:`if let expression` or a
  :t:`while let loop expression`,

* :dp:`fls_nman7mJVSQlm`
  The :t:`subject expression` of a :t:`match expression`,

* :dp:`fls_JBfZuFDQg3mU`
  The :t:`base initializer` of a :t:`struct expression`.

.. glossary-entry:: immutable place expression context
   :glossary-dp: fls_O0924m8mSfIa
   
   :glossary:
     :dp:`fls_UvrQ49dSoQGc`
     An :dt:`immutable place expression context` is a :t:`place expression context`
     whose memory location cannot be modified.

.. glossary-entry:: mutable place expression context
   :glossary-dp: fls_x5BKVLc4KDlK
   
   :glossary:
     :dp:`fls_2ixH8LWGHi3k`
     A :dt:`mutable place expression context` is a :t:`place expression context`
     that may evaluate its :t:`operand` as a mutable memory location.
   :chapter:
     :dp:`fls_wxGAOWEVT77u`
     A :t:`mutable place expression context` is a :t:`place expression context` that
     may evaluate its :t:`operand` as a mutable memory location. The following
     :t:`[construct]s` are :t:`[mutable place expression context]s`:

* :dp:`fls_qytgkbhqr5ln`
  The :t:`indexed operand` of an :t:`index expression` if evaluated in a
  :t:`mutable place expression context`,

* :dp:`fls_5gy92rsi2mqm`
  The :t:`assignee operand` of an :t:`assignment expression` or a
  :t:`compound assignment expression`,

* :dp:`fls_u80htrnr2ebz`
  The :t:`operand` of a mutable :t:`borrow expression`,

* :dp:`fls_o0feajus3jtu`
  The :t:`operand` of a :t:`dereference expression` if evaluated in a
  :t:`mutable place expression context`,

* :dp:`fls_ffjx1d5dseo4`
  The :t:`container operand` of :t:`field access expression` if evaluated in a
  :t:`mutable place expression context`,

* :dp:`fls_9r7dopqf1nzl`
  The :t:`subject let expression` of an :t:`if let expression` or a
  :t:`while let loop expression`,

* :dp:`fls_o76QXHyrrJPG`
  The :t:`operand` of a mutable :t:`implicit borrow`,

* :dp:`fls_ka5b87tkf8t6`
  The initialization :t:`expression` of a :t:`let statement`,

* :dp:`fls_brwv1zwu37e8`
  The :t:`subject expression` of a :t:`match expression`,

:dp:`fls_4axr4V0icdBP`
A :t:`place expression` that is evaluated in a :t:`value expression context`
or bound :t:`by value` in a :t:`pattern` denotes the :t:`value` held in the
memory location of the :t:`place expression`. Such an evaluation is subject to
:t:`[passing convention]s`.

.. _fls_e7zgqroy2qxn:

Value Expressions
~~~~~~~~~~~~~~~~~

.. rubric:: Legality Rules

.. glossary-entry:: value expression
   :glossary-dp: fls_h03noz6jzpyl
   
   :glossary:
     :dp:`fls_mn6tcuz5j3p`
     A :dt:`value expression` is an :t:`expression` that represents a :t:`value`.
   :chapter:
     :dp:`fls_7q4hrt6yfr9b`
     A :t:`value expression` is an :t:`expression` that represents a :t:`value`.
     All :t:`[expression]s` that are not :t:`[place expression]s` are
     :t:`[value expression]s`.

.. glossary-entry:: value expression context
   :glossary-dp: fls_7xiaXXSwy4GP
   
   :glossary:
     :dp:`fls_NGGZEbmoLRbD`
     A :dt:`value expression context` is an expression context that is not a
     :t:`place expression context`.
   :chapter:
     :dp:`fls_pB6xlp4uAg37`
     A :t:`value expression context` is an expression context that is not a
     :t:`place expression context`.

:dp:`fls_8uhfwqurbyqf`
The evaluation of a :t:`value expression` in a :t:`place expression context`
shall evaluate the :t:`value expression` as a :t:`temporary` and then use the
:t:`temporary` in the :t:`place expression context`.

.. _fls_h0dvogc64tfh:

Literal Expressions
-------------------

.. rubric:: Syntax

.. syntax::

   LiteralExpression ::=
       Literal

.. rubric:: Legality Rules

.. glossary-entry:: literal expression
   :glossary-dp: fls_b57clq8jhw5w
   
   :glossary:
     :dp:`fls_otaauusc24v5`
     A :dt:`literal expression` is an :t:`expression` that denotes a :t:`literal`.
     
     :dp:`fls_7po7zobtlhzn`
     See :s:`LiteralExpression`.
   :chapter:
     :dp:`fls_rbwwczom3agt`
     A :t:`literal expression` is an :t:`expression` that denotes a :t:`literal`.

:dp:`fls_w30su9x4q13r`
The :t:`type` of a :t:`literal expression` is the :t:`type` of the corresponding
:t:`literal`.

:dp:`fls_wdpbg5xzgmwu`
The :t:`value` of a :t:`literal expression` is the :t:`value` of the
corresponding :t:`literal`.

.. rubric:: Dynamic Semantics

:dp:`fls_g061yzws1m45`
The :t:`evaluation` of a :t:`literal expression` has no effect.

.. rubric:: Examples

.. code-block:: rust

   5
   'a'
   "hello"

.. _fls_6l60b5hwnjbm:

Path Expressions
----------------

.. rubric:: Syntax

.. syntax::

   PathExpression ::=
       UnqualifiedPathExpression
     | QualifiedPathExpression

.. rubric:: Legality Rules

.. glossary-entry:: path expression
   :glossary-dp: fls_1xdj34py8zc3
   
   :glossary:
     :dp:`fls_4ik66nmvx5hn`
     A :dt:`path expression` is a :t:`path` that acts as an :t:`expression`.
     
     :dp:`fls_3qjpjqm0legc`
     See :s:`PathExpression`.
   :chapter:
     :dp:`fls_gvanx4874ycy`
     A :t:`path expression` is an :t:`expression` that denotes a :t:`path`.

:dp:`fls_EOkrcIj9CuhV`
A :t:`path expression` shall resolve to either a :t:`constant parameter`, a
:t:`constant`, a :t:`function`, a :t:`static`, a :t:`tuple enum variant`, a
:t:`tuple struct`, a :t:`unit enum variant`, a :t:`unit struct`, or a
:t:`variable`.

:dp:`fls_gz67ju6l7uhn`
A :t:`path expression` that resolves to a :t:`mutable static` shall require
:t:`unsafe context`.

:dp:`fls_cjywisyiyti6`
The :t:`type` of a :t:`path expression` is the :t:`type` of the :t:`entity` that
it resolved to.

:dp:`fls_5ifai8nkp5ek`
The :t:`value` of a :t:`path expression` is the :t:`entity` that it resolved to.

.. rubric:: Examples

.. code-block:: rust

   globals::STATIC_VARIABLE
   Vec::<i32>::push

.. _fls_hndm19t57wby:

Block Expressions
-----------------

.. rubric:: Syntax

.. syntax::

   BlockExpression ::=
       $${$$
         InnerAttributeOrDoc*
         StatementList
       $$}$$

   StatementList ::=
       Statement* Expression?

.. rubric:: Legality Rules

.. glossary-entry:: block expression
   :glossary-dp: fls_c5qn7wjk0mnx
   
   :glossary:
     :dp:`fls_gvjvzxi2xps4`
     A :dt:`block expression` is an :t:`expression` that sequences expressions and
     :t:`[statement]s`.
     
     :dp:`fls_h8j9t2xq2i1u`
     See :s:`BlockExpression`.
   :chapter:
     :dp:`fls_nf65p0l0v0gr`
     A :t:`block expression` is an :t:`expression` that sequences :t:`[expression]s`
     and :t:`[statement]s`.

.. glossary-entry:: tail expression
   :glossary-dp: fls_psd2ll10ixs
   
   :glossary:
     :dp:`fls_6k873f1knasi`
     A :dt:`tail expression` is the last :t:`expression` within a
     :t:`block expression`.
   :chapter:
     :dp:`fls_tn3hj7k2lliu`
     A :t:`tail expression` is the last :t:`expression` within a :t:`block
     expression`.

:dp:`fls_DfCne8YWevLE`
When the remaining :t:`[lexical element]s` of a :s:`StatementList` match either
an :s:`Expression` or :s:`Statement` they are interpreted as an :s:`Expression`.

:dp:`fls_u4gj2lnkq9ub`
The :t:`type` of a :t:`block expression` is determined as follows:

* :dp:`fls_ltEygvWDtHXE`
  If the :t:`block expression` contains at least one :t:`break expression` and
  has a :t:`tail expression`, then the :t:`type` is the :t:`unified type` of
  the :t:`[break type]s` of all :t:`[break expression]s` and the :t:`type` of the
  :t:`tail expression`.

* :dp:`fls_97v4fnekrRXI`
  Otherwise, if the :t:`block expression` contains at least one
  :t:`break expression`, then the :t:`type` is the :t:`unified type` of the
  :t:`[break type]s` of all :t:`[break expression]s`.

* :dp:`fls_ob76y2ymdd27`
  Otherwise, if the :t:`block expression` has a :t:`tail expression`, then the
  :t:`type` is the :t:`type` of the :t:`tail expression`.

* :dp:`fls_u0avbm147nyh`
  Otherwise the :t:`type` is the :t:`unit type`.

:dp:`fls_1hzup0sf8l7l`
The :t:`value` of a :t:`block expression` is determined as follows:

* :dp:`fls_kKZPKvJ902cw`
  If the :t:`block expression` contains at least one :t:`break expression` and
  a :t:`break expression` broke out the :t:`block expression`, then the
  :t:`value` is the :t:`break value` of the :t:`break expression` that
  broke out of the :t:`block expression`.

* :dp:`fls_9nmssjseq3jt`
  Otherwise, if the :t:`block expression` has a :t:`tail expression`, then the
  :t:`value` is the :t:`value` of the :t:`tail expression`.

* :dp:`fls_a3ulnvyc1ut`
  Otherwise the :t:`value` is the :t:`unit value`.

.. rubric:: Dynamic Semantics

:dp:`fls_elcl73psruxw`
The :t:`evaluation` of a :t:`block expression` proceeds as follows:

#. :dp:`fls_13b5n127rj92`
   Each :t:`statement` is executed in declarative order.

#. :dp:`fls_nzdpw59plr2g`
   The :t:`tail expression` is evaluated.

.. rubric:: Examples

.. code-block:: rust

   {
       fn_call();
       42
   }

.. _fls_aadan19t5006:

Async Blocks
~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   AsyncBlockExpression ::=
       $$async$$ $$move$$? BlockExpression

.. rubric:: Legality Rules

.. glossary-entry:: async block
   :glossary-dp: fls_9speqyus5ku3
   
   :glossary:
     :dp:`fls_pf6lrmcjywoj`
     For :dt:`async block`, see :t:`async block expression`.

.. glossary-entry:: async block expression
   :glossary-dp: fls_n5m58be9jnjj
   
   :glossary:
     :dp:`fls_p6nvfs7bfoxd`
     An :dt:`async block expression` is a :t:`block expression` that is specified
     with :t:`keyword` ``async`` and encapsulates behavior which is executed in
     an asynchronous manner.
     
     :dp:`fls_je689rormhd6`
     See :s:`AsyncBlockExpression`.
   :chapter:
     :dp:`fls_hhidi5ukxo`
     An :t:`async block expression` is a :t:`block expression` that is specified
     with :t:`keyword` ``async`` and encapsulates behavior which is executed in
     an asynchronous manner.

:dp:`fls_oisws5qykedi`
An :t:`async block expression` denotes a new :t:`async control flow boundary`.

:dp:`fls_tzclkasinpoq`
An :t:`async block expression` is subject to :t:`capturing`.

:dp:`fls_ncd0wkgtldem`
The :t:`type` of an :t:`async block expression` is a unique anonymous :t:`type`
that implement the :std:`core::future::Future` trait.

:dp:`fls_pvnofoomgwl5`
The :t:`value` of an :t:`async block expression` is a :t:`value` of the
:t:`async block expression`'s :t:`type`.

.. rubric:: Dynamic Semantics

:dp:`fls_9ghp5yet75y6`
The :t:`evaluation` of an :t:`async block expression` produces a :t:`value` of
the :t:`type` of the :t:`async block expression` that :t:`captures <capturing>`
the :t:`[capture target]s` of the :t:`async block expression`.

.. rubric:: Examples

.. code-block:: rust

   async {
       42
   }

.. _fls_G59PiNQkVUnQ:

Const Blocks
~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   ConstBlockExpression ::=
       $$const$$ BlockExpression

.. rubric:: Legality Rules

.. glossary-entry:: const block expression
   :glossary-dp: fls_vuBjK3kdImTn
   
   :glossary:
     :dp:`fls_5ApoJzRSTZGH`
     A :dt:`const block expression` is a :t:`block expression` that is specified
     with :t:`keyword` ``const`` and encapsulates behavior which is evaluated
     statically.
   :chapter:
     :dp:`fls_0lcunL4bo8ka`
     A :t:`const block expression` is a :t:`block expression` that is specified
     with :t:`keyword` ``const`` and encapsulates behavior which is evaluated
     statically.

:dp:`fls_veEGzEbpT4ny`
An :t:`const block expression` denotes a new :t:`control flow boundary`.

:dp:`fls_PiUS1hF3dv9U`
The :t:`block expression` of a :t:`const block expression` shall be a
:t:`constant expression`.

:dp:`fls_wuwb0SnpP6Zu`
The :t:`type` of a :t:`const block expression` is the :t:`type` of the
containing :t:`block expression`.

:dp:`fls_2i7TD7VoQk4B`
The :t:`value` of a :t:`const block expression` is the :t:`value` of the
contained :t:`block expression`.

.. rubric:: Examples

.. code-block:: rust

   const {
       42
   }

.. _fls_0ybsR1hEo7wV:

Named Blocks
~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   NamedBlockExpression ::=
       Label BlockExpression

.. rubric:: Legality Rules

.. glossary-entry:: named block expression
   :glossary-dp: fls_CxzbzLu4pWPY
   
   :glossary:
     :dp:`fls_ivFb8uAMVY3Q`
     A :dt:`named block expression` is a :t:`block expression` with a :t:`label`.
   :chapter:
     :dp:`fls_J8wJNfcSAYrS`
     A :t:`named block expression` is a :t:`block expression` with a :t:`label`.

:dp:`fls_B4NBv2jfZLuy`
The :t:`type` of the :t:`named block expression` is the :t:`type` of its
:t:`block expression`.

:dp:`fls_YxvAUUYAPkaq`
The :t:`value` of the :t:`named block expression` is the :t:`value` of its
:t:`block expression`.

.. rubric:: Examples

.. code-block:: rust

   'block: {
       break 'block 1;
       3
   }

.. _fls_8wnyln2nmg4y:

Unsafe Blocks
~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   UnsafeBlockExpression ::=
       $$unsafe$$ BlockExpression

.. rubric:: Legality Rules

.. glossary-entry:: unsafe block
   :glossary-dp: fls_6349nvapfj9d
   
   :glossary:
     :dp:`fls_8tkolhmd6xfp`
     For :dt:`unsafe block`, see :t:`unsafe block expression`.

.. glossary-entry:: unsafe block expression
   :glossary-dp: fls_u8sdp2fxz9pn
   
   :glossary:
     :dp:`fls_et2h89jyivhs`
     An :dt:`unsafe block expression` is a :t:`block expression` that is specified
     with :t:`keyword` ``unsafe``.
     
     :dp:`fls_c94rudunhp5b`
     See :s:`UnsafeBlockExpression`.
   :chapter:
     :dp:`fls_2az5huhcxzzy`
     An :t:`unsafe block expression` is a :t:`block expression` that is specified
     with :t:`keyword` ``unsafe``.

:dp:`fls_5ucvvja4dzoc`
An :t:`unsafe block expression` allows :t:`unsafety`.

:dp:`fls_j3mmg317q442`
The :t:`type` of the :t:`unsafe block expression` is the :t:`type` of its
:t:`block expression`.

:dp:`fls_nygurv3x3wq6`
The :t:`value` of the :t:`unsafe block expression` is the :t:`value` of its
:t:`block expression`.

.. rubric:: Dynamic Semantics

:dp:`fls_pv5gcy3tbjwo`
The :t:`evaluation` of an :t:`unsafe block expression` evaluates its
:t:`block expression`.

.. rubric:: Examples

.. code-block:: rust

   unsafe {
       unsafe_fn_call()
   }

.. _fls_izdv9i4spokw:

Operator Expressions
--------------------

.. rubric:: Syntax

.. syntax::

   OperatorExpression ::=
       ArithmeticExpression
     | AssignmentExpression
     | BitExpression
     | BorrowExpression
     | ComparisonExpression
     | CompoundAssignmentExpression
     | DereferenceExpression
     | ErrorPropagationExpression
     | LazyBooleanExpression
     | NegationExpression
     | RawBorrowExpression
     | TypeCastExpression

.. rubric:: Legality Rules

.. glossary-entry:: operator expression
   :glossary-dp: fls_smk8mi72lt57
   
   :glossary:
     :dp:`fls_6ev01xwcfow1`
     An :dt:`operator expression` is an :t:`expression` that involves an operator.
     
     :dp:`fls_qdszbyeuo7w1`
     See :s:`OperatorExpression`.
   :chapter:
     :dp:`fls_ursc5ynymoy`
     An :t:`operator expression` is an :t:`expression` that involves an operator.

.. glossary-entry:: unary operator
   :glossary-dp: fls_p032easjag3d
   
   :glossary:
     :dp:`fls_p6mk2zrwgwem`
     A :dt:`unary operator` operates on one :t:`operand`.

.. rubric:: Dynamic Semantics

:dp:`fls_lSxXWxJn0vMO`
An :t:`operator expression` that operates with :t:`[floating-point value]s` run as a :t:`constant expression` is allowed to yield different :t:`[value]s` compared to when run as a non-:t:`constant expression`.

.. _fls_qztk0bkju9u:

Borrow Expression
~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   BorrowExpression ::=
       $$&$$ $$mut$$? Operand

.. rubric:: Legality Rules

.. glossary-entry:: borrow expression
   :glossary-dp: fls_u0hymkjwyur7
   
   :glossary:
     :dp:`fls_2f55piwg78ru`
     A :dt:`borrow expression` is an :t:`expression` that borrows the :t:`value`
     of its :t:`operand` and creates a :t:`reference` to the memory location of its
     operand.
     
     :dp:`fls_c3hydbp2exok`
     See :s:`BorrowExpression`.
   :chapter:
     :dp:`fls_nnqfkl228hjx`
     A :t:`borrow expression` is an :t:`expression` that borrows the :t:`value` of
     its :t:`operand` and creates a :t:`reference` to the memory location of its
     :t:`operand`.

.. glossary-entry:: immutable borrow expression
   :glossary-dp: fls_pqunxp6io1n9
   
   :glossary:
     :dp:`fls_dojod5pg4r7l`
     An :dt:`immutable borrow expression` is a :t:`borrow expression` that lacks
     :t:`keyword` ``mut``.
   :chapter:
     :dp:`fls_r7ix8webgqlm`
     An :t:`immutable borrow expression` is a :t:`borrow expression` that lacks
     :t:`keyword` ``mut``.

.. glossary-entry:: shared borrow
   :glossary-dp: fls_c9xwhhg639u5
   
   :glossary:
     :dp:`fls_gmbskxin90zi`
     A :dt:`shared borrow` is a :t:`borrow` produced by evaluating an
     :t:`immutable borrow expression`.

.. glossary-entry:: mutable borrow expression
   :glossary-dp: fls_kw3oiotr98tt
   
   :glossary:
     :dp:`fls_80kcc4y21hu6`
     A :dt:`mutable borrow expression` is a :t:`borrow expression` that has
     :t:`keyword` ``mut``.
   :chapter:
     :dp:`fls_50j167r4v61b`
     A :t:`mutable borrow expression` is a :t:`borrow expression` that has
     :t:`keyword` ``mut``.

:dp:`fls_ya77l2zgtilp`
When the :t:`operand` of a :t:`borrow expression` is a :t:`place expression`,
the :t:`borrow expression` produces a :t:`reference` to the memory location
indicated by the :t:`operand`. The memory location is placed in a borrowed
state, or simply :t:`borrowed`.

.. glossary-entry:: borrowed
   :glossary-dp: fls_gl84828b074a
   
   :glossary:
     :dp:`fls_3gnps2s95ck4`
     A memory location is :dt:`borrowed` when a :t:`reference` pointing to it is
     :t:`active`.

:dp:`fls_chr03xll75d`
The :t:`type` of a :t:`borrow expression` is determined as follows:

* :dp:`fls_5b2x5ri2w54r`
  If the :t:`borrow expression` denotes an :t:`immutable borrow expression`, then the
  :t:`type` is ``&T``, where ``T`` is the :t:`type` of the :t:`operand`.

* :dp:`fls_agl09ia869rk`
  If the :t:`borrow expression` denotes a :t:`mutable borrow expression`, then the
  :t:`type` is ``&mut T``, where ``T`` is the :t:`type` of the :t:`operand`.

:dp:`fls_8cvmee9bzs40`
The :t:`value` of a :t:`borrow expression` is the address of its :t:`operand`.

:dp:`fls_LuaPBicDlDTT`
It is a static error if a :t:`borrow expression` would create an unaligned
reference to a :t:`field` in an :t:`abstract data type` subject to
:t:`attribute` :c:`repr`.

.. rubric:: Dynamic Semantics

:dp:`fls_2jd0mgw4zja4`
The :t:`evaluation` of a :t:`borrow expression` evaluates its :t:`operand`.

.. rubric:: Examples

.. code-block:: rust

   let mut answer = 42;

:dp:`fls_350qejoq9i23`
Mutable borrow.

.. syntax::

   let ref_answer = &mut answer;

.. _fls_vXGuvRWOLbEE:

Raw Borrow Expression
~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   RawBorrowExpression ::=
       $$&$$ $$raw$$ ($$const$$ | $$mut$$) Operand

.. rubric:: Legality Rules

.. glossary-entry:: raw borrow expression
   :glossary-dp: fls_YLhE2qpzYXRK
   
   :glossary:
     :dp:`fls_Fe39wLb0vvEg`
     A :dt:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.
     
     :dp:`fls_I71jq8BGyLqi`
     See :s:`RawBorrowExpression`.
   :chapter:
     :dp:`fls_TS6DvMon5h27`
     A :t:`raw borrow expression` is an :t:`expression` that creates a :t:`raw pointer` to the memory location of its :t:`operand` without incurring a :t:`borrow`.

:dp:`fls_UtjWrE2qeplQ`
An :dt:`immutable raw borrow expression` is a :t:`raw borrow expression` that has :t:`keyword` ``const``.

:dp:`fls_4e7EE4a8Yvmy`
A :dt:`mutable raw borrow expression` is a :t:`raw borrow expression` that has :t:`keyword` ``mut``.

:dp:`fls_gOXUWePymgGV`
When the :t:`operand` of a :t:`raw borrow expression` is a :t:`place expression`, the :t:`raw borrow expression` produces a :t:`raw pointer` to the memory location indicated by the :t:`operand`.

:dp:`fls_YBC8GrIBzZbi`
It is a static error if the :t:`operand` of a :t:`raw borrow expression` is a :t:`temporary`.

:dp:`fls_Twkre8IzUa8S`
The :t:`type` of a :t:`raw borrow expression` is determined as follows:

* :dp:`fls_Ki4FOzJMqtvJ`
  If the :t:`raw borrow expression` denotes an :t:`immutable raw borrow expression`, then the :t:`type` is ``*const T``, where ``T`` is the :t:`type` of the :t:`operand`.

* :dp:`fls_DJxQDBsO9hc7`
  If the :t:`raw borrow expression` denotes a :t:`mutable raw borrow expression`, then the :t:`type` is ``*mut T``, where ``T`` is the :t:`type` of the :t:`operand`.

:dp:`fls_WlXB0AHifCdd`
The :t:`value` of a :t:`raw borrow expression` is the address of its :t:`operand`.

.. rubric:: Dynamic Semantics

:dp:`fls_qQrV8QuGGcVO`
The :t:`evaluation` of a :t:`raw borrow expression` evaluates its :t:`operand`.

.. rubric:: Examples

.. code-block:: rust

   let mut answer = 42;

:dp:`fls_dTABiwAPGhdZ`
Mutable raw borrow.

.. syntax::

   let ref_answer = &raw mut answer;

.. _fls_5cm4gkt55hjh:

Dereference Expression
~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   DereferenceExpression ::=
       $$*$$ Operand

.. rubric:: Legality Rules

.. glossary-entry:: dereference expression
   :glossary-dp: fls_o588wfq878rm
   
   :glossary:
     :dp:`fls_3cuyhbh2llei`
     A :dt:`dereference expression` is an :t:`expression` that obtains the
     pointed-to memory location of its :t:`operand`.
     
     :dp:`fls_hx0jwahdb1nf`
     See :s:`DereferenceExpression`.
   :chapter:
     :dp:`fls_f6wktzofzdn1`
     A :t:`dereference expression` is an :t:`expression` that obtains the pointed-to
     memory location of its :t:`operand`.

.. glossary-entry:: dereference
   :glossary-dp: fls_127n1n5ssk2b
   
   :glossary:
     :dp:`fls_hk97pb1qt04y`
     A :dt:`dereference` is the memory location produced by evaluating a
     :t:`dereference expression`.

:dp:`fls_aeh5pzpcjveq`
When the :t:`operand` of a :t:`dereference expression` is of a :t:`pointer
type`, the :t:`dereference expression` denotes the pointed-to memory location of
the :t:`operand`, or the :t:`dereference` of the :t:`operand`.

:dp:`fls_9cc0ml2sru6x`
The :t:`dereference` is assignable when the :t:`dereference expression` is a
:t:`mutable place expression`.

:dp:`fls_8i4jzksxlrw0`
Dereferencing a :t:`raw pointer` shall require :t:`unsafe context` unless the :t:`dereference expression` is the :t:`operand` of a :t:`raw borrow expression`.

:dp:`fls_d68ddlse4zp`
If the context of a :t:`dereference expression` is an
:t:`immutable place expression context`, then the :t:`dereference expression`
is equivalent to :t:`expression` ``*core::ops::Deref::deref(&operand)``.

:dp:`fls_g73vguanbs1x`
If the context of a :t:`dereference expression` is a
:t:`mutable place expression context`, then the :t:`dereference expression`
is equivalent to :t:`expression`
``*core::ops::DerefMut::deref_mut(&mut operand)``.

:dp:`fls_8ibfqxtnahzx`
The :t:`type` of a :t:`dereference expression` is determined as follows:

* :dp:`fls_7e7tka4f2f1a`
  If the :t:`type` of the :t:`operand` is ``&mut T``, ``&T``, ``*mut T``, or
  ``*const T``, then the :t:`type` is ``T``.

* :dp:`fls_y9bc691kkh6v`
  Otherwise the :t:`type` is :t:`associated type`
  :std:`core::ops::Deref::Target`.

:dp:`fls_gw49nukfveib`
The :t:`value` of a :t:`dereference expression` is determined as follows:

* :dp:`fls_jjf3sz9ddfhy`
  If the :t:`type` of the :t:`operand` is ``&mut T``, ``&T``, ``*mut T``, or
  ``*const T``, then the :t:`value` is the pointed-to :t:`value`.

* :dp:`fls_fyend8kkpqq4`
  Otherwise the :t:`value` is the result of evaluating :t:`expression`
  ``*core::ops::Deref::deref(&operand)`` or :t:`expression`
  ``*core::ops::DerefMut::deref_mut(&mut operand)`` respectively.

.. rubric:: Dynamic Semantics

:dp:`fls_72bpdsxxbgeq`
The :t:`evaluation` of a :t:`dereference expression` evaluates its :t:`operand`.

.. glossary-entry:: dangling
   :glossary-dp: fls_76cj65bptdpn
   
   :glossary:
     :dp:`fls_lq2urzh7bzxx`
     A :t:`value` of an :t:`indirection type` is :dt:`dangling` if it is either
     :c:`null` or not all of the bytes at the referred memory location are part of
     the same allocation.

.. rubric:: Undefined Behavior

:dp:`fls_9wgldua1u8yt`
It is undefined behavior to dereference a :t:`raw pointer` that is either
:t:`dangling` or unaligned.

.. rubric:: Examples

:dp:`fls_9ifaterm8nop`
See :p:`fls_350qejoq9i23` for the declaration of ``ref_answer``.

.. code-block:: rust

   let deref_answer = *ref_answer;

.. _fls_pocsh1neugpc:

Error Propagation Expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   ErrorPropagationExpression ::=
       Operand $$?$$

.. rubric:: Legality Rules

.. glossary-entry:: error propagation expression
   :glossary-dp: fls_kz7tgpi8xkt4
   
   :glossary:
     :dp:`fls_5kebgodxtqqt`
     An :dt:`error propagation expression` is an :t:`expression` that either
     evaluates to a :t:`value` of its :t:`operand` or returns a value to the next
     control flow boundary.
     
     :dp:`fls_agyqvyda3rcj`
     See :s:`ErrorPropagationExpression`.
   :chapter:
     :dp:`fls_8q59wbumrt5s`
     An :t:`error propagation expression` is an :t:`expression` that either evaluates
     to a :t:`value` of its :t:`operand` or returns a value to the enclosing control
     flow boundary.

:dp:`fls_mq2h4seoxah`
An :t:`error propagation expression` shall appear within a :t:`control flow
boundary`.

:dp:`fls_ab4vhq4nwn7f`
The :t:`type` of an :t:`error propagation expression` is :t:`associated type`
:std:`core::ops::Try::Output`.

:dp:`fls_z4zikxy2b1em`
The :t:`value` of an :t:`error propagation expression` is determined as follows:

* :dp:`fls_a09614kgsspt`
  If the :t:`evaluation` of the :t:`error propagation expression` executed
  :std:`core::ops::Try::branch`, then the :t:`value` is the :t:`value` of
  the :std:`core::ops::ControlFlow::Continue` variant.

* :dp:`fls_8df018q7y6g`
  Otherwise control flow is returned to the end of the enclosing :t:`control
  flow boundary`.

.. rubric:: Dynamic Semantics

:dp:`fls_alk4qvfprnvy`
The :t:`evaluation` of an :t:`error propagation expression` of the form

.. code-block:: rust

   expression?

:dp:`fls_1nnhjcgy8kdh`
is equivalent to the :t:`evaluation` the following :t:`expression`:

.. code-block:: rust

   match core::ops::Try::branch(expression) {
       core::ops::ControlFlow::Continue(value) =>
           value,

       core::ops::ControlFlow::Break(value) =>
           core::ops::FromResidual::from_residual(value),
   }

.. rubric:: Examples

.. code-block:: rust

   fn try_to_parse() -> Result<i32, ParseIntError> {
       "42".parse()?
   }

   fn try_some() -> Option<i32> {
       let val = Some(42)?;
       Some(val)
   }

.. _fls_wrecura8u5ar:

Negation Expression
~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   NegationExpression ::=
       NegationOperator Operand

   NegationOperator ::=
       BitwiseNegationOperator
     | SignNegationOperator

   BitwiseNegationOperator ::=
       $$!$$

   SignNegationOperator ::=
       $$-$$

.. rubric:: Legality Rules

.. glossary-entry:: negation expression
   :glossary-dp: fls_3sp4twvfvb32
   
   :glossary:
     :dp:`fls_pmn6cjamdt0a`
     A :dt:`negation expression` is an :t:`expression` that negates its :t:`operand`.
     
     :dp:`fls_o1f35ud4klvv`
     See :s:`NegationExpression`.
   :chapter:
     :dp:`fls_pfa81kv2mru8`
     A :t:`negation expression` is an :t:`expression` that negates its :t:`operand`.

:dp:`fls_plcut8vzdwox`
The :t:`type` of the :t:`operand` of a :t:`negation expression` with a
:s:`BitwiseNegationOperator` shall implement the :std:`core::ops::Not`
:t:`trait`.

:dp:`fls_ohu0kljfexd3`
The :t:`type` of a :t:`negation expression` with a :s:`BitwiseNegationOperator`
is :t:`associated type` :std:`core::ops::Not::Output`.

:dp:`fls_ghqvj8q71o97`
The :t:`value` of a :t:`negation expression` with a :s:`BitwiseNegationOperator`
is the result of ``core::ops::Not::not(operand)``.

:dp:`fls_3m4mgqnzqhri`
The :t:`type` of the :t:`operand` of a :t:`negation expression` with a
:s:`SignNegationOperator` shall implement the :std:`core::ops::Neg` :t:`trait`.

:dp:`fls_u7gzm6n75rzm`
The :t:`type` of a :t:`negation expression` with a :s:`SignNegationOperator`
shall be :t:`associated type` :std:`core::ops::Neg::Output`.

:dp:`fls_9rmq7iaf092d`
The :t:`value` of a :t:`negation expression` with a :s:`SignNegationOperator` is
the result of ``core::ops::Neg::neg(operand)``.

.. rubric:: Dynamic Semantics

:dp:`fls_yzt6pcsvj3a`
The :t:`evaluation` of a :t:`negation expression` with a
:s:`BitwiseNegationOperator` proceeds as follows:

#. :dp:`fls_8tgxtprtifrr`
   The :t:`operand` is evaluated.

#. :dp:`fls_rFFlt33a5RsZ`
   If the type of the :t:`operand` is an :t:`integer type`, then the
   :t:`negation expression` evaluates to the bitwise negation of the
   :t:`operand`.

#. :dp:`fls_h7pIl1WZ8Y2t`
   If the type of the :t:`operand` is :c:`bool`, then the result is computed as
   follows, depending on the :t:`value` of the :t:`operand`:

  .. list-table::

    * - :dp:`fls_yfK3pGHzUo3x`
      - **Operand**
      - **Result**
    * - :dp:`fls_dcNtgLq2hRZb`
      - ``true``
      - ``false``
    * - :dp:`fls_sxLwuITs62sN`
      - ``false``
      - ``true``

#. :dp:`fls_gn3dnuxm2h8m`
   If the type of :t:`operand` is neither an :t:`integer type` nor
   :c:`bool`, then ``core::ops::Not::not(operand)`` is invoked.

:dp:`fls_tsou6yz4mfte`
The :t:`evaluation` of a :t:`negation expression` with a
:s:`SignNegationOperator` proceeds as follows:

#. :dp:`fls_zdfgqky85r1f`
   The :t:`operand` is evaluated.

#. :dp:`fls_CutpaCFCGHQs`
   If the type of the :t:`operand` is an :t:`integer type`, then the
   :t:`negation expression` evaluates to the :t:`value` of the :t:`operand`,
   with its sign inverted. If the result of the :t:`negation expression` does
   not fit within the range of the :t:`operand` type, then
   :t:`arithmetic overflow` occurs.

#. :dp:`fls_B2eKGWaJhFKD`
   If the type of the :t:`operand` is a :t:`floating-point type`, then the
   :t:`negation expression` evaluates to the :t:`value` of the :t:`operand`,
   with its sign inverted. No :t:`arithmetic overflow` is possible.

#. :dp:`fls_uldh10k77sng`
   If the type of the :t:`operand` is neither an :t:`integer type` nor a
   :t:`floating-point type`, then ``core::ops::Neg::neg(operand)`` is invoked.

.. rubric:: Examples

:dp:`fls_uo6vv2yf8usx`
Sign negation.

.. code-block:: rust

   -42

:dp:`fls_hbrg0d98jak5`
Bitwise negation.

.. code-block:: rust

   !42

:dp:`fls_kqtr9c3jorvg`
Logical negation.

.. code-block:: rust

   !false

.. _fls_1k9mkv7rbezi:

Arithmetic Expressions
~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   ArithmeticExpression ::=
       AdditionExpression
     | DivisionExpression
     | MultiplicationExpression
     | RemainderExpression
     | SubtractionExpression

   AdditionExpression ::=
       LeftOperand $$+$$ RightOperand

   DivisionExpression ::=
       LeftOperand $$/$$ RightOperand

   MultiplicationExpression ::=
       LeftOperand $$*$$ RightOperand

   RemainderExpression ::=
       LeftOperand $$%$$ RightOperand

   SubtractionExpression ::=
       LeftOperand $$-$$ RightOperand

.. rubric:: Legality Rules

.. glossary-entry:: arithmetic operator
   :glossary-dp: fls_kSuc3Gi7cdly
   
   :glossary:
     :dp:`fls_Qf7DckakqvRq`
     An :dt:`arithmetic operator` is the operator of an :t:`arithmetic expression`.

.. glossary-entry:: arithmetic expression
   :glossary-dp: fls_kf81ozijral2
   
   :glossary:
     :dp:`fls_u3z2r1fw89xo`
     An :dt:`arithmetic expression` is an :t:`expression` that computes a :t:`value`
     from two :t:`[operand]s` using arithmetic.
     
     :dp:`fls_in59ccg4g3we`
     See :s:`ArithmeticExpression`.
   :chapter:
     :dp:`fls_asibqpe3z95h`
     An :t:`arithmetic expression` is an :t:`expression` that computes a :t:`value`
     from two :t:`[operand]s` using arithmetic.

.. glossary-entry:: addition expression
   :glossary-dp: fls_mcabdigrqv21
   
   :glossary:
     :dp:`fls_ylfdtuajmi0t`
     An :dt:`addition expression` is an :t:`arithmetic expression` that uses
     addition.
     
     :dp:`fls_5bgx5dyi817x`
     See :s:`AdditionExpression`.
   :chapter:
     :dp:`fls_kr8Opj3c7uvb`
     An :t:`addition expression` is an :t:`arithmetic expression` that uses addition.

:dp:`fls_8imzo7agyx0k`
The :t:`type` of the :t:`left operand` of an :t:`addition expression` shall
implement the :std:`core::ops::Add` :t:`trait` with the :t:`type` of the
:t:`right operand` as the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_vk17mfv47wk9`
The :t:`type` of an :t:`addition expression` is :t:`associated type`
:std:`core::ops::Add::Output`.

:dp:`fls_ryzhdpxgm7ii`
The :t:`value` of an :t:`addition expression` is the result of
``core::ops::Add::add(left_operand, right_operand)``.

.. glossary-entry:: division expression
   :glossary-dp: fls_vxd5q8nekkn0
   
   :glossary:
     :dp:`fls_du05yp205f4y`
     A :dt:`division expression` is an :t:`arithmetic expression` that uses division.
     
     :dp:`fls_d3vwk4autyd`
     See :s:`DivisionExpression`.
   :chapter:
     :dp:`fls_dstca76y08ge`
     A :t:`division expression` is an :t:`arithmetic expression` that uses division.

:dp:`fls_f1puss9t4btz`
The :t:`type` of the :t:`left operand` of a :t:`division expression` shall
implement the :std:`core::ops::Div` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_5rdrkvspw57z`
The :t:`type` of a :t:`division expression` is :t:`associated type`
:std:`core::ops::Div::Output`.

:dp:`fls_thyq4h55mx55`
The :t:`value` of a :t:`division expression` is the result of
``core::ops::Div::div(left_operand, right_operand)``.

.. glossary-entry:: multiplication expression
   :glossary-dp: fls_bgtznqqgtmd8
   
   :glossary:
     :dp:`fls_324qh8wz474b`
     A :dt:`multiplication expression` is an :t:`arithmetic expression` that uses
     multiplication.
     
     :dp:`fls_34bkl5i75q5`
     See :s:`MultiplicationExpression`.
   :chapter:
     :dp:`fls_kf41bphvlse3`
     A :t:`multiplication expression` is an :t:`arithmetic expression` that uses
     multiplication.

:dp:`fls_hrml95g2txcj`
The :t:`type` of the :t:`left operand` of a :t:`multiplication expression`
shall implement the :std:`core::ops::Mul` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_ittf4yggk7do`
The :t:`type` of a :t:`multiplication expression` is :t:`associated type`
:std:`core::ops::Mul::Output`.

:dp:`fls_ylqm6wucq2sw`
The :t:`value` of a :t:`multiplication expression` is the result of
``core::ops::Mul::mul(left_operand, right_operand)``.

.. glossary-entry:: remainder expression
   :glossary-dp: fls_f15h4919ln3k
   
   :glossary:
     :dp:`fls_l6muwnclm1do`
     A :dt:`remainder expression` is an :t:`arithmetic expression` that uses
     remainder division.
     
     :dp:`fls_h98qlby2uiru`
     See :s:`RemainderExpression`.
   :chapter:
     :dp:`fls_3de9ulyzuoa`
     A :t:`remainder expression` is an :t:`arithmetic expression` that uses remainder
     division.

:dp:`fls_8fbhreyynhid`
The :t:`type` of the :t:`left operand` of a :t:`remainder expression` shall
implement the :std:`core::ops::Rem` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_u3jwnrqun5kl`
The :t:`type` of a :t:`remainder expression` is :t:`associated type`
:std:`core::ops::Rem::Output`.

:dp:`fls_2ude3wrxji2p`
The :t:`value` of a :t:`remainder expression` is the result of
``core::ops::Rem::rem(left_operand, right_operand)``.

.. glossary-entry:: subtraction expression
   :glossary-dp: fls_25ru96mfdcsn
   
   :glossary:
     :dp:`fls_caamjgpw59id`
     A :dt:`subtraction expression` is an :t:`arithmetic expression` that uses
     subtraction.
     
     :dp:`fls_mx3olnbntpye`
     See :s:`SubtractionExpression`.
   :chapter:
     :dp:`fls_aalxhbvu8kdi`
     A :t:`subtraction expression` is an :t:`arithmetic expression` that uses
     subtraction.

:dp:`fls_fjcv1nm8tlgf`
The :t:`type` of the :t:`left operand` of a :t:`subtraction expression` shall
implement the :std:`core::ops::Sub` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_9x2i1zlsm364`
The :t:`type` of a :t:`subtraction expression` is :t:`associated type`
:std:`core::ops::Sub::Output`.

:dp:`fls_v8vekngd27sz`
The :t:`value` of a :t:`subtraction expression` is the result of
``core::ops::Sub::sub(left_operand, right_operand)``.

.. rubric:: Dynamic Semantics

:dp:`fls_5nsa9zefz9cv`
The :t:`evaluation` of an :t:`addition expression` proceeds as follows:

#. :dp:`fls_u3pstd6xe43y`
   The :t:`left operand` is evaluated.

#. :dp:`fls_jjmc1xgny77`
   The :t:`right operand` is evaluated.

#. :dp:`fls_NcLf4o1dpniS`
   If the :t:`type` of both :t:`[operand]s` is the same :t:`integer type` or
   :t:`floating-point type`, then the :t:`addition expression` evaluates to the
   sum of the :t:`[operand]s`, following the rules of unsigned integer addition
   for :t:`[unsigned integer type]s`, two's complement addition for
   :t:`[signed integer type]s`, or floating-point addition for
   :t:`[floating-point type]s`. If unsigned integer addition or two's
   complement addition is performed, then the operation may result in an
   :t:`arithmetic overflow`.

#. :dp:`fls_cayhj5hcuhcg`
   Otherwise, ``core::ops::Add::add(left_operand, right_operand)`` is invoked.

:dp:`fls_43knkymqpj7t`
The :t:`evaluation` of a :t:`division expression` proceeds as follows:

#. :dp:`fls_62gpbubfj30w`
   The :t:`left operand` is evaluated.

#. :dp:`fls_bveocgaagk1n`
   The :t:`right operand` is evaluated.

#. :dp:`fls_zLroZh43MOtN`
   If the :t:`type` of both :t:`[operand]s` is the same :t:`integer type` or
   :t:`floating-point type`, then the :t:`division expression` evaluates to the
   quotient of the :t:`[operand]s`, following the rules of unsigned integer
   division for :t:`[unsigned integer type]s`, two's complement division for
   :t:`[signed integer type]s`, or floating-point division for
   :t:`[floating-point type]s`.

   #. :dp:`fls_Q9dhNiICGIfr`
      If unsigned integer division is performed and the :t:`right operand` is
      0, then the operation results in a :t:`panic`.

   #. :dp:`fls_albbLSTYtmyq`
      If two's complement division is performed and the :t:`right operand` is 0
      or the result does not fit in the target type, then the operation results
      in a :t:`panic`.

#. :dp:`fls_qd6ggdgq2hob`
   Otherwise, ``core::ops::Div::div(left_operand, right_operand)`` is invoked.

:dp:`fls_lr2a21v5en59`
The :t:`evaluation` of a :t:`multiplication expression` proceeds as follows:

#. :dp:`fls_kpbxcdaflb06`
   The :t:`left operand` is evaluated.

#. :dp:`fls_b94ojbfukhvd`
   The :t:`right operand` is evaluated.

#. :dp:`fls_Et5gp1I7VqBX`
   If the :t:`type` of both :t:`[operand]s` is the same :t:`integer type` or
   :t:`floating-point type`, then the :t:`multiplication expression` evaluates
   to the product of the :t:`[operand]s`, following the rules of unsigned
   integer multiplication for :t:`[unsigned integer type]s`, two's complement
   multiplication for :t:`[signed integer type]s`, or floating-point
   multiplication for :t:`[floating-point type]s`. If unsigned integer
   multiplication or two's complement multiplication is performed, then the
   operation may result in an :t:`arithmetic overflow`.

#. :dp:`fls_blyr18iao20n`
   Otherwise, ``core::ops::Mul::mul(left_operand, right_operand)`` is invoked.

:dp:`fls_g28igfbnwfe0`
The :t:`evaluation` of a :t:`remainder expression` proceeds as follows:

#. :dp:`fls_thcumw8n8xbw`
   The :t:`left operand` is evaluated.

#. :dp:`fls_gld1u9fnsj6d`
   The :t:`right operand` is evaluated.

#. :dp:`fls_Kdr6fLrRj0Du`
   If the :t:`type` of both :t:`[operand]s` is the same :t:`integer type` or
   :t:`floating-point type`, then the :t:`remainder expression` evaluates to
   the remainder of the division of the :t:`left operand` by the
   :t:`right operand`, following the rules of unsigned integer division for
   :t:`[unsigned integer type]s`, two's complement division for
   :t:`[signed integer type]s`, or floating-point division for
   :t:`[floating-point type]s`.

   #. :dp:`fls_FxLnXeGT2n9u`
      If unsigned integer division is performed and the :t:`right operand` is
      0, then the operation results in a :t:`panic`.

   #. :dp:`fls_kN0HnldvDXSg`
      If two's complement division is performed and the :t:`right operand` is 0
      or the resulting remainder does not fit in the target type, then the
      operation results in a :t:`panic`.

#. :dp:`fls_k7lmxvpkxtub`
   Otherwise, ``core::ops::Rem::rem(left_operand, right_operand)`` is invoked.

:dp:`fls_bndpd66973ev`
The :t:`evaluation` of a :t:`subtraction expression` proceeds as follows:

#. :dp:`fls_izmfimd4yg27`
   The :t:`left operand` is evaluated.

#. :dp:`fls_ad9tc6ki8vcq`
   The :t:`right operand` is evaluated.

#. :dp:`fls_Vy0DyZqfy7Iv`
   If the :t:`type` of both :t:`[operand]s` is the same :t:`integer type` or
   :t:`floating-point type`, then the :t:`subtraction expression` evaluates to
   the difference of the :t:`[operand]s`, following the rules of unsigned
   integer subtraction for :t:`[unsigned integer type]s`, two's complement
   subtraction for :t:`[signed integer type]s`, or floating-point subtraction
   for :t:`[floating-point type]s`. If unsigned integer subtraction or two's
   complement subtraction is performed, then the operation may result in an
   :t:`arithmetic overflow`.

#. :dp:`fls_b9g0r9vc4rou`
   Otherwise, ``core::ops::Sub::sub(left_operand, right_operand)`` is invoked.

.. rubric:: Examples

.. code-block:: rust

   1 + 2
   4.0 / 3.29
   8.4 * 5.3
   10 % 4
   3 - 2

.. _fls_abp6tjbz8tpn:

Bit Expressions
~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   BitExpression ::=
       BitAndExpression
     | BitOrExpression
     | BitXOrExpression
     | ShiftLeftExpression
     | ShiftRightExpression

   BitAndExpression ::=
       LeftOperand $$&$$ RightOperand

   BitOrExpression ::=
       LeftOperand $$|$$ RightOperand

   BitXorExpression ::=
       LeftOperand $$^$$ RightOperand

   ShiftLeftExpression ::=
       LeftOperand $$<<$$ RightOperand

   ShiftRightExpression ::=
       LeftOperand $$>>$$ RightOperand

.. rubric:: Legality Rules

.. glossary-entry:: bit expression
   :glossary-dp: fls_ed6yltkt0gb1
   
   :glossary:
     :dp:`fls_b3p5xqsfolqo`
     A :dt:`bit expression` is an :t:`expression` that computes a :t:`value` from
     two :t:`[operand]s` using bit arithmetic.
     
     :dp:`fls_iw1k2cfwfjou`
     See :s:`BitExpression`.
   :chapter:
     :dp:`fls_3zd59yuywz6l`
     A :t:`bit expression` is an :t:`expression` that computes a :t:`value` from two
     :t:`[operand]s` using bit arithmetic.

.. glossary-entry:: bit and expression
   :glossary-dp: fls_h6sh4im3gjys
   
   :glossary:
     :dp:`fls_c1g5gljnr9kz`
     A :dt:`bit and expression` is a :t:`bit expression` that uses bit and
     arithmetic.
     
     :dp:`fls_vbsvu0troqci`
     See :s:`BitAndExpression`.
   :chapter:
     :dp:`fls_f6mmva3lbj1i`
     A :t:`bit and expression` is a :t:`bit expression` that uses bit and arithmetic.

:dp:`fls_cmowpfrcelke`
The :t:`type` of the :t:`left operand` of a :t:`bit and expression` shall
implement the :std:`core::ops::BitAnd` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_kchprk9z6xun`
The :t:`type` of a :t:`bit and expression` is :t:`associated type`
:std:`core::ops::BitAnd::Output`.

:dp:`fls_dimu987fw4kg`
The :t:`value` of a :t:`bit and expression` is the result of
``core::ops::BitAnd::bitand(left_operand, right_operand)``.

.. glossary-entry:: bit or expression
   :glossary-dp: fls_m33m8nd2rnf8
   
   :glossary:
     :dp:`fls_183aem60of9o`
     A :dt:`bit or expression` is a :t:`bit expression` that uses bit or arithmetic.
     
     :dp:`fls_ctqsjp653tbt`
     See :s:`BitOrExpression`.
   :chapter:
     :dp:`fls_3136k1y6x3cu`
     A :t:`bit or expression` is a :t:`bit expression` that uses bit or arithmetic.

:dp:`fls_oo2ynd8e1ys6`
The :t:`type` of the :t:`left operand` of a :t:`bit or expression` shall
implement the :std:`core::ops::BitOr` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_s6hkt5fg598y`
The :t:`type` of a :t:`bit or expression` is :t:`associated type`
:std:`core::ops::BitOr::Output`.

:dp:`fls_osfse0t6ua8a`
The :t:`value` of a :t:`bit or expression` is the result of
``core::ops::BitOr::bitor(left_operand, right_operand)``.

.. glossary-entry:: bit xor expression
   :glossary-dp: fls_ixw1601j8u39
   
   :glossary:
     :dp:`fls_kccsvtzfhbp1`
     A :dt:`bit xor expression` is a :t:`bit expression` that uses bit exclusive or
     arithmetic.
     
     :dp:`fls_6qulwlo43w6m`
     See :s:`BitXorExpression`.
   :chapter:
     :dp:`fls_j7ujcuthga1i`
     A :t:`bit xor expression` is a :t:`bit expression` that uses bit exclusive or
     arithmetic.

:dp:`fls_fnywefl9nty2`
The :t:`type` of the :t:`left operand` of a :t:`bit xor expression` shall
implement the :std:`core::ops::BitXor` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_4f24nyx0ix0j`
The :t:`type` of a :t:`bit xor expression` is :t:`associated type`
:std:`core::ops::BitXor::Output`.

:dp:`fls_8tb22c6zbp3`
The :t:`value` of a :t:`bit xor expression` is the result of
``core::ops::BitXor::bitxor(left_operand, right_operand)``.

.. glossary-entry:: shift left expression
   :glossary-dp: fls_sru4wi5jomoe
   
   :glossary:
     :dp:`fls_phiv6k4emauc`
     A :dt:`shift left expression` is a :t:`bit expression` that uses bit shift left
     arithmetic.
     
     :dp:`fls_56lu9kenzig9`
     See :s:`ShiftLeftExpression`.
   :chapter:
     :dp:`fls_caxn774ij8lk`
     A :t:`shift left expression` is a :t:`bit expression` that uses bit shift left
     arithmetic.

:dp:`fls_1f4pc612f2a8`
The :t:`type` of the :t:`left operand` of a :t:`shift left expression` shall
implement the :std:`core::ops::Shl` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_8trozue35xe4`
The :t:`type` of a :t:`shift left expression` is :t:`associated type`
:std:`core::ops::Shl::Output`.

:dp:`fls_kqntxbwnc58v`
The :t:`value` of a :t:`shift left expression` is the result of
``core::ops::Shl::shl(left_operand, right_operand)``.

.. glossary-entry:: shift right expression
   :glossary-dp: fls_dj6epbraptqn
   
   :glossary:
     :dp:`fls_j6itily0u0k9`
     A :dt:`shift right expression` is a :t:`bit expression` that uses bit shift
     right arithmetic.
     
     :dp:`fls_ex1mopil8w1p`
     See :s:`ShiftRightExpression`.
   :chapter:
     :dp:`fls_t709sl4co3al`
     A :t:`shift right expression` is a :t:`bit expression` that uses bit shift right
     arithmetic.

:dp:`fls_onutb0b9p9zj`
The :t:`type` of the :t:`left operand` of a :t:`shift right expression` shall
implement the :std:`core::ops::Shr` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_yq8rtwfp3nv0`
The :t:`type` of a :t:`shift right expression` is :t:`associated type`
:std:`core::ops::Shr::Output`.

:dp:`fls_fbazfgd5m1ot`
The :t:`value` of a :t:`shift right expression` is the result of
``core::ops::Shr::shr(left_operand, right_operand)``.

.. rubric:: Dynamic Semantics

:dp:`fls_f4o8xlu67okn`
The :t:`evaluation` of a :t:`bit and expression` proceeds as follows:

#. :dp:`fls_kp747xqekyrr`
   The :t:`left operand` is evaluated.

#. :dp:`fls_m0pdk78dah6n`
   The :t:`right operand` is evaluated.

#. :dp:`fls_m2hsk41hwm2j`
   ``core::ops::BitAnd::bitand(left_operand, right_operand)`` is invoked.

:dp:`fls_p9rlmjhbnbao`
The :t:`evaluation` of a :t:`bit or expression` proceeds as follows:

#. :dp:`fls_vprp53kv64q6`
   The :t:`left operand` is evaluated.

#. :dp:`fls_d456ummq6vrk`
   The :t:`right operand` is evaluated.

#. :dp:`fls_n269ufyesndz`
   ``core::ops::BitOr::bitor(left_operand, right_operand)`` is invoked.

:dp:`fls_i9iqtobheivu`
The :t:`evaluation` of a :t:`bit xor expression` proceeds as follows:

#. :dp:`fls_htw2tpujktwt`
   The :t:`left operand` is evaluated.

#. :dp:`fls_gf9tyu1idpjk`
   The :t:`right operand` is evaluated.

#. :dp:`fls_u5irwqswbsvu`
   ``core::ops::BitXor::bitxor(left_operand, right_operand)`` is invoked.

:dp:`fls_2kkpr955i4lm`
The :t:`evaluation` of a :t:`shift left expression` proceeds as follows:

#. :dp:`fls_7p64lgnjxylz`
   The :t:`left operand` is evaluated.

#. :dp:`fls_ieh1itrkcnf6`
   The :t:`right operand` is evaluated.

#. :dp:`fls_f0p70y92k14f`
   If the types of both :t:`[operand]s` are :t:`[integer type]s`, then the
   :t:`shift left expression` evaluates to the value of the left :t:`operand`
   whose bits are shifted left by the number of positions the right :t:`operand`
   evaluates to. Vacated bits are filled with zeros. ``lhs << rhs`` evaluates
   to :math:`\mathrm{lhs} \times 2 ^ \mathrm{rhs}`, casted to the type of the left
   :t:`operand`. If the value of the right :t:`operand` is negative or greater
   than or equal to the width of the left operand, then the operation results in
   an :t:`arithmetic overflow`.

#. :dp:`fls_8QGbl2SBU3R0`
   Otherwise, ``core::ops::Shl::shl(left_operand, right_operand)`` is invoked.

:dp:`fls_303r0u6ug215`
The :t:`evaluation` of a :t:`shift right expression` proceeds as follows:

#. :dp:`fls_4gxj18t6cnzq`
   The :t:`left operand` is evaluated.

#. :dp:`fls_gurl2ve58drz`
   The :t:`right operand` is evaluated.

#. :dp:`fls_r02OGonXp93A`
   If the types of both :t:`[operand]s` are :t:`[integer type]s`, then the
   :t:`shift right expression` evaluates to the value of the left :t:`operand`
   whose bits are shifted right by the number of positions the right
   :t:`operand` evaluates to. If the type of the left :t:`operand` is any
   :t:`signed integer type` and is negative, then vacated bits are filled
   with ones. Otherwise, vacated bits are filled with zeros. ``lhs >> rhs``
   evaluates to :math:`\mathrm{lhs} / 2^ \mathrm{rhs}`, casted to the type of
   the left :t:`operand`. If the value of the right :t:`operand` is negative,
   greater than or equal to the width of the left operand, then the operation
   results in an :t:`arithmetic overflow`.

#. :dp:`fls_xkyj83mcb9d5`
   Otherwise, ``core::ops::Shr::shr(left_operand, right_operand)`` is invoked.

.. rubric:: Examples

.. code-block:: rust

   0b1010 & 0b1100
   0b1010 | 0b0011
   0b1010 ^ 0b1001
   13 << 3
   -10 >> 2

.. _fls_nsvzzbldhq53:

Comparison Expressions
~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   ComparisonExpression ::=
       EqualsExpression
     | GreaterThanExpression
     | GreaterThanOrEqualsExpression
     | LessThanExpression
     | LessThanOrEqualsExpression
     | NotEqualsExpression

   EqualsExpression ::=
       LeftOperand $$==$$ RightOperand

   GreaterThanExpression ::=
       LeftOperand $$>$$ RightOperand

   GreaterThanOrEqualsExpression ::=
       LeftOperand $$>=$$ RightOperand

   LessThanExpression ::=
       LeftOperand $$<$$ RightOperand

   LessThanOrEqualsExpression ::=
       LeftOperand $$<=$$ RightOperand

   NotEqualsExpression ::=
       LeftOperand $$!=$$ RightOperand

.. rubric:: Legality Rules

.. glossary-entry:: comparison expression
   :glossary-dp: fls_hjxuoe1hwlhm
   
   :glossary:
     :dp:`fls_394p7gdruvk7`
     A :dt:`comparison expression` is an :t:`expression` that compares the
     :t:`[value]s` of two :t:`[operand]s`.
     
     :dp:`fls_1jk0s7389mt0`
     See :s:`ComparisonExpression`.
   :chapter:
     :dp:`fls_yzuceqx6nxwa`
     A :t:`comparison expression` is an :t:`expression` that compares the
     :t:`[value]s` of two :t:`[operand]s`.

:dp:`fls_asfrqemqviad`
A :t:`comparison expression` implicitly takes :t:`[shared borrow]s` of its
:t:`[operand]s`.

:dp:`fls_9s4re3ujnfis`
The :t:`type` of a :t:`comparison expression` is :t:`type` :c:`bool`.

.. glossary-entry:: equals expression
   :glossary-dp: fls_alifv570nx7q
   
   :glossary:
     :dp:`fls_mn1g2hijtd6f`
     An :dt:`equals expression` is a :t:`comparison expression` that tests equality.
     
     :dp:`fls_j32l4do0xw4d`
     See :s:`EqualsExpression`.
   :chapter:
     :dp:`fls_ruyho6cu7rxg`
     An :t:`equals expression` is a :t:`comparison expression` that tests equality.

:dp:`fls_8echqk9po1cf`
The :t:`type` of the :t:`left operand` of an :t:`equals expression` shall
implement the :std:`core::cmp::PartialEq` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_d62qfloqk2ub`
The :t:`value` of an :t:`equals expression` is the result of
``core::cmp::PartialEq::eq(&left_operand, &right_operand)``.

.. glossary-entry:: greater-than expression
   :glossary-dp: fls_g4n20dy3utzy
   
   :glossary:
     :dp:`fls_j7x5qii6rhwj`
     A :dt:`greater-than expression` is a :t:`comparison expression` that tests for
     a greater-than relationship.
     
     :dp:`fls_yni50ba3ufvs`
     See :s:`GreaterThanExpression`.
   :chapter:
     :dp:`fls_wapl0ir7uvbp`
     A :t:`greater-than expression` is a :t:`comparison expression` that tests for a
     greater-than relationship.

:dp:`fls_x2s6ydvj5zyd`
The :t:`type` of the :t:`left operand` of a :t:`greater-than expression` shall
implement the :std:`core::cmp::PartialOrd` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_pso38dowbk91`
The :t:`value` of a :t:`greater-than expression` is the result of
``core::cmp::PartialOrd::gt(&left_operand, &right_operand)``.

.. glossary-entry:: greater-than-or-equals expression
   :glossary-dp: fls_mxz589rq4hiy
   
   :glossary:
     :dp:`fls_wvspqc2otn6v`
     A :dt:`greater-than-or-equals expression` is a :t:`comparison expression` that
     tests for a greater-than-or-equals relationship.
     
     :dp:`fls_9azbvj9xux6y`
     See :s:`GreaterThanOrEqualsExpression`.
   :chapter:
     :dp:`fls_7n5gol6a8lod`
     A :t:`greater-than-or-equals expression` is a :t:`comparison expression` that
     tests for a greater-than-or-equals relationship.

:dp:`fls_hholzcbp5u3n`
The :t:`type` of the :t:`left operand` of a
:t:`greater-than-or-equals expression` shall implement the
:std:`core::cmp::PartialOrd` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_wytygse41vzm`
The :t:`value` of a :t:`greater-than-or-equals expression` is the result of
``core::cmp::PartialOrd::ge(&left_operand, &right_operand)``.

.. glossary-entry:: less-than expression
   :glossary-dp: fls_ulmspewtlo57
   
   :glossary:
     :dp:`fls_9ttxqxt9ui4t`
     A :dt:`less-than expression` is a :t:`comparison expression` that tests for a
     less-than relationship.
     
     :dp:`fls_rhnbdyo2l4kp`
     See :s:`LessThanExpression`.
   :chapter:
     :dp:`fls_yd4qqi39w248`
     A :t:`less-than expression` is a :t:`comparison expression` that tests for a
     less-than relationship.

:dp:`fls_ynibdcke3etb`
The :t:`type` of the :t:`left operand` of a :t:`less-than expression` shall
implement the :std:`core::cmp::PartialOrd` :t:`trait` where the :t:`type` of
the :t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_xmtxkit3qpw7`
The :t:`value` of a :t:`less-than expression` is the result of
``core::cmp::PartialOrd::lt(&left_operand, &right_operand)``.

.. glossary-entry:: less-than-or-equals expression
   :glossary-dp: fls_es169x7ars9a
   
   :glossary:
     :dp:`fls_8pya58ug180j`
     A :dt:`less-than-or-equals expression` is a :t:`comparison expression` that
     tests for a less-than-or-equals relationship.
     
     :dp:`fls_ft5aeo4ilgwc`
     See :s:`LessThanOrEqualsExpression`.
   :chapter:
     :dp:`fls_yxwe1o27u6ns`
     A :t:`less-than-or-equals expression` is a :t:`comparison expression` that tests
     for a less-than-or-equals relationship.

:dp:`fls_6dgfieyxdan0`
The :t:`type` of the :t:`left operand` of a :t:`less-than-or-equals expression`
shall implement the :std:`core::cmp::PartialOrd` :t:`trait` where the :t:`type`
of the :t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_7pfsqby2saag`
The :t:`value` of a :t:`less-than-or-equals expression` is the result of
``core::cmp::PartialOrd::le(&left_operand, &right_operand)``.

.. glossary-entry:: not-equals expression
   :glossary-dp: fls_shgatqvpdqkg
   
   :glossary:
     :dp:`fls_2hmynl94uusk`
     A :dt:`not-equals expression` is a :t:`comparison expression` that tests for
     inequality.
     
     :dp:`fls_5d6vvr9m35n2`
     See :s:`NotEqualsExpression`.
   :chapter:
     :dp:`fls_w71j7i3n1kit`
     A :t:`not-equals expression` is a :t:`comparison expression` that tests for
     inequality.

:dp:`fls_qzo1torhv5i3`
The :t:`type` of the :t:`left operand` of a :t:`not-equals expression` shall
implement the :std:`core::cmp::PartialEq` :t:`trait` where the :t:`type` of the
:t:`right operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_kodwkh58hmdv`
The :t:`value` of a :t:`not-equals expression` is the result of
``core::cmp::PartialEq::ne(&left_operand, &right_operand)``.

.. rubric:: Dynamic Semantics

:dp:`fls_ydt9zvh0h5ex`
The :t:`evaluation` of an :t:`equals expression` proceeds as follows:

#. :dp:`fls_4vbrc31r0o60`
   The :t:`left operand` is evaluated.

#. :dp:`fls_hyy974ksbbrq`
   The :t:`right operand` is evaluated.

#. :dp:`fls_htrjqxiv3avh`
   ``core::cmp::PartialEq::eq(&left_operand, &right_operand)`` is invoked.

:dp:`fls_1udbc4aom6ok`
The :t:`evaluation` of a :t:`greater-than expression` proceeds as follows:

#. :dp:`fls_96mt7gx5ogo0`
   The :t:`left operand` is evaluated.

#. :dp:`fls_or0i2cqxwl8o`
   The :t:`right operand` is evaluated.

#. :dp:`fls_udnhkbxpk83m`
   ``core::cmp::PartialOrd::gt(&left_operand, &right_operand)`` is invoked.

:dp:`fls_mab6yirx77zl`
The :t:`evaluation` of a :t:`greater-than-or-equals expression` proceeds as
follows:

#. :dp:`fls_2ggb7a7nhrk9`
   The :t:`left operand` is evaluated.

#. :dp:`fls_ukm97arfzsk1`
   The :t:`right operand` is evaluated.

#. :dp:`fls_wrftg7onlkmm`
   ``core::cmp::PartialOrd::ge(&left_operand, &right_operand)`` is invoked.

:dp:`fls_irlqykpbtvd`
The :t:`evaluation` of a :t:`less-than expression` proceeds as follows:

#. :dp:`fls_udonl4c7f6pz`
   The :t:`left operand` is evaluated.

#. :dp:`fls_ebvyhqbb921g`
   The :t:`right operand` is evaluated.

#. :dp:`fls_rfomib80bnn2`
   ``core::cmp::PartialOrd::lt(&left_operand, &right_operand)`` is invoked.

:dp:`fls_6cb4wg59wmef`
The :t:`evaluation` of a :t:`less-than-or-equals expression` proceeds as
follows:

#. :dp:`fls_dkbjn7noq8n2`
   The :t:`left operand` is evaluated.

#. :dp:`fls_kezynx2xc1q7`
   The :t:`right operand` is evaluated.

#. :dp:`fls_8luq5sellcaq`
   ``core::cmp::PartialOrd::le(&left_operand, &right_operand)`` is invoked.

:dp:`fls_c93pacid548a`
The :t:`evaluation` of a :t:`not-equals expression` proceeds as follows:

#. :dp:`fls_gqy6uuowij9e`
   The :t:`left operand` is evaluated.

#. :dp:`fls_s6sq6p8th5nt`
   The :t:`right operand` is evaluated.

#. :dp:`fls_kdga59xx4nx3`
   ``core::cmp::PartialEq::ne(&left_operand, &right_operand)`` is invoked.

.. rubric:: Examples

.. code-block:: rust

   12 == 12
   42 > 12
   42 >= 35
   42 < 109
   42 <= 42
   12 != 42

.. _fls_lstusiu2c8lu:

Lazy Boolean Expressions
~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   LazyBooleanExpression ::=
       LazyAndExpression
     | LazyOrExpression

   LazyAndExpression ::=
       LeftOperand $$&&$$ RightOperand

   LazyOrExpression ::=
       LeftOperand $$||$$ RightOperand

.. rubric:: Legality Rules

.. glossary-entry:: lazy boolean expression
   :glossary-dp: fls_4a6yhxj783a1
   
   :glossary:
     :dp:`fls_jpv7l86sdh6i`
     A :dt:`lazy boolean expression` is an :t:`expression` that performs short
     circuit Boolean arithmetic.
     
     :dp:`fls_9tu5x810ztbg`
     See :s:`LazyBooleanExpression`.
   :chapter:
     :dp:`fls_gpbvus89iy4c`
     A :t:`lazy boolean expression` is an :t:`expression` that performs short circuit
     Boolean arithmetic.

.. glossary-entry:: lazy and expression
   :glossary-dp: fls_bputdgkeezfs
   
   :glossary:
     :dp:`fls_v2e6t73uk6nt`
     A :dt:`lazy and expression` is a :t:`lazy boolean expression` that uses short
     circuit and arithmetic.
     
     :dp:`fls_rkthjuvems6v`
     See :s:`LazyAndExpression`.
   :chapter:
     :dp:`fls_40jya46h62yi`
     A :t:`lazy and expression` is a :t:`lazy boolean expression` that uses short
     circuit and arithmetic.

.. glossary-entry:: lazy or expression
   :glossary-dp: fls_9mvrfhsegwp0
   
   :glossary:
     :dp:`fls_aln8bbvx9kzm`
     A :dt:`lazy or expression` is a :t:`lazy boolean expression` that uses short
     circuit or arithmetic.
     
     :dp:`fls_jiv7e3mr86kf`
     See :s:`LazyOrExpression`.
   :chapter:
     :dp:`fls_k8u77ow5bb6c`
     A :t:`lazy or expression` is a :t:`lazy boolean expression` that uses short
     circuit or arithmetic.

:dp:`fls_u0gwo0s2l0tn`
The :t:`[type]s` of the :t:`[operand]s` of a :t:`lazy boolean expression` shall
be :t:`type` :c:`bool`.

:dp:`fls_zas0lizgq2hn`
The :t:`type` of a :t:`lazy boolean expression` is :t:`type` :c:`bool`.

:dp:`fls_xdgvrd58nkoa`
The :t:`value` of a :t:`lazy boolean expression` is either ``true`` or
``false``.

.. rubric:: Dynamic Semantics

:dp:`fls_ufre0ko2cwh2`
The :t:`evaluation` of a :t:`lazy and expression` proceeds as follows:

#. :dp:`fls_jugckad775kq`
   The :t:`left operand` is evaluated.

#. :dp:`fls_tmfmu3syxp2q`
   If the :t:`left operand` evaluated to ``true``, then the :t:`right operand`
   is evaluated and returned as the :t:`[lazy and expression]'s` :t:`value`.

#. :dp:`fls_srfv1d4idxy9`
   Otherwise the :t:`lazy and expression` evaluates to ``false``.

:dp:`fls_tflikh8cmxvc`
The :t:`evaluation` of a :t:`lazy or expression` proceeds as follows:

#. :dp:`fls_p0rafjsridre`
   The :t:`left operand` is evaluated.

#. :dp:`fls_yg1348rlziw3`
   If the :t:`left operand` evaluated to ``false``, then the :t:`right operand`
   is evaluated and returned as the :t:`[lazy or expression]'s` :t:`value`.

#. :dp:`fls_yffozo2vq5xz`
   Otherwise the :t:`lazy or expression` evaluates to ``true``.

.. rubric:: Examples

.. code-block:: rust

   false && panic!()
   this || that

.. _fls_1qhsun1vyarz:

Type Cast Expressions
~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   TypeCastExpression ::=
       Operand $$as$$ TypeSpecificationWithoutBounds

.. rubric:: Legality Rules

.. glossary-entry:: type cast expression
   :glossary-dp: fls_k24jb967nu1q
   
   :glossary:
     :dp:`fls_j6zo3rir1x76`
     A :dt:`type cast expression` is an :t:`expression` that changes the :t:`type`
     of an :t:`operand`.
     
     :dp:`fls_dvh1xy9w74ch`
     See :s:`TypeCastExpression`.
   :chapter:
     :dp:`fls_ltioqbhl14g0`
     A :t:`type cast expression` is an :t:`expression` that changes the :t:`type` of
     an :t:`operand`.

.. glossary-entry:: cast
   :glossary-dp: fls_pcaygpx7db24
   
   :glossary:
     :dp:`fls_e5hvszhcrtmj`
     :dt:`Cast` or :dt:`casting` is the process of changing the :t:`type` of an
     :t:`expression`.
   :chapter:
     :dp:`fls_99kvyh4puy57`
     :t:`Cast` or :t:`casting` is the process of changing the :t:`type` of an
     :t:`expression`.

:dp:`fls_a6midh2m0w0b`
The ``TypeSpecificationWithoutBounds`` describes the :dt:`target type` of the
:t:`type cast expression`.

:dp:`fls_otaxe9okhdr1`
A :t:`type cast expression` with the following characteristics performs a
:dt:`specialized cast`:

* :dp:`fls_4s69s9pcvbn7`
  An :t:`operand` of a :t:`numeric type` and a target :t:`numeric type` perform
  a :t:`numeric cast`.

* :dp:`fls_le6bchl25ewz`
  An :t:`operand` of an :t:`enum type` and a target :t:`integer type`
  perform :t:`enum cast`. An :dt:`enum cast` converts the :t:`operand` to its
  :t:`discriminant`, followed by a :t:`numeric cast`.

* :dp:`fls_pcromhosmnf0`
  An operand of :t:`type` :c:`bool` or :t:`type` :c:`char` and a
  target :t:`integer type` perform :t:`primitive-to-integer cast`. A
  :dt:`primitive-to-integer cast`

  * :dp:`fls_al9f1t7vlsxi`
    Converts an :t:`operand` of :t:`type` :c:`bool` with :t:`value` ``false``
    to zero.

  * :dp:`fls_jea17f39fmsg`
    Converts an :t:`operand` of :t:`type` :c:`bool` with :t:`value` ``true``
    to one.

  * :dp:`fls_eb00s8fxlvjb`
    Convert an :t:`operand` of :t:`type` :c:`char` to the :t:`value` of the
    corresponding :t:`code point`, followed by a :t:`numeric cast`.

* :dp:`fls_qk5trk8wkvxb`
  An :t:`operand` of :t:`type` :c:`u8` and a target :t:`type` :c:`char` performs
  :t:`u8-to-char cast`. A :dt:`u8-to-char cast` converts an :t:`operand` of
  :t:`type` :c:`u8` to the :t:`value` of the corresponding :t:`code point`.

* :dp:`fls_t16yzaxro5ew`
  An :t:`operand` of :t:`type` ``*const T`` or ``*mut T`` and a
  :t:`target type` ``*const V`` or ``*mut V`` where ``V`` implements the
  :std:`core::marker::Sized` :t:`trait` performs pointer-to-pointer cast.

* :dp:`fls_i4zsbbmfa2fl`
  An :t:`operand` of :t:`type` ``*const T`` or ``*mut T`` where ``T`` implements
  the :std:`core::marker::Sized` :t:`trait` and a target :t:`integer type`
  perform :t:`pointer-to-address cast`. A :dt:`pointer-to-address cast` produces
  an integer that represents the machine address of the referenced memory. If
  the :t:`integer type` is smaller than the :t:`type` of the :t:`operand`, the
  address is truncated.

* :dp:`fls_59mpteeczzo`
  An :t:`operand` of :t:`integer type` and :t:`target type` ``*const V`` or
  ``*mut V`` where ``V`` implements the :std:`core::marker::Sized` :t:`trait`
  perform :t:`address-to-pointer cast`. An :dt:`address-to-pointer cast`
  produces a :t:`pointer` that interprets the integer as a machine address.

* :dp:`fls_8ccwlliqw9jx`
  An :t:`operand` of :t:`type` ``&mut [T; N]`` and a :t:`target type`
  ``*const T`` perform array-to-pointer cast.

* :dp:`fls_i8txki3htx92`
  An :t:`operand` of a :t:`function item type` and a :t:`target type`
  ``*const V`` or ``*mut V`` where ``V`` implements the
  :std:`core::marker::Sized` :t:`trait` perform function-item-to-pointer cast.

* :dp:`fls_6hbkvbb1c8aj`
  An :t:`operand` of a :t:`function item type` and a target :t:`integer type`
  perform function-to-address cast.

* :dp:`fls_133j6xw8k4qe`
  An :t:`operand` of a :t:`function pointer type` and a :t:`target type`
  ``*const V`` or ``*mut V`` where ``V`` implements the
  :std:`core::marker::Sized` :t:`trait` perform
  :dt:`function-pointer-to-pointer cast`.

* :dp:`fls_bhw2j9wjpf2x`
  An :t:`operand` of a :t:`function pointer type` and a target :t:`integer type`
  perform :t:`function-pointer-to-address cast`. A
  :dt:`function-pointer-to-address cast` produces an integer that represents the
  machine address of the referenced :t:`function`. If the :t:`integer type` is
  smaller than the size of the :t:`function pointer type`, the address is
  truncated.

:dp:`fls_3ww5gbk9w4ys`
A :t:`cast` is legal when it either performs :t:`type coercion` or is a
:t:`specialized cast`.

:dp:`fls_hhxawo12cndy`
The :t:`type` of a :t:`type cast expression` is the :t:`target type`.

:dp:`fls_uuayaksl8059`
The :t:`value` of a :t:`type cast expression` is the :t:`value` of the
:t:`operand` after the :t:`cast`.

.. rubric:: Dynamic Semantics

:dp:`fls_syk2li8ft3rx`
The :t:`evaluation` of a :t:`type cast expression` evaluates its :t:`operand`.

:dp:`fls_uqv32nthva6y`
The :t:`evaluation` of a :dt:`numeric cast` proceeds as follows:

* :dp:`fls_kc3gwj9x3jnr`
  Casting an :t:`operand` of an :t:`integer type` to a target :t:`integer type`
  of the same :t:`size` has no effect.

* :dp:`fls_76eq3bd6birr`
  Casting an :t:`operand` of an :t:`integer type` to a target :t:`integer type`
  with smaller :t:`size` truncates the :t:`value` of the :t:`operand`.

* :dp:`fls_ldiritt32h2w`
  Casting an :t:`operand` of an :t:`integer type` to a target :t:`integer type`
  with a larger :t:`size` either

  * :dp:`fls_h9sxg3pxn7i2`
    Zero-extends the :t:`operand` if the :t:`[operand]'s` :t:`type` is
    unsigned, or

  * :dp:`fls_shy6e0e30bco`
    Sign-extends the :t:`operand` if the :t:`[operand]'s` :t:`type` is signed.

* :dp:`fls_4xldaoj5ac6t`
  Casting an :t:`operand` of a :t:`floating-point type` to a target
  :t:`integer type` rounds the :t:`value` of the :t:`operand` towards zero. In
  addition, the :t:`type cast expression`

  * :dp:`fls_50714cvaqkfv`
    Returns zero if the :t:`operand` denotes :std:`f32::NaN` or :std:`f64::NaN`
    respectively.

  * :dp:`fls_g3xbmp8zx1yh`
    Saturates the :t:`value` of the :t:`operand` to the maximum :t:`value`
    of the target :t:`integer type` if the :t:`[operand]'s` :t:`value`
    exceeds the maximum :t:`value` of the target :t:`integer type` or denotes
    :std:`f32::INFINITY` or :std:`f64::INFINITY` respectively.

  * :dp:`fls_hcc5odh52bk7`
    Saturates the :t:`value` of the :t:`operand` to the minimum :t:`value`
    of the target :t:`integer type` if the :t:`[operand]'s` :t:`value`
    exceeds the minimum :t:`value` of the target :t:`integer type` or denotes
    :std:`f32::NEG_INFINITY` or :std:`f64::NEG_INFINITY` respectively.

* :dp:`fls_o2ep4b6t287z`
  Casting an :t:`operand` of an :t:`integer type` to a target
  :t:`floating-point type` produces the closest possible floating-point
  :t:`value`. In addition, the :t:`type cast expression`

  * :dp:`fls_vfofk2aagsj5`
    Rounds the :t:`value` of the :t:`operand` preferring the :t:`value` with an
    even least significant digit if exactly halfway between two floating-point
    numbers.

  * :dp:`fls_cx86k8yfjhht`
    Produces :std:`f32::INFINITY` or :std:`f64::INFINITY` of the same sign as
    the :t:`value` of the :t:`operand` when the :t:`value` of the :t:`operand`
    causes :t:`arithmetic overflow`.

* :dp:`fls_gzmdwibl5s4w`
  Casting an :t:`operand` of :t:`type` :c:`f32` to a :t:`target type` :c:`f64`
  is perfect and lossless.

* :dp:`fls_mjqvjt7v8a25`
  Casting an :t:`operand` of :t:`type` :c:`f64` to :t:`target type` :c:`f32`
  produces the closest possible :c:`f32` :t:`value`. In addition, the
  :t:`type cast expression`

  * :dp:`fls_4fd5vkh0jt4`
    Prefers the nearest :t:`value` with an even least significant digit if
    exactly halfway between two floating-point numbers.

  * :dp:`fls_2etd73f8jg2n`
    Produces :std:`f32::INFINITY` of the same sign as the :t:`value` of the
    :t:`operand` when the :t:`value` of the :t:`operand` causes
    :t:`arithmetic overflow`.

.. rubric:: Examples

:dp:`fls_vdxkpvmpwl3s`
See :p:`fls_2jd0mgw4zja4` for the declaration of ``answer``.

.. code-block:: rust

   answer as f64

.. _fls_y4by2i8dl05o:

Assignment Expressions
~~~~~~~~~~~~~~~~~~~~~~

.. glossary-entry:: assignment
   :glossary-dp: fls_f6ztsofr6xa9
   
   :glossary:
     :dp:`fls_j9pyuucyplmi`
     See :t:`assignment expression`.

.. rubric:: Syntax

.. syntax::

   AssignmentExpression ::=
       AssigneeOperand $$=$$ ValueOperand

   AssigneeOperand ::=
       Operand

   ValueOperand ::=
       Operand

.. rubric:: Legality Rules

.. glossary-entry:: assignment expression
   :glossary-dp: fls_2d2elg5eukv4
   
   :glossary:
     :dp:`fls_6jkc6a6me3zr`
     An :dt:`assignment expression` is an :t:`expression` that assigns the
     :t:`value` of a :t:`value operand` to an :t:`assignee operand`.
     
     :dp:`fls_njw68i3bp9qq`
     See :s:`AssignmentExpression`.
   :chapter:
     :dp:`fls_nhgexeu2h6wi`
     An :t:`assignment expression` is an :t:`expression` that assigns the :t:`value`
     of a :t:`value operand` to an :t:`assignee operand`.

.. glossary-entry:: assignee operand
   :glossary-dp: fls_3hs9hqsthil1
   
   :glossary:
     :dp:`fls_4tgf0wu2mr3l`
     An :dt:`assignee operand` is the target :t:`operand` of an
     :t:`assignment expression`.
     
     :dp:`fls_df0j0vnnq20a`
     See :s:`AssigneeOperand`.
   :chapter:
     :dp:`fls_bsjw6f4a3wol`
     An :t:`assignee operand` is the target :t:`operand` of an
     :t:`assignment expression`.

.. glossary-entry:: value operand
   :glossary-dp: fls_a5xof9jlpc2e
   
   :glossary:
     :dp:`fls_x4seemjknk2z`
     A :dt:`value operand` is an :t:`operand` that supplies the :t:`value` that is
     assigned to an :t:`assignee operand` by an :t:`assignment expression`.
     
     :dp:`fls_cl4fakfkpscp`
     See :s:`ValueOperand`.
   :chapter:
     :dp:`fls_uinh05sslxeo`
     A :t:`value operand` is an :t:`operand` that supplies the :t:`value` that is
     assigned to an :t:`assignee operand` by an :t:`assignment expression`.

:dp:`fls_qengy157fa4a`
The :t:`type` of an :t:`assignment expression` is the :t:`unit type`.

:dp:`fls_bwwtgqprbxrm`
The :t:`value` of an :t:`assignment expression` is the :t:`unit value`.

.. _fls_nnqlae9zp80s:

Basic Assignment
^^^^^^^^^^^^^^^^

.. rubric:: Legality Rules

.. glossary-entry:: basic assignment
   :glossary-dp: fls_bii5eu1wznzk
   
   :glossary:
     :dp:`fls_byq9e2jf8r22`
     A :dt:`basic assignment` is an :t:`assignment expression` that is not a
     :t:`destructuring assignment`.
   :chapter:
     :dp:`fls_uhcodvq75nlr`
     A :t:`basic assignment` is an :t:`assignment expression` that is not a
     :t:`destructuring assignment`.

.. rubric:: Dynamic Semantics

:dp:`fls_esn5ceoldta`
The :t:`evaluation` of a :t:`basic assignment` proceeds as follows:

#. :dp:`fls_t8eqzc64ivin`
   The :t:`value operand` is evaluated.

#. :dp:`fls_b0mqcn5fejhk`
   The :t:`assignee operand` is evaluated.

#. :dp:`fls_9i0ctuo099bp`
   The :t:`value` denoted by the :t:`assignee operand` is :t:`dropped`, unless
   the :t:`assignee operand` denotes an uninitialized :t:`variable` or an
   uninitialized :t:`field` of a :t:`variable`.

#. :dp:`fls_hc01gtvlxba`
   The :t:`value` of the :t:`value operand` is :t:`passed <passing convention>`
   into the :t:`place` of the :t:`assignee operand`.

.. rubric:: Examples

.. code-block:: rust

   this = 42

.. _fls_9beohh5475s2:

Destructuring Assignment
^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Legality Rules

.. glossary-entry:: destructuring assignment
   :glossary-dp: fls_2fuu3zr9rn2q
   
   :glossary:
     :dp:`fls_7jienn9uzn5k`
     A :dt:`destructuring assignment` is an :t:`assignment expression` where
     the :t:`assignee operand` is either an :t:`array expression`, a
     :t:`struct expression`, or a :t:`tuple expression`.
   :chapter:
     :dp:`fls_2eheo4yo2orm`
     A :t:`destructuring assignment` is an :t:`assignment expression` where
     the :t:`assignee operand` is either an :t:`array expression`, a :t:`struct
     expression`, a :t:`tuple expression` or a :t:`tuple struct call expression`.

:dp:`fls_z8c3b9s9de3x`
The :t:`assignee operand` of a :t:`destructuring assignment` is treated as an
:dt:`assignee pattern` depending on its kind, as follows:

* :dp:`fls_vqb89rkkjw81`
  An :t:`array expression` corresponds to a :t:`slice pattern` with all the
  :t:`[subexpression]s` lowered to their corresponding :t:`[pattern]s`.

* :dp:`fls_vqj7ljrrd7wi`
  A :t:`full range expression` corresponds to a :t:`rest pattern` if inside an
  :t:`array expression`, otherwise this is a static error.

* :dp:`fls_du5eybf8mocy`
  A :t:`place expression` corresponds to an :t:`identifier pattern` with a
  unique :t:`identifier` and without :t:`keyword` ``ref``, keyword ``mut``, or
  a :t:`bound pattern`.

* :dp:`fls_hj6srmzbobid`
  A :t:`struct expression` corresponds to a :t:`struct pattern` with all the
  :t:`[subexpression]s` lowered to their corresponding :t:`[pattern]s`.

* :dp:`fls_uydzlfc4hjbx`
  A :t:`tuple expression` corresponds to a :t:`tuple pattern` with all the
  :t:`[subexpression]s` lowered to their corresponding :t:`[pattern]s`.

* :dp:`fls_fa14yfvxsbx3`
  A :t:`tuple struct call expression` corresponds to a
  :t:`tuple struct pattern` with all the :t:`[subexpression]s` lowered to their
  corresponding :t:`[pattern]s`.

* :dp:`fls_q90ikfi7ewoi`
  An :t:`underscore expression` corresponds to an :t:`underscore pattern`.

:dp:`fls_4bb07tn28ivw`
The :t:`pattern` that corresponds to a :t:`destructuring assignment` shall be
an :t:`irrefutable pattern`.

:dp:`fls_g80a92tr2ser`
A :t:`destructuring assignment` is equivalent to a :t:`block expression` of the
following form:

.. glossary-entry:: initialization expression
   :glossary-dp: fls_ctusGvpQvJue
   
   :glossary:
     :dp:`fls_KUeiSByPUc4w`
     An :dt:`initialization expression` is either a :t:`constant initializer` or a
     :t:`static initializer`.

* :dp:`fls_u0iqhbw37xvq`
  The first :t:`statement` is a :t:`let statement` with its :t:`pattern`
  equivalent to the lowered :t:`assignee pattern` and its
  :t:`initialization expression` equivalent to the :t:`value operand`.

* :dp:`fls_wsfhd3udt6fq`
  Then each bound :t:`identifier` of the :t:`assignee pattern` is an
  :t:`assignment expression` used as a :t:`statement`, as follows:

* :dp:`fls_ll6h6qcaos65`
  The bound :t:`identifier` becomes the :t:`value operand` of the new
  :t:`assignment expression`, and

* :dp:`fls_ajbdn54qe6wc`
  The corresponding :t:`expression` from the :t:`assignee operand` of the
  :t:`destructuring assignment` becomes the :t:`assignee operand` of the new
  :t:`assignment expression`.

.. rubric:: Dynamic Semantics

:dp:`fls_l4u5hhw8tnvs`
The :t:`evaluation` of a :t:`destructuring assignment` proceeds as follows:

#. :dp:`fls_dd62w8c9n9sd`
   The :t:`value operand` is evaluated.

#. :dp:`fls_jqu2u6mdccgi`
   The :t:`assignee operand` is evaluated by evaluating its :t:`[operand]s` in
   a left-to-right order.

#. :dp:`fls_n7nuj1lvpspc`
   Each :t:`value` denoted by the :t:`assignee operand` is :t:`dropped`
   in left-to-right order, unless the :t:`assignee operand` denotes an
   uninitialized :t:`variable` or an uninitialized field of a :t:`variable`.

#. :dp:`fls_qb8u5skn8bc4`
   The :t:`value` of the :t:`value operand` is :t:`passed <passing convention>`
   into the :t:`place` of the :t:`assignee operand`.

.. rubric:: Examples

.. code-block:: rust

   (four, two) = (4, 2)

.. _fls_290jmzfh7x4e:

Compound Assignment Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   CompoundAssignmentExpression ::=
       AdditionAssignmentExpression
     | BitAndAssignmentExpression
     | BitOrAssignmentExpression
     | BitXorAssignmentExpression
     | DivisionAssignmentExpression
     | MultiplicationAssignmentExpression
     | RemainderAssignmentExpression
     | ShiftLeftAssignmentExpression
     | ShiftRightAssignmentExpression
     | SubtractionAssignmentExpression

   AdditionAssignmentExpression ::=
       AssignedOperand $$+=$$ ModifyingOperand

   BitAndAssignmentExpression ::=
       AssignedOperand $$&=$$ ModifyingOperand

   BitOrAssignmentExpression ::=
       AssignedOperand $$|=$$ ModifyingOperand

   BitXorAssignmentExpression ::=
       AssignedOperand $$^=$$ ModifyingOperand

   DivisionAssignmentExpression ::=
       AssignedOperand $$/=$$ ModifyingOperand

   MultiplicationAssignmentExpression ::=
       AssignedOperand $$*=$$ ModifyingOperand

   RemainderAssignmentExpression ::=
       AssignedOperand $$%=$$ ModifyingOperand

   ShiftLeftAssignmentExpression ::=
       AssignedOperand $$<<=$$ ModifyingOperand

   ShiftRightAssignmentExpression ::=
       AssignedOperand $$>>=$$ ModifyingOperand

   SubtractionAssignmentExpression ::=
       AssignedOperand $$-=$$ ModifyingOperand

   AssignedOperand ::=
       Operand

   ModifyingOperand ::=
       Operand

.. glossary-entry:: addition assignment
   :glossary-dp: fls_xqZapSv9tM1F
   
   :glossary:
     :dp:`fls_FVgKeCXlmuPe`
     For :dt:`addition assignment`, see :t:`addition assignment expression`.

.. glossary-entry:: addition assignment expression
   :glossary-dp: fls_iw30dqjaeqle
   
   :glossary:
     :dp:`fls_w83tf9m7vu67`
     An :dt:`addition assignment expression` is a
     :t:`compound assignment expression` that uses addition.
     
     :dp:`fls_hihh97p0rnt8`
     See :s:`AdditionAssignmentExpression`.

.. glossary-entry:: bit and assignment
   :glossary-dp: fls_clut5DWMQin8
   
   :glossary:
     :dp:`fls_wIl0K7O6lTXJ`
     For :dt:`bit and assignment`, see :t:`bit and assignment expression`.

.. glossary-entry:: bit or assignment
   :glossary-dp: fls_90E3eiBYgicI
   
   :glossary:
     :dp:`fls_21iFIDCu7Pk4`
     For :dt:`bit or assignment`, see :t:`bit or assignment expression`.

.. glossary-entry:: bit xor assignment
   :glossary-dp: fls_jEnv7RjEUZvm
   
   :glossary:
     :dp:`fls_VJpCPVCuszs1`
     For :dt:`bit xor assignment`, see :t:`bit xor assignment expression`.

.. glossary-entry:: compound assignment
   :glossary-dp: fls_pTMrfPXETibe
   
   :glossary:
     :dp:`fls_lGV9QvCmYGcH`
     For :dt:`compound assignment`, see :t:`compound assignment expression`.

.. rubric:: Legality Rules

.. glossary-entry:: compound assignment expression
   :glossary-dp: fls_iktiir89xbo2
   
   :glossary:
     :dp:`fls_mkxpk2jhe5s0`
     A :dt:`compound assignment expression` is an expression that first computes
     a :t:`value` from two :t:`[operand]s` and then assigns the value to an
     :t:`assigned operand`.
     
     :dp:`fls_55abuw8symub`
     See :s:`CompoundAssignmentExpression`.
   :chapter:
     :dp:`fls_3bu3g8o5nopc`
     A :t:`compound assignment expression` is an expression that first computes
     a :t:`value` from two :t:`[operand]s` and then assigns the value to an
     :t:`assigned operand`.

.. glossary-entry:: bit and assignment expression
   :glossary-dp: fls_y72vyr2tmdyb
   
   :glossary:
     :dp:`fls_dvqotpte0pc2`
     A :dt:`bit and assignment expression` is a :t:`compound assignment expression`
     that uses bit and arithmetic.
     
     :dp:`fls_ix9ecb5olcx`
     See :s:`BitAndAssignmentExpression`.
   :chapter:
     :dp:`fls_w2hbhb989yr4`
     A :t:`bit and assignment expression` is a :t:`compound assignment expression`
     that uses bit and arithmetic.

.. glossary-entry:: bit or assignment expression
   :glossary-dp: fls_ehorb0lul906
   
   :glossary:
     :dp:`fls_tu1owkfk0lu0`
     A :dt:`bit or assignment expression` is a :t:`compound assignment expression`
     that uses bit or arithmetic.
     
     :dp:`fls_utjcsfz8up88`
     See :s:`BitOrAssignmentExpression`.
   :chapter:
     :dp:`fls_ak4g5112jkl`
     A :t:`bit or assignment expression` is a :t:`compound assignment expression`
     that uses bit or arithmetic.

.. glossary-entry:: bit xor assignment expression
   :glossary-dp: fls_u3fcq7jjyxux
   
   :glossary:
     :dp:`fls_ma980ujltab2`
     A :dt:`bit xor assignment expression` is a :t:`compound assignment expression`
     that uses bit exclusive or arithmetic.
     
     :dp:`fls_lcrd0birf0un`
     See :s:`BitXorAssignmentExpression`.
   :chapter:
     :dp:`fls_lkjwyy78m2vx`
     A :t:`bit xor assignment expression` is a :t:`compound assignment expression`
     that uses bit exclusive or arithmetic.

.. glossary-entry:: division assignment
   :glossary-dp: fls_0lpT9Ncj7S9X
   
   :glossary:
     :dp:`fls_kvQskrzE1y97`
     For :dt:`division assignment`, see :t:`division assignment expression`.

.. glossary-entry:: division assignment expression
   :glossary-dp: fls_ccv27fji08ou
   
   :glossary:
     :dp:`fls_lzuz5fkveikk`
     A :dt:`division assignment expression` is a :t:`compound assignment expression`
     that uses division.
     
     :dp:`fls_cdxt76aqwtkq`
     See :s:`DivisionAssignmentExpression`.
   :chapter:
     :dp:`fls_pkzj0uigfcgm`
     A :t:`division assignment expression` is a :t:`compound assignment expression`
     that uses division.

.. glossary-entry:: multiplication assignment
   :glossary-dp: fls_lpSCLhnaxeCg
   
   :glossary:
     :dp:`fls_llUb5VHKjwW4`
     For :dt:`multiplication assignment`, see
     :t:`multiplication assignment expression`.

.. glossary-entry:: multiplication assignment expression
   :glossary-dp: fls_yo4k6lk0tizn
   
   :glossary:
     :dp:`fls_eo9gx05n5ru3`
     A :dt:`multiplication assignment expression` is a
     :t:`compound assignment expression` that uses multiplication.
     
     :dp:`fls_b0dc5lec1mdc`
     See :s:`MultiplicationAssignmentExpression`.
   :chapter:
     :dp:`fls_ndlv3k9uclz2`
     A :t:`multiplication assignment expression` is a
     :t:`compound assignment expression` that uses multiplication.

.. glossary-entry:: remainder assignment
   :glossary-dp: fls_JnhUWipah0nO
   
   :glossary:
     :dp:`fls_58eDC2XtQcaR`
     For :dt:`remainder assignment`, see :t:`remainder assignment expression`.

.. glossary-entry:: remainder assignment expression
   :glossary-dp: fls_mio7pagghcks
   
   :glossary:
     :dp:`fls_en7ytqvefw7j`
     A :dt:`remainder assignment expression` is a
     :t:`compound assignment expression` that uses remainder division.
     
     :dp:`fls_rkk80quk8uzc`
     See :s:`RemainderAssignmentExpression`.
   :chapter:
     :dp:`fls_fbp5dojti27r`
     A :t:`remainder assignment expression` is a :t:`compound assignment expression`
     that uses remainder division.

.. glossary-entry:: shift left assignment
   :glossary-dp: fls_o8EVuKgr0Y98
   
   :glossary:
     :dp:`fls_6adWrtvab6Tw`
     For :dt:`shift left assignment`, see :t:`shift left assignment expression`.

.. glossary-entry:: shift left assignment expression
   :glossary-dp: fls_29n0oe4d7lwa
   
   :glossary:
     :dp:`fls_j15ke2p8cjfp`
     A :dt:`shift left assignment expression` is a
     :t:`compound assignment expression` that uses bit shift left arithmetic.
     
     :dp:`fls_ozu74fsakomn`
     See :s:`ShiftLeftAssignmentExpression`.
   :chapter:
     :dp:`fls_oy9ur11k78t`
     A :t:`shift left assignment expression` is a :t:`compound assignment expression`
     that uses bit shift left arithmetic.

.. glossary-entry:: shift right assignment
   :glossary-dp: fls_V5LMAe8ijiMQ
   
   :glossary:
     :dp:`fls_XuwcHjwHdyA8`
     For :dt:`shift right assignment`, see :t:`shift right assignment expression`.

.. glossary-entry:: shift right assignment expression
   :glossary-dp: fls_cqfzbsasnd1t
   
   :glossary:
     :dp:`fls_1jpnp7hatlmu`
     A :dt:`shift right assignment expression` is a
     :t:`compound assignment expression` that uses bit shift right arithmetic.
     
     :dp:`fls_naqzlebew1uf`
     See :s:`ShiftRightAssignmentExpression`.
   :chapter:
     :dp:`fls_s7rey2bndfei`
     A :t:`shift right assignment expression` is a
     :t:`compound assignment expression` that uses bit shift right arithmetic.

.. glossary-entry:: subtraction assignment
   :glossary-dp: fls_0hf1gNf90qKr
   
   :glossary:
     :dp:`fls_75Eyk2YXO2j4`
     For :dt:`subtraction assignment`, see :t:`subtraction assignment`.

.. glossary-entry:: subtraction assignment expression
   :glossary-dp: fls_a4iu72zn4h0
   
   :glossary:
     :dp:`fls_4pb85nl4r7vs`
     A :dt:`subtraction assignment expression` is a
     :t:`compound assignment expression` that uses subtraction.
     
     :dp:`fls_mye9yj5tc8hr`
     See :s:`SubtractionAssignmentExpression`.
   :chapter:
     :dp:`fls_7l7v7vigw3fu`
     A :t:`subtraction assignment expression` is a
     :t:`compound assignment expression` that uses subtraction.

.. glossary-entry:: assigned operand
   :glossary-dp: fls_l78iam7w8w38
   
   :glossary:
     :dp:`fls_g714mnh7s7fx`
     An :dt:`assigned operand` is the target :t:`operand` of a
     :t:`compound assignment expression`.
     
     :dp:`fls_z0amfuj9vsqe`
     See :s:`AssignedOperand`.
   :chapter:
     :dp:`fls_dvy201zd6oym`
     An :t:`assigned operand` is the target :t:`operand` of a
     :t:`compound assignment expression`.

.. glossary-entry:: modifying operand
   :glossary-dp: fls_5hoe1v960xfi
   
   :glossary:
     :dp:`fls_9wt2l5gg06pb`
     A :dt:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
     is used in the calculation of a :t:`compound assignment expression`.
     
     :dp:`fls_qnwbrwdnv7n0`
     See :s:`ModifyingOperand`.
   :chapter:
     :dp:`fls_9v09ayi2azpe`
     A :t:`modifying operand` is an :t:`operand` that supplies the :t:`value` that
     is used in the calculation of a :t:`compound assignment expression`.

.. glossary-entry:: mutable assignee expression
   :glossary-dp: fls_TEVPHHiCMByO
   
   :glossary:
     :dp:`fls_0RSlFbwrB3gp`
     A :dt:`mutable assignee expression` is an :t:`assignee expression` whose
     :t:`value` can be modified.

:dp:`fls_row7saf53vwd`
An :t:`assigned operand` shall denote a :t:`mutable assignee expression`.

:dp:`fls_xmgcdw9yhb55`
The :t:`type` of a :t:`compound assignment` is the :t:`unit type`.

:dp:`fls_yeh6mvyvb4dp`
The :t:`value` of a :t:`compound assignment` is the :t:`unit value`.

:dp:`fls_657knnsobdyu`
The :t:`type` of the :t:`assigned operand` of an :t:`addition assignment` shall
implement the :std:`core::ops::AddAssign` trait where the type of the right
operand is the trait implementation type parameter.

:dp:`fls_m942dwwmr2cl`
The :t:`type` of the :t:`assigned operand` of a :t:`bit and assignment` shall
implement the :std:`core::ops::BitAndAssign` :t:`trait` where the :t:`type` of
the :t:`modifying operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_np33oqrz33mp`
The :t:`type` of the :t:`assigned operand` of a :t:`bit or assignment` shall
implement the :std:`core::ops::BitOrAssign` :t:`trait` where the :t:`type` of
the :t:`modifying operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_atdpr8be2o2r`
The :t:`type` of the :t:`assigned operand` of a :t:`bit xor assignment` shall
implement the :std:`core::ops::BitXorAssign` :t:`trait` where the :t:`type` of
the :t:`modifying operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_fbgwb3pdfgz`
The :t:`type` of the :t:`assigned operand` of a :t:`division assignment` shall
implement the :std:`core::ops::DivAssign` :t:`trait` where the :t:`type` of the
:t:`modifying operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_8tbxq95x06yt`
The :t:`type` of the :t:`assigned operand` of a :t:`multiplication assignment`
shall implement the :std:`core::ops::MulAssign` :t:`trait` where the :t:`type`
of the :t:`modifying operand` is the :t:`trait implementation`
:t:`type parameter`.

:dp:`fls_9oy9zo3x3fy3`
The :t:`type` of the :t:`assigned operand` of a :t:`remainder assignment` shall
implement the :std:`core::ops::RemAssign` :t:`trait` where the :t:`type` of the
:t:`modifying operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_pdgj2xekdead`
The :t:`type` of the :t:`assigned operand` of a :t:`shift left assignment` shall
implement the :std:`core::ops::ShlAssign` :t:`trait` where the :t:`type` of the
:t:`modifying operand` is the :t:`trait implementation` :t:`type parameter`.

:dp:`fls_4uoi6k8r7mvc`
The :t:`type` of the :t:`assigned operand` of a :t:`shift right assignment`
shall implement the :std:`core::ops::ShrAssign` :t:`trait` where the :t:`type`
of the :t:`modifying operand` is the :t:`trait implementation`
:t:`type parameter`.

:dp:`fls_fjaz4m90cagr`
The :t:`type` of the :t:`assigned operand` of a :t:`subtraction assignment`
shall implement the :std:`core::ops::SubAssign` :t:`trait` where the :t:`type`
of the :t:`modifying operand` is the :t:`trait implementation`
:t:`type parameter`.

.. rubric:: Dynamic Semantics

:dp:`fls_eesn9kuylim`
The :t:`evaluation` of a :t:`compound assignment` proceeds as follows:

#. :dp:`fls_4nnqz4etisgw`
   If the :t:`[type]s` of both :t:`[operand]s` are :t:`[integer type]s` or :t:`[floating-point type]s`, then

   #. :dp:`fls_a2g4hs15jpiu`
      The :t:`modifying operand` is evaluated.

   #. :dp:`fls_kuet16jp6ps9`
      The :t:`assigned operand` is evaluated.

   #. :dp:`fls_hovju0sni9gr`
      The appropriate :t:`function` is invoked as indicated below.

#. :dp:`fls_ngimpabunzis`
   Otherwise

   #. :dp:`fls_4sbpfi12frwe`
      The :t:`assigned operand` is evaluated.

   #. :dp:`fls_n5ds6ydgckvo`
      The :t:`modifying operand` is evaluated.

   #. :dp:`fls_xjdu0y1slsg9`
      The appropriate :t:`function` is invoked as indicated below.

:dp:`fls_ijfmnnrdlu8n`
For an :t:`addition assignment`,
``core::ops::AddAssign::add_assign(&mut assigned_operand, modifying_operand)``
is invoked.

:dp:`fls_6x7j9x354pkb`
For a :t:`bit and assignment`,
``core::ops::BitAndAssign::bitand_assign(&mut assigned_operand, modifying_operand)``
is invoked.

:dp:`fls_h2cpbz2t74hy`
For a :t:`bit or assignment`,
``core::ops::BitOrAssign::bitor_assign(&mut assigned_operand, modifying_operand)``
is invoked.

:dp:`fls_whj50spxz3bh`
For a :t:`bit xor assignment`,
``core::ops::BitXorAssign::bitxor_assign(&mut assigned_operand, modifying_operand)``
is invoked.

:dp:`fls_d1cxq1zbt5fq`
For a :t:`division assignment`,
``core::ops::DivAssign::div_assign(&mut assigned_operand, modifying_operand)``
is invoked.

:dp:`fls_48i245an2449`
For a :t:`multiplication assignment`,
``core::ops::MulAssign::mul_assign(&mut assigned_operand, modifying_operand)``
is invoked.

:dp:`fls_69wr03rt0ali`
For a :t:`remainder assignment`,
``core::ops::RemAssign::rem_assign(&mut assigned_operand, modifying_operand)``
is invoked.

:dp:`fls_9d970yfwmj2d`
For a :t:`shift left assignment`,
``core::ops::ShlAssign::shl_assign(&mut assigned_operand, modifying_operand)``
is invoked.

:dp:`fls_p9687v3xckps`
For a :t:`shift right assignment`,
``core::ops::ShrAssign::shr_assign(&mut assigned_operand, modifying_operand)``
is invoked.

:dp:`fls_8j408kckzzud`
For a :t:`subtraction assignment`,
``core::ops::SubAssign::sub_assign(&mut assigned_operand, modifying_operand)``
is invoked.

.. rubric:: Examples

.. code-block:: rust

   let mut result = 42;
   result += 1
   result &= 59
   result /= 3
   result ^= 2
   result *= 81
   result |= 9402
   result %= 7
   result <<= 2
   result >>= 3
   result -= 0

.. _fls_tpwp86mronn2:

Underscore Expressions
----------------------

.. rubric:: Syntax

.. syntax::

   UnderscoreExpression ::=
       $$_$$

.. rubric:: Legality Rules

.. glossary-entry:: underscore expression
   :glossary-dp: fls_57kis2vnt3cv
   
   :glossary:
     :dp:`fls_ukl1sefb99gj`
     An :dt:`underscore expression` is an :t:`expression` that acts as a placeholder
     in a :t:`destructuring assignment`.
     
     :dp:`fls_qbo267kdjcgs`
     See :s:`UnderscoreExpression`.
   :chapter:
     :dp:`fls_pydmv629vfuu`
     An :t:`underscore expression` is an :t:`expression` that acts as a placeholder
     in a :t:`destructuring assignment`.

:dp:`fls_wms3dbwjwyu4`
An :t:`underscore expression` shall appear in the :t:`assigned operand` of a
:t:`destructuring assignment`.

.. rubric:: Examples

.. code-block:: rust

   let pair = (1, 2);
   let mut second = 0;
   (_, second) = pair;

.. _fls_g0uyl7qw4c7w:

Parenthesized Expressions
-------------------------

.. rubric:: Syntax

.. syntax::

   ParenthesizedExpression ::=
       $$($$ Operand $$)$$

.. rubric:: Legality Rules

.. glossary-entry:: parenthesized expression
   :glossary-dp: fls_fl56jfxbj0f
   
   :glossary:
     :dp:`fls_yu1x2rr7cewa`
     A :dt:`parenthesized expression` is an :t:`expression` that groups other
     expressions.
     
     :dp:`fls_p9exa6fpplfu`
     See :s:`ParenthesizedExpression`.
   :chapter:
     :dp:`fls_jhazc75w5vj`
     A :t:`parenthesized expression` is an :t:`expression` that groups other
     :t:`[expression]s`.

:dp:`fls_5d66h7naoup6`
The :t:`type` of a :t:`parenthesized expression` is the :t:`type` of its
:t:`operand`.

:dp:`fls_xp9whcj2obk8`
The :t:`value` of a :t:`parenthesized expression` is the :t:`value` of its
:t:`operand`.

.. rubric:: Dynamic Semantics

:dp:`fls_2po52gv0m021`
The :t:`evaluation` of a :t:`parenthesized expression` evaluates its
:t:`operand`.

.. rubric:: Examples

.. code-block:: rust

   (1 + 2) * 3

.. _fls_xinykul167l:

Array Expressions
-----------------

.. rubric:: Syntax

.. syntax::

   ArrayExpression ::=
       $$[$$ ArrayElementExpression? $$]$$

   ArrayElementExpression ::=
       ArrayElementConstructor
     | ArrayRepetitionConstructor

   ArrayElementConstructor ::=
       ExpressionList

   ArrayRepetitionConstructor ::=
       RepeatOperand $$;$$ SizeOperand

   RepeatOperand ::=
       Operand

   SizeOperand ::=
       Operand

.. rubric:: Legality Rules

.. glossary-entry:: array
   :glossary-dp: fls_bn1regeucxqi
   
   :glossary:
     :dp:`fls_metry7a5prpt`
     An :dt:`array` is a :t:`value` of an :t:`array type`.

.. glossary-entry:: array expression
   :glossary-dp: fls_yvzpqb192pci
   
   :glossary:
     :dp:`fls_pyjkjbvqarto`
     An :dt:`array expression` is an :t:`expression` that constructs an :t:`array`.
     
     :dp:`fls_vua1xy4y9irp`
     See :s:`ArrayExpression`.
   :chapter:
     :dp:`fls_ya9res33oxt6`
     An :t:`array expression` is an :t:`expression` that constructs an :t:`array`.

.. glossary-entry:: array element constructor
   :glossary-dp: fls_2d9fee2o9
   
   :glossary:
     :dp:`fls_cmx9ls5zoazp`
     An :dt:`array element constructor` is an :t:`array expression` that lists all
     elements of the :t:`array` being constructed.
     
     :dp:`fls_9bwte7cmszl1`
     See :s:`ArrayElementConstructor`.
   :chapter:
     :dp:`fls_fwtd3b10veiw`
     An :t:`array element constructor` is an :t:`array expression` that lists all
     elements of the :t:`array` being constructed.

.. glossary-entry:: array repetition constructor
   :glossary-dp: fls_6jkgj61m49vg
   
   :glossary:
     :dp:`fls_st1kw8mor2zk`
     An :dt:`array repetition constructor` is an :t:`array expression` that
     specifies how many times an element is repeated in the :t:`array` being
     constructed.
     
     :dp:`fls_1zr997qwsal2`
     See :s:`ArrayRepetitionConstructor`.
   :chapter:
     :dp:`fls_81jf78m5uga4`
     An :t:`array repetition constructor` is an :t:`array expression` that specifies
     how many times an element is repeated in the :t:`array` being constructed.

.. glossary-entry:: repeat operand
   :glossary-dp: fls_b35oy3nnzixm
   
   :glossary:
     :dp:`fls_ol2y1og2jwss`
     A :dt:`repeat operand` is an :t:`operand` that specifies the element being
     repeated in an :t:`array repetition constructor`.
     
     :dp:`fls_r4acyux78txu`
     See :s:`RepeatOperand`.
   :chapter:
     :dp:`fls_3y69y9ga4at7`
     A :t:`repeat operand` is an :t:`operand` that specifies the element being
     repeated in an :t:`array repetition constructor`.

.. glossary-entry:: size operand
   :glossary-dp: fls_2y5oyon3y1za
   
   :glossary:
     :dp:`fls_srajsqi5i3py`
     A :dt:`size operand` is an :t:`operand` that specifies the size of an
     :t:`array` or an :t:`array type`.
     
     :dp:`fls_228ioayvdguv`
     See :s:`SizeOperand`.
   :chapter:
     :dp:`fls_2l9objtb23zn`
     A :t:`size operand` is an :t:`operand` that specifies the size of an :t:`array`
     or an :t:`array type`.

:dp:`fls_9gmnjvs83d8o`
The :t:`size operand` shall be a :t:`constant expression`.

:dp:`fls_by21pey7k423`
The :t:`[type]s` of the :t:`[operand]s` of an :t:`array element constructor`
shall be :t:`unifiable`.

:dp:`fls_x2xu2pynxy1u`
If the :t:`size operand` is greater than one, then the :t:`type` of the
:t:`repeat operand` shall implement the :std:`core::copy::Copy` :t:`trait`
or the :t:`repeat operand` shall be a :t:`path expression` resolving to a
:t:`constant`.

:dp:`fls_qplsh3pdqitq`
The :t:`type` of the :t:`size operand` shall be :t:`type` :c:`usize`.

:dp:`fls_wmsekin1gd2y`
The :t:`type` of an :t:`array expression` is ``[T; N]``, where ``T`` is the
:t:`element type` and ``N`` is the size of the array. The :t:`size` of an
:t:`array` is determined as follows:

* :dp:`fls_2gto5kp9bjw8`
  If the :t:`array expression` appears with an :t:`array element constructor`,
  then the :t:`size` is the number of :t:`[operand]s` in the
  :t:`array element constructor`.

* :dp:`fls_guop34ayjw2`
  Otherwise the :t:`size` is the :t:`value` of :t:`size operand`.

:dp:`fls_aj6tbe54v5jl`
The :t:`value` of an :t:`array expression` is the constructed :t:`array`.

.. rubric:: Dynamic Semantics

:dp:`fls_t52in1kkyli3`
The :t:`evaluation` of an :t:`array expression` with an
:t:`array element constructor` evaluates its :t:`[operand]s` in left-to-right
order.

:dp:`fls_1kj8nlc5eb8a`
The :t:`evaluation` of an :t:`array expression` with an
:t:`array repetition constructor` proceeds as follows:

#. :dp:`fls_f3izbkm8607z`
   If the :t:`value` of the :t:`size operand` is greater than zero, then the
   :t:`repeat operand` is evaluated once and its :t:`value` is
   :t:`passed <passing convention>` :t:`by copy` :t:`[size operand]'s`
   :t:`value` times.

#. :dp:`fls_5cs68nm54l31`
   Otherwise the :t:`repeat operand` is evaluated once.

.. rubric:: Examples

.. code-block:: rust

   [1, 2, 3]
   ["one", "two", "three",]

:dp:`fls_p7hcqryal5cm`
Two dimensional array.

.. syntax::

   [[0, 0], [0, 1], [1, 0], [1, 1]]

:dp:`fls_izlpt6100gvk`
An array of nine 42s.

.. syntax::

   [42; 9]

.. _fls_sxcr4aa098i6:

Indexing Expressions
--------------------

.. rubric:: Syntax

.. syntax::

   IndexExpression ::=
       IndexedOperand $$[$$ IndexingOperand $$]$$

   IndexedOperand ::=
       Operand

   IndexingOperand ::=
       Operand

.. rubric:: Legality Rules

.. glossary-entry:: indexable type
   :glossary-dp: fls_S0pnJKPJPU0i
   
   :glossary:
     :dp:`fls_AdVGyKZFvvUS`
     A :dt:`indexable type` is a :t:`type` that implements the
     :std:`core::ops::Index` :t:`trait`.
   :chapter:
     :dp:`fls_X9kdEAPTqsAe`
     An :t:`indexable type` is a :t:`type` that implements the
     :std:`core::ops::Index` :t:`trait`.

.. glossary-entry:: index expression
   :glossary-dp: fls_6tysvlg2ifr3
   
   :glossary:
     :dp:`fls_1f7e9q8n431n`
     An :dt:`index expression` is an :t:`expression` that indexes into a :t:`value`
     of a :t:`type`.
     
     :dp:`fls_xm2er7vuo07g`
     See :s:`IndexExpression`.
   :chapter:
     :dp:`fls_42ijvuqqqlvh`
     An :t:`index expression` is an :t:`expression` that indexes into a :t:`value`
     of an :t:`indexable type`.

.. glossary-entry:: indexed operand
   :glossary-dp: fls_irp9ive4e66r
   
   :glossary:
     :dp:`fls_dvmm47wnl33e`
     An :dt:`indexed operand` is an :t:`operand` which indicates the :t:`value` of a
     :t:`type` implementing :std:`core::ops::Index` being indexed into by an
     :t:`index expression`.
     
     :dp:`fls_je8eh3a02riq`
     See :s:`IndexedOperand`.
   :chapter:
     :dp:`fls_pc0c22asgzvw`
     An :t:`indexed operand` is an :t:`operand` which indicates the :t:`value`
     being indexed into by an :t:`index expression`.

.. glossary-entry:: indexing operand
   :glossary-dp: fls_a350zwl1or4g
   
   :glossary:
     :dp:`fls_ipw4tfrserbu`
     An :dt:`indexing operand` is an :t:`operand` which specifies the index for the
     :t:`indexed operand` being indexed into by an :t:`index expression`.
     
     :dp:`fls_t2j8vzlrlvb0`
     See :s:`IndexingOperand`.
   :chapter:
     :dp:`fls_ff3sgpldn52o`
     An :t:`indexing operand` is an :t:`operand` which specifies the index of an
     :t:`index expression`.

:dp:`fls_w96p9oyv5mqt`
An :t:`index expression` is a :t:`constant expression` if the
:t:`indexing operand` and :t:`indexed operand` are :t:`[constant expression]s`.

:dp:`fls_u9sl7h4i8hqu`
The :t:`type` of the :t:`indexing operand` is the :t:`generic parameter` of the
:std:`core::ops::Index` :t:`implementation` of the :t:`type` of the
:t:`indexed operand`.

:dp:`fls_98qeczwv7fmy`
If the :t:`indexed operand` is evaluated in a :t:`value expression context`,
then

* :dp:`fls_sb2b8gszzaxq`
  The :t:`type` of the :t:`indexed operand` shall implement the
  :std:`core::ops::Index` :t:`trait`.

* :dp:`fls_issaykiuha75`
  The :t:`type` of the :t:`index expression` is ``&T``, where ``T`` is
  :t:`associated type` :std:`core::ops::Index::Output`.

:dp:`fls_y3sduoma6q9v`
If the :t:`indexed operand` is :t:`mutable` and the :t:`index expression` is
evaluated in a :t:`mutable place expression context`, then

* :dp:`fls_ld7lbvqms5i6`
  The :t:`type` of the :t:`indexed operand` shall implement the
  :std:`core::ops::IndexMut` :t:`trait`.

* :dp:`fls_nw705fpon79b`
  The :t:`type` of the :t:`index expression` is ``&mut T``, where ``T`` is
  the element type of the :t:`indexed operand`'s :t:`type`.

:dp:`fls_fouu0z3jwoad`
The :t:`value` of an :t:`index expression` is the indexed memory location.

.. rubric:: Dynamic Semantics

:dp:`fls_6sgj0ltt21i`
The :t:`evaluation` of an :t:`index expression` proceeds as follows:

#. :dp:`fls_e5l4y3dy69xi`
   The :t:`indexed operand` is evaluated.

#. :dp:`fls_fza3omn8yw7s`
   The :t:`indexing operand` is evaluated.

#. :dp:`fls_ehamppbq4gmg`
   If the :t:`index expression` is evaluated in a :t:`mutable place
   expression context`, then :t:`expression`
   ``*core::ops::IndexMut::index_mut(&mut indexed_operand, indexing_operand)``
   is evaluated.

#. :dp:`fls_i68oxj659hc1`
   Otherwise :t:`expression` ``*core::ops::Index::index(&indexed_operand,
   indexing_operand)`` is evaluated.

.. rubric:: Examples

.. code-block:: rust

   let a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
   a[1][2]

:dp:`fls_esvpmh6razg3`
Evaluates to 6.

.. _fls_k64tfywtn0g8:

Tuple Expressions
-----------------

.. rubric:: Syntax

.. syntax::

   TupleExpression ::=
       $$($$ TupleInitializerList? $$)$$

   TupleInitializerList ::=
       ExpressionList

.. rubric:: Legality Rules

.. glossary-entry:: tuple expression
   :glossary-dp: fls_udl6ujjg1jae
   
   :glossary:
     :dp:`fls_x7m4u1dx4eli`
     A :dt:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.
     
     :dp:`fls_qawnvcddgyxx`
     See :s:`TupleExpression`.
   :chapter:
     :dp:`fls_87rp1hfwvjel`
     A :t:`tuple expression` is an :t:`expression` that constructs a :t:`tuple`.

.. glossary-entry:: tuple initializer
   :glossary-dp: fls_zfvvbf7ncrhj
   
   :glossary:
     :dp:`fls_94hg6re11zl5`
     A :dt:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
     :t:`tuple field` in a :t:`tuple expression`.
   :chapter:
     :dp:`fls_581y6jq1eyn8`
     A :t:`tuple initializer` is an :t:`operand` that provides the :t:`value` of a
     :t:`tuple field` in a :t:`tuple expression`.

:dp:`fls_ljz3sxmfzflm`
The :t:`type` of a :t:`tuple expression` is ``(T1, T2, ..., TN)``, where ``T1``
is the :t:`type` of the first :t:`tuple initializer`, ``T2`` is the :t:`type` of
the second :t:`tuple initializer`, and ``TN`` is the :t:`type` of the ``N``-th
:t:`tuple initializer`.

:dp:`fls_k2aznqo9j49p`
The :t:`value` of a :t:`tuple expression` is ``(V1, V2, ..., VN)``, where ``V1``
is the :t:`value` of the first :t:`tuple initializer`, ``V2`` is the :t:`value`
of the second :t:`tuple initializer`, and ``VN`` is the :t:`value` of the
``N``-th :t:`tuple initializer`.

.. rubric:: Dynamic Semantics

:dp:`fls_waf55yd3mpsq`
The :t:`evaluation` of a :t:`tuple expression` evaluates its
:t:`[tuple initializer]s` in left-to-right order.

.. rubric:: Examples

.. code-block:: rust

   ()
   (1.2, 3.4)
   ("hello", 42i16, true)

.. _fls_8tsynkj2cufj:

Struct Expressions
------------------

.. rubric:: Syntax

.. syntax::

   StructExpression ::=
       Constructee $${$$ StructExpressionContent? $$}$$

   Constructee ::=
       PathExpression

   StructExpressionContent ::=
       BaseInitializer
     | FieldInitializerList ($$,$$ BaseInitializer | $$,$$?)

   BaseInitializer ::=
       $$..$$ Operand

   FieldInitializerList ::=
       FieldInitializer ($$,$$ FieldInitializer)*

   FieldInitializer ::=
       IndexedInitializer
     | NamedInitializer
     | ShorthandInitializer

   IndexedInitializer ::=
       FieldIndex $$:$$ Expression

   NamedInitializer ::=
       Identifier $$:$$ Expression

   ShorthandInitializer ::=
       Identifier

.. rubric:: Legality Rules

.. glossary-entry:: struct expression
   :glossary-dp: fls_dxfyejkbiz3p
   
   :glossary:
     :dp:`fls_m8n9e0sxyb95`
     A :dt:`struct expression` is an :t:`expression` that constructs an
     :t:`enum value`, a :t:`struct value`, or a :t:`union value`.
     
     :dp:`fls_odm68rhu2j1`
     See :s:`StructExpression`.
   :chapter:
     :dp:`fls_ij8rebvupb85`
     A :t:`struct expression` is an :t:`expression` that constructs an
     :t:`enum value`, a :t:`struct value`, or a :t:`union value`.

.. glossary-entry:: constructee
   :glossary-dp: fls_fBGjoTVhYvUe
   
   :glossary:
     :dp:`fls_Twbu94uGW4Cb`
     A :dt:`constructee` indicates the :t:`enum variant`, :t:`struct` or :t:`union`
     whose value is being constructed by a :t:`struct expression`.
   :chapter:
     :dp:`fls_4z91ymz3ciup`
     A :t:`constructee` indicates the :t:`enum variant`, :t:`struct`, or :t:`union`
     whose value is being constructed by a :t:`struct expression`.

.. glossary-entry:: base initializer
   :glossary-dp: fls_a8tavqxuvaju
   
   :glossary:
     :dp:`fls_dnuwn2tnvtgy`
     A :dt:`base initializer` is a :t:`construct` that specifies an :t:`enum value`,
     a :t:`struct value`, or a :t:`union value` to be used as a base for
     construction in a :t:`struct expression`.
     
     :dp:`fls_mprzem71zlhy`
     See :s:`BaseInitializer`.
   :chapter:
     :dp:`fls_uib1ml41mfrn`
     A :t:`base initializer` is a :t:`construct` that specifies an :t:`enum value`, or
     a :t:`struct value` to be used as a base for
     construction in a :t:`struct expression`.

:dp:`fls_gfu267bpl9ql`
The :t:`type` of a :t:`base initializer` is the :t:`type` of its :t:`operand`.
The :t:`type` of a :t:`base initializer` shall be the same as the :t:`type` of
the :t:`constructee`.

.. glossary-entry:: indexed initializer
   :glossary-dp: fls_rua2ni3p9qz2
   
   :glossary:
     :dp:`fls_oonqolgqyrq1`
     An :dt:`indexed initializer` is a :t:`construct` that specifies the index and
     initial :t:`value` of a :t:`field` in a :t:`struct expression`.
     
     :dp:`fls_werlw98l3ra0`
     See :s:`IndexedInitializer`.
   :chapter:
     :dp:`fls_ph7fsphbpbv4`
     An :t:`indexed initializer` is a :t:`construct` that specifies the index and
     initial :t:`value` of a :t:`field` in a :t:`struct expression`.

:dp:`fls_y3p6rtm7ek3l`
An :t:`indexed initializer` matches a :t:`field` of the :t:`constructee`
when the :t:`field index` of the :t:`indexed initializer` resolves to a valid
position of a :t:`field` in the :t:`constructee`. Such an
:t:`indexed initializer` is a :dt:`matched indexed initializer`.

:dp:`fls_dfajs3xaxbv`
The :t:`type` of the :t:`operand` of an :t:`indexed initializer` and the
:t:`type` of the matched :t:`field` shall be :t:`unifiable`.

:dp:`fls_e5b9n910z1cp`
The :t:`value` of an :t:`indexed initializer` is the :t:`value` of its
:t:`operand`.

.. glossary-entry:: named initializer
   :glossary-dp: fls_kp0mbopkbjer
   
   :glossary:
     :dp:`fls_xwvz8i4jim7a`
     A :dt:`named initializer` is a :t:`construct` that specifies the name and
     initial :t:`value` of a :t:`field` in a :t:`struct expression`.
     
     :dp:`fls_aueznbw3lohl`
     See :s:`NamedInitializer`.
   :chapter:
     :dp:`fls_lwyq3vyc91rn`
     A :t:`named initializer` is a :t:`construct` that specifies the name and
     initial :t:`value` of a :t:`field` in a :t:`struct expression`.

:dp:`fls_qed1pps827dv`
A :t:`named initializer` matches a :t:`field` of the :t:`constructee` when
its :t:`identifier` and the :t:`name` of the :t:`field` are the same. Such a
:t:`named initializer` is a :dt:`matched named initializer`.

:dp:`fls_b60omrhc7t73`
The :t:`type` of a :t:`named initializer` and the :t:`type` of the matched
:t:`field` shall be :t:`unifiable`.

:dp:`fls_z3gj1v6g605r`
The :t:`value` of a :t:`named initializer` is the :t:`value` of its
:t:`expression`.

.. glossary-entry:: shorthand initializer
   :glossary-dp: fls_oa4p10yles30
   
   :glossary:
     :dp:`fls_bgxxg48snck1`
     A :dt:`shorthand initializer` is a :t:`construct` that specifies the :t:`name`
     of a :t:`field` in a :t:`struct expression`.
     
     :dp:`fls_qc08ydgmqudi`
     See :s:`ShorthandInitializer`.
   :chapter:
     :dp:`fls_57t368kema7h`
     A :t:`shorthand initializer` is a :t:`construct` that specifies the :t:`name`
     of a :t:`field` in a :t:`struct expression`.

:dp:`fls_sm2hx8sh4agb`
A :t:`shorthand initializer` is equivalent to a :t:`named initializer` where
both the :t:`identifier` and the :t:`expression` of the :t:`named initializer`
denote the :t:`identifier` of the :t:`shorthand initializer`.

:dp:`fls_yjx1t3x6qpfg`
A :t:`shorthand initializer` matches a :t:`field` of the :t:`constructee`
when its :t:`identifier` and the :t:`name` of the :t:`field` are the same. Such
a :t:`shorthand initializer` is a :dt:`matched shorthand initializer`.

:dp:`fls_2dajkhq58cdp`
The :t:`type` of a :t:`shorthand initializer` and the :t:`type` of the matched
:t:`field` shall be :t:`unifiable`.

:dp:`fls_9s4znhi0u3ys`
The :t:`value` of a :t:`shorthand initializer` is the :t:`value` its
:t:`identifier` resolves to.

:dp:`fls_i31rodt42m0z`
The :t:`type` of a :t:`struct expression` is the :t:`type` of the
:t:`constructee`.

:dp:`fls_sjwd8o5mknjo`
The :t:`value` of a :t:`struct expression` is the :t:`enum value`,
:t:`struct value`, or :t:`union value` in construction.

:dp:`fls_ccqomsereni2`
If the :t:`constructee` is a :t:`record enum variant` or a :t:`record struct`,
then

* :dp:`fls_pivpdyr4seez`
  For each :t:`field` of the :t:`constructee`, the :t:`struct expression` shall
  either:

  * :dp:`fls_bbmm5vir9xos`
    Contain at most one :t:`matched named initializer`, or

  * :dp:`fls_9370n5xkkzce`
    Contain at most one :t:`matched shorthand initializer`, or

  * :dp:`fls_rclgwzdhfjj`
    Have exactly one :t:`base initializer`.

* :dp:`fls_lmxz5768v5d8`
  A :t:`base initializer` is allowed even if all :t:`[field]s` of the
  :t:`constructee` have been matched.

:dp:`fls_939cugbxju5e`
If the :t:`constructee` is a :t:`tuple enum variant` or a :t:`tuple struct`,
then

* :dp:`fls_c34qwhaq2asm`
  For each :t:`field` of the :t:`constructee`, the :t:`struct expression` shall
  either:

  * :dp:`fls_j2kmp1fee0g4`
    Contain at most one :t:`matched indexed initializer`, or

  * :dp:`fls_90q7krxazc6u`
    Have exactly one :t:`base initializer`.

* :dp:`fls_qo05owpmtag0`
  A :t:`base initializer` is allowed even if all :t:`[field]s` of the
  :t:`constructee` have been matched.

:dp:`fls_ywh3nk6emwmw`
If the :t:`constructee` is a :t:`union type`, then

* :dp:`fls_5w9lj5dc84p`
  The :t:`struct expression` shall not contain a :t:`base initializer`.

* :dp:`fls_5zceer19mhdu`
  For the single :t:`field` of the :t:`constructee`, the :t:`struct expression`
  shall either:

  * :dp:`fls_mq80i8fof7sx`
    Contain exactly one :t:`matched named initializer`, or

  * :dp:`fls_raon1c1vrhx7`
    Contain exactly one :t:`matched shorthand initializer`.

:dp:`fls_njder5r7y5fg`
If the :t:`constructee` is a :t:`unit enum variant` or a :t:`unit struct`, then
the :t:`struct expression` shall have at most one :t:`base initializer`.

:dp:`fls_w7x9wy6t0qcp`
If a :t:`base initializer` is supplied, then for each :t:`field` that was not
matched in the :t:`struct expression` the :t:`value` of the corresponding
:t:`field` of the :t:`base initializer` is :t:`passed <passing convention>` to
the :t:`field` of the :t:`constructee`.

.. rubric:: Dynamic Semantics

:dp:`fls_vsxsbqps64o`
The :t:`evaluation` of a :t:`struct expression` evaluates its :t:`[operand]s` in
a left-to-right order.

.. rubric:: Examples

.. code-block:: rust

   enum Occupation {
       Engineer,
       Gardener
   }

   struct Employee {
       name: String,
       age: u16,
       occupation: Occupation
       compensation: u32
   }

   let alice = Employee {
       name: "Alice".to_string(),
       age: 23,
       occupation: Occupation::Engineer
       compensation: 250_000
   };

   let age = 45;

   let bob = Employee {
       name: "Bob".to_string(), // matched named initializer
       age, // matched shorthand initializer
       .. alice // equivalent to alice.occupation, alice.compensation
   };

   union Union {
   	int: u32,
   	float: f32
   }

   let u1 = Union { int: 0 };
   let u2 = Union { float: 0.0 };

.. _fls_mjVXiDQRIAzU:

Invocation Expressions
----------------------

.. _fls_xa4nbfas01cj:

Call Expressions
~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   CallExpression ::=
       CallOperand $$($$ ArgumentOperandList? $$)$$

   CallOperand ::=
       Operand

   ArgumentOperandList ::=
       ExpressionList

.. rubric:: Legality Rules

.. glossary-entry:: call expression
   :glossary-dp: fls_xeo59ol6uh5i
   
   :glossary:
     :dp:`fls_a9ap0tyk2eou`
     A :dt:`call expression` is an :t:`expression` that invokes a :t:`function` or
     constructs a :t:`tuple struct value` or :t:`tuple enum variant value`.
     
     :dp:`fls_aibti9uqrmmd`
     See :s:`CallExpression`.
   :chapter:
     :dp:`fls_fvgfx17ossd9`
     A :t:`call expression` is an :t:`expression` that invokes a :t:`function` or
     constructs a :t:`tuple enum variant value` or a :t:`tuple struct value`.

.. glossary-entry:: argument operand
   :glossary-dp: fls_dd008npswhij
   
   :glossary:
     :dp:`fls_ljuwr88k92vp`
     An :dt:`argument operand` is an :t:`operand` which is used as an argument in a
     :t:`call expression` or a :t:`method call expression`.
   :chapter:
     :dp:`fls_jvz5z3eqxb39`
     An :t:`argument operand` is an :t:`operand` which is used as an argument in a
     :t:`call expression` or a :t:`method call expression`.

.. glossary-entry:: call operand
   :glossary-dp: fls_ezk9xkst7gfj
   
   :glossary:
     :dp:`fls_cqnko94y4xbs`
     A :dt:`call operand` is the :t:`function` being invoked or the
     :t:`tuple struct value` or :t:`tuple enum variant value` being constructed by a
     :t:`call expression`.
     
     :dp:`fls_w6wu4wi6srjj`
     See :s:`CallOperand`.
   :chapter:
     :dp:`fls_7ql1c71eidg8`
     A :t:`call operand` is the :t:`function` being invoked or the
     :t:`tuple enum variant value` or the :t:`tuple struct value` being constructed
     by a :t:`call expression`.

.. glossary-entry:: Call conformance
   :glossary-dp: fls_Egfa8tdbqllA
   
   :glossary:
     :dp:`fls_Jr1gUX7Ju4Oh`
     :dt:`Call conformance` measures the compatibility between a set of
     :t:`[argument operand]s` and a set if :t:`[function parameter]s` or
     :t:`[field]s`.

.. glossary-entry:: adjusted call operand
   :glossary-dp: fls_wbdlbe61de3t
   
   :glossary:
     :dp:`fls_mchqbc64iu0u`
     An :dt:`adjusted call operand` is a :t:`call operand` adjusted with inserted :t:`[borrow expression]s` and :t:`[dereference expression]s`.

.. glossary-entry:: tuple struct call expression
   :glossary-dp: fls_UYCpeq4Z87My
   
   :glossary:
     :dp:`fls_DQaCUkskfXzk`
     A :dt:`tuple struct call expression` is a :t:`call expression` where the
     :t:`call operand` resolves to a :t:`tuple struct` or a :t:`tuple enum variant`.
   :chapter:
     :dp:`fls_QpBu34U6hXn9`
     A :t:`tuple struct call expression` is a :t:`call expression` where the
     :t:`call operand` resolves to a :t:`tuple struct`.

.. glossary-entry:: callee type
   :glossary-dp: fls_luuc01g4ffog
   
   :glossary:
     :dp:`fls_o21myf6wnnn6`
     A :dt:`callee type` is either a :t:`function item type`, a
     :t:`function pointer type`, a :t:`tuple struct type`, a :t:`tuple enum variant`
     or a :t:`type` that implements any of the :std:`core::ops::Fn`,
     :std:`core::ops::FnMut`, or :std:`core::ops::FnOnce` :t:`[trait]s`.
   :chapter:
     :dp:`fls_4t6imtiw6kzt`
     A :t:`callee type` is either a :t:`function item type`, a
     :t:`function pointer type`, a :t:`tuple enum variant`, a
     :t:`tuple struct type`, or a :t:`type` that implements any of the
     :std:`core::ops::Fn`, :std:`core::ops::FnMut`, or :std:`core::ops::FnOnce`
     :t:`[trait]s`.

:dp:`fls_bu6i3mcvnbin`
The :t:`type` of a :t:`call expression` is the :t:`return type` of the invoked
:t:`function`, the :t:`type` of the :t:`tuple enum variant` or the
:t:`tuple struct` being constructed, or :t:`associated type`
:std:`core::ops::FnOnce::Output`.

:dp:`fls_8ljrgdept7s8`
A :t:`call expression` whose :t:`callee type` is either an
:t:`external function item type`, an :t:`unsafe function item type`, or an
:t:`unsafe function pointer type` shall require :t:`unsafe context`.

:dp:`fls_7p6zrjbpj0kl`
The :t:`value` of a :t:`call expression` is determined as follows:

* :dp:`fls_yrr1s0tucgvh`
  If the :t:`callee type` is a :t:`function item type` or a
  :t:`function pointer type`, then the :t:`value` is the result of invoking the
  corresponding :t:`function` with the :t:`[argument operand]s`.

* :dp:`fls_RZjFs9koNOk8`
  If the :t:`callee type` is a :t:`tuple enum variant` or a
  :t:`tuple struct type`, then the :t:`value` is the result of constructing
  the :t:`tuple enum variant` or the :t:`tuple struct` with the
  :t:`[argument operand]s`.

* :dp:`fls_s3q3sej1hgho`
  If the :t:`callee type` implements the :std:`core::ops::Fn` :t:`trait`, then
  the :t:`value` is the result of invoking
  ``core::ops::Fn::call(adjusted_call_operand, argument_operand_tuple)``,
  where ``adjusted_call_operand`` is the :t:`adjusted call operand`, and
  ``argument_operand_tuple`` is a :t:`tuple` that wraps the
  :t:`[argument operand]s`.

* :dp:`fls_cu2ubdm3tfwb`
  If the :t:`call operand` implements the :std:`core::ops::FnMut` :t:`trait`,
  then the :t:`value` is the result of invoking
  ``core::ops::FnMut::call_mut(adjusted_call_operand, argument_operand_tuple),``
  where ``adjusted_call_operand`` is the :t:`adjusted call operand`, and
  ``argument_operand_tuple`` is a :t:`tuple` that wraps the
  :t:`[argument operand]s`.

* :dp:`fls_9bbewx1l7h5h`
  If the :t:`call operand` implements the :std:`core::ops::FnOnce` :t:`trait`,
  then the :t:`value` is the result of invoking
  ``core::ops::FnOnce::call_once(adjusted_call_operand, argument_operand_tuple),``
  where ``adjusted_call_operand`` is the :t:`adjusted call operand`, and
  ``argument_operand_tuple`` is a :t:`tuple` that wraps the
  :t:`[argument operand]s`.

:dp:`fls_ZSkcro52q097`
A :t:`call expression` is subject to :t:`call resolution`.

.. rubric:: Dynamic Semantics

:dp:`fls_ggr5i91vur0r`
The :t:`evaluation` of a :t:`call expression` proceeds as follows:

#. :dp:`fls_hwalzgdidbfz`
   The :t:`call operand` is evaluated.

#. :dp:`fls_p52mfvpadu7w`
   The :t:`[argument operand]s` are evaluated in left-to-right order.

#. :dp:`fls_1cyo5qhbl1j9`
   If the :t:`adjusted call operand` is a :t:`function item type` or
   :t:`function pointer type`, then corresponding :t:`function` is invoked.

#. :dp:`fls_nb0eqky2akzt`
   If the :t:`type` of the :t:`call operand` implements the
   :std:`core::ops::Fn` :t:`trait`, then
   ``core::ops::Fn::call(adjusted_call_operand, argument_operand_tuple)`` is
   invoked.

#. :dp:`fls_9lt4wh9ql5ae`
   If the :t:`type` of the :t:`call operand` implements the
   :std:`core::ops::FnMut` :t:`trait`, then
   ``core::ops::FnMut::call_mut(adjusted_call_operand, argument_operand_tuple)``
   is invoked.

#. :dp:`fls_ixebnlcccmit`
   If the :t:`type` of the :t:`call operand` implements the
   :std:`core::ops::FnOnce` :t:`trait`, then
   ``core::ops::FnOnce::call_once(adjusted_call_operand, argument_operand_tuple)``
   is invoked.

.. rubric:: Undefined Behavior

:dp:`fls_5yeq4oah58dl`
It is undefined behavior to call a :t:`function` with an :t:`ABI` other than the
:t:`ABI` the :t:`function` was defined with.

.. rubric:: Examples

.. code-block:: rust

   let three: i32 = add(1, 2);

.. _fls_z7q8kbjwdc7g:

Method Call Expressions
~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   MethodCallExpression ::=
       ReceiverOperand $$.$$ MethodOperand $$($$ ArgumentOperandList? $$)$$

   ReceiverOperand ::=
       Operand

   MethodOperand ::=
       PathExpressionSegment

.. rubric:: Legality Rules

.. glossary-entry:: method call expression
   :glossary-dp: fls_l4wel2551cw9
   
   :glossary:
     :dp:`fls_367sod24edts`
     A :dt:`method call expression` is an :t:`expression` that invokes a :t:`method`
     of a :t:`variable`.
     
     :dp:`fls_ohhcvxcaqv11`
     See :s:`MethodCallExpression`.
   :chapter:
     :dp:`fls_b7i26954j1hc`
     A :t:`method call expression` is an :t:`expression` that invokes a :t:`method`
     of a :t:`variable`.

.. glossary-entry:: receiver operand
   :glossary-dp: fls_nfb3ciarl50w
   
   :glossary:
     :dp:`fls_odbg4bizvqxq`
     A :dt:`receiver operand` is an :t:`operand` that denotes the :t:`value` whose
     :t:`method` is being invoked by a :t:`method call expression`.
     
     :dp:`fls_4rme1x6romeg`
     See :s:`ReceiverOperand`.
   :chapter:
     :dp:`fls_jx3ryre0xs88`
     A :t:`receiver operand` is an :t:`operand` that denotes the :t:`value` whose
     :t:`method` is being invoked by a :t:`method call expression`.

.. glossary-entry:: method operand
   :glossary-dp: fls_l6eJxvmplLqQ
   
   :glossary:
     :dp:`fls_VLLAFjAxCfkE`
     A :dt:`method operand` is an :t:`operand` that denotes the :t:`method` being
     invoked by a :t:`method call expression`.
     
     :dp:`fls_Pkgr4fJQZpJ6`
     See :s:`MethodOperand`.
   :chapter:
     :dp:`fls_3AQUOBo7akXu`
     A :t:`method operand` is an :t:`operand` that denotes the :t:`method` being
     invoked by a :t:`method call expression`.

:dp:`fls_11glzggtbgb3`
The :t:`type` of a :t:`method call expression` is the :t:`return type` of the
invoked :t:`method`.

:dp:`fls_ljvj1f9fv085`
The :t:`value` of a :t:`method call expression` is the :t:`value` returned by
the invoked :t:`method`.

:dp:`fls_y7bj7y6davlh`
A :t:`method call expression` is subject to :t:`method resolution`.

.. rubric:: Dynamic Semantics

:dp:`fls_oxxk3snd7ya0`
The :t:`evaluation` of a :t:`method call expression` proceeds as follows:

#. :dp:`fls_gmpq15g77o20`
   The :t:`receiver operand` is evaluated.

#. :dp:`fls_pu0n9hakkym2`
   The :t:`[argument operand]s` are evaluated in left-to-right order.

#. :dp:`fls_cawdkgvvd1x6`
   The :t:`method` is invoked.

.. rubric:: Examples

.. code-block:: rust

   trait Command {
       fn execute(&self);
   }

   struct ClickCommand { ... }

   impl ClickCommand for Command {
       fn execute(&self) {
           println!("Someone clicked me!")
       }
   }

   let click = ClickCommand { ... };
   click.execute();

.. _fls_8gPCPVc99pXJ:

Call Conformance
~~~~~~~~~~~~~~~~

:dp:`fls_tsn6SUUG9LvW`
A :t:`method call expression` is equivalent to a :t:`call expression` where the
:t:`call operand` is the resolved :t:`method` and the adjusted
:t:`receiver operand` is prepended to the :t:`[argument operand]s`.

:dp:`fls_c40C6rg6rGv6`
An :t:`argument operand` matches a :t:`function parameter` or :t:`field` of the
:t:`callee type` when its position and the position of the
:t:`function parameter` or :t:`field` are the same. Such an
:t:`argument operand` is a :dt:`matched argument operand`.

:dp:`fls_Gr1ixJ9vFjUm`
The :t:`type` of a :t:`matched argument operand` and the :t:`type` of the
corresponding :t:`function parameter` or :t:`field` shall be :t:`unifiable`.

:dp:`fls_jTMQa6AJSMpE`
The number of :t:`[argument operand]s` shall be equal to the number of
:t:`[field]s` or :t:`[function parameter]s` of the :t:`callee type`.

.. _fls_18k3uajrgq5f:

Field Access Expressions
------------------------

.. rubric:: Syntax

.. syntax::

   FieldAccessExpression ::=
       ContainerOperand $$.$$ FieldSelector

   ContainerOperand ::=
       Operand

   FieldSelector ::=
       IndexedFieldSelector
     | NamedFieldSelector

   IndexedFieldSelector ::=
       DecimalLiteral

   NamedFieldSelector ::=
       Identifier

.. rubric:: Legality Rules

.. glossary-entry:: field access expression
   :glossary-dp: fls_yipl7ajrbs6y
   
   :glossary:
     :dp:`fls_gdl348a04d15`
     A :dt:`field access expression` is an :t:`expression` that accesses a
     :t:`field` of a :t:`value`.
     
     :dp:`fls_luetyuwu54d6`
     See :s:`FieldAccessExpression`.
   :chapter:
     :dp:`fls_hr8qvwlhd9ts`
     A :t:`field access expression` is an :t:`expression` that accesses a :t:`field`
     of a :t:`value`.

.. glossary-entry:: container operand
   :glossary-dp: fls_39s6od9hj4g6
   
   :glossary:
     :dp:`fls_stjmobac6wyd`
     A :dt:`container operand` is an :t:`operand` that indicates the :t:`value`
     whose :t:`field` is selected in a :t:`field access expression`.
     
     :dp:`fls_hgm1ssicc8j4`
     See :s:`ContainerOperand`.
   :chapter:
     :dp:`fls_s2vpn4ihenpe`
     A :t:`container operand` is an :t:`operand` that indicates the :t:`value` whose
     :t:`field` is selected in a :t:`field access expression`.

.. glossary-entry:: field selector
   :glossary-dp: fls_kqbata8slp1y
   
   :glossary:
     :dp:`fls_aq1yg9cp1uof`
     A :dt:`field selector` is a :t:`construct` that selects the :t:`field` to be
     accessed in a :t:`field access expression`.
     
     :dp:`fls_x8swot8e1j32`
     See :s:`FieldSelector`.
   :chapter:
     :dp:`fls_yeuayil6uxzx`
     A :t:`field selector` is a :t:`construct` that selects the :t:`field` to be
     accessed in a :t:`field access expression`.

.. glossary-entry:: indexed field selector
   :glossary-dp: fls_bu46dg60o8us
   
   :glossary:
     :dp:`fls_u6mh5yediub`
     An :dt:`indexed field selector` is a :t:`field selector` where the selected
     :t:`field` is indicated by an index.
     
     :dp:`fls_wbbyf2szc8a7`
     See :s:`IndexedFieldSelector`.

.. glossary-entry:: field index
   :glossary-dp: fls_6uwwat9j4x7y
   
   :glossary:
     :dp:`fls_6061r871qgbj`
     A :dt:`field index` is the position of a :t:`field` within a
     :t:`tuple struct type` or :t:`tuple enum variant`. The first :t:`field` has a
     :t:`field index` of zero, the Nth :t:`field` has a :t:`field index` of N-1.
     
     :dp:`fls_IDYKXUIL845x`
     See :s:`FieldIndex`.

.. glossary-entry:: selected field
   :glossary-dp: fls_rfk06mm3pdxg
   
   :glossary:
     :dp:`fls_8otlvwlqrd4e`
     A :dt:`selected field` is a :t:`field` that is selected by a
     :t:`field access expression`.
   :chapter:
     :dp:`fls_qqrconpa92i3`
     A :t:`selected field` is a :t:`field` that is selected by a
     :t:`field access expression`.

:dp:`fls_fovs9il2h9xg`
The :t:`type` of a :t:`field access expression` is the :t:`type` of the
:t:`selected field`.

:dp:`fls_r1b4n12i93pg`
The :t:`value` of a :t:`field access expression` is the :t:`value` of the
:t:`selected field`.

:dp:`fls_kddnnz8uc15b`
Reading the :t:`selected field` of a :t:`union` shall require
:t:`unsafe context`.

:dp:`fls_an3no949lvfw`
Writing to the :t:`selected field` of a :t:`union` where the :t:`type` of the
:t:`selected field` implements the :std:`core::marker::Copy` :t:`trait` or the
:std:`core::mem::ManuallyDrop` :t:`trait` shall not require :t:`unsafe context`.

:dp:`fls_t6xmsm2nk1bc`
Writing to and then reading from the :t:`selected field` of a :t:`union`
subject to :t:`attribute` :c:`repr` is equivalent to invoking :t:`function`
``core::mem::transmute<write_type, read_type>(field_bits)`` where ``write_type``
is the :t:`type` used at the time of writing the :t:`selected field`,
``read_type`` is the :t:`type` used at the time of reading the
:t:`selected field`, and ``field_bits`` is the bit representation of the
:t:`selected field`.

:dp:`fls_jjnyuU9KIaGy`
A :t:`field access expression` is subject to :t:`field resolution`.

.. rubric:: Undefined Behavior

:dp:`fls_Vani4665hiJY`
It is undefined behavior reading the :t:`selected field` of a
:t:`union type` when it contains data that is invalid for the :t:`selected
field`'s type.

.. rubric:: Dynamic Semantics

:dp:`fls_6uzouesw2sod`
The :t:`evaluation` of a :t:`field access expression` evaluates its
:t:`container operand`.

.. rubric:: Examples

:dp:`fls_x27yayh4z787`
See :p:`fls_vsxsbqps64o` for the declaration of ``alice``.

.. code-block:: rust

   alice.name

:dp:`fls_dimto84ifanr`
The following indexed field access evaluates to ``42``.

.. code-block:: rust

   ("hello", 42i16, true).1

.. _fls_tjyexqrx0fx5:

Closure Expressions
-------------------

.. rubric:: Syntax

.. syntax::

   ClosureExpression ::=
       $$async$$? $$move$$? $$|$$ ClosureParameterList? $$|$$
         (ClosureBody | ClosureBodyWithReturnType)

   ClosureBody ::=
       Expression

   ClosureBodyWithReturnType ::=
       ReturnTypeWithoutBounds BlockExpression

   ReturnTypeWithoutBounds ::=
       $$->$$ TypeSpecificationWithoutBounds

   ClosureParameterList ::=
       ClosureParameter ($$,$$ ClosureParameter)* $$,$$?

   ClosureParameter ::=
       OuterAttributeOrDoc* PatternWithoutAlternation TypeAscription?

.. rubric:: Legality Rules

.. glossary-entry:: closure expression
   :glossary-dp: fls_mrwle2ediywb
   
   :glossary:
     :dp:`fls_x87rhn9ikz00`
     A :dt:`closure expression` is an :t:`expression` that defines a
     :t:`closure type` and constructs a value of that :t:`type`.
     
     :dp:`fls_psd18dkzplf6`
     See :s:`ClosureExpression`.
   :chapter:
     :dp:`fls_2d141c9a0yui`
     A :t:`closure expression` is an :t:`expression` that defines a
     :t:`closure type` and constructs a value of that :t:`type`.

.. glossary-entry:: async closure expression
   :glossary-dp: fls_oUdQnbW1MAFW
   
   :glossary:
     :dp:`fls_SxydbQPPX9Jw`
     An :dt:`async closure expression` is a :t:`closure expression` subject to keyword ``async`` that defines an :t:`async closure type` and constructs a value of that :t:`type`.
     
     :dp:`fls_JZsDFMg85a3u`
     See :s:`ClosureExpression`.
   :chapter:
     :dp:`fls_My6pMgpeFCFg`
     An :t:`async closure expression` is a :t:`closure expression` subject to keyword ``async`` that defines an :t:`async closure type` and constructs a value of that :t:`type`.

.. glossary-entry:: async closure type
   :glossary-dp: fls_Pq4ohvrMOi5p
   
   :glossary:
     :dp:`fls_IT28HJaF8rnm`
     An :dt:`async closure type` is a unique anonymous :t:`function type` that encapsulates
     all :t:`[capture target]s` of a :t:`closure expression` producing a :std:`core::future::Future`.

:dp:`fls_UgJgur0z6d4a`
The :t:`return type` of a :t:`closure type` is determined as follows:

* :dp:`fls_af1WL2mBKMfW`
  If the :t:`closure expression` specifies a :s:`ClosureBodyWithReturnType`, then the :t:`return type` is the specified :s:`ReturnTypeWithoutBounds`.

* :dp:`fls_wLVeE6cNG8oa`
  Otherwise the :t:`return type` is the :t:`type` of the :t:`closure body`.

:dp:`fls_DSy7bPKGzyov`
The :t:`return type` of an :t:`async closure type` is an :t:`anonymous return type` with a :std:`core::future::Future` :t:`trait bound` and a :t:`binding argument` for the ``Output`` :t:`associated type alias` with the actual :t:`return type` of the corresponding :t:`closure type`.

.. glossary-entry:: closure body
   :glossary-dp: fls_5vm5cijnucsr
   
   :glossary:
     :dp:`fls_vgnycw6dykwo`
     A :dt:`closure body` is a :t:`construct` that represents the executable portion
     of a :t:`closure expression`.
     
     :dp:`fls_zefhg4auut8d`
     See :s:`ClosureBody`, :s:`ClosureBodyWithReturnType`.
   :chapter:
     :dp:`fls_srbl7ptknjyk`
     A :t:`closure body` is a :t:`construct` that represents the executable portion
     of a :t:`closure expression`.

:dp:`fls_oey0ivaiu1l`
A :t:`closure body` denotes a new :t:`control flow boundary`.

:dp:`fls_fg8lx0yyt6oq`
A :t:`closure body` is subject to :t:`capturing`.

.. glossary-entry:: closure parameter
   :glossary-dp: fls_f5RBXj9g5iab
   
   :glossary:
     :dp:`fls_yQBZHBLhPswn`
     A :dt:`closure parameter` is a :t:`construct` that yields a set of
     :t:`[binding]s` that bind matched input :t:`[value]s` to :t:`[name]s` at the
     site of a :t:`call expression` or a :t:`method call expression`.
     
     :dp:`fls_Dus3fBU3TwR4`
     See :s:`ClosureParameter`.
   :chapter:
     :dp:`fls_c3rzwUxjmBMY`
     A :t:`closure parameter` is a :t:`construct` that yields a set of
     :t:`[binding]s` that bind matched input :t:`[value]s` to :t:`[name]s` at the
     site of a :t:`call expression` or a :t:`method call expression`.

:dp:`fls_81KOEXwps2HS`
The :t:`type` of a :t:`closure parameter` is determined as follows:

* :dp:`fls_XWJ9SFggdVeH`
  If the :t:`closure parameter` lacks a :s:`TypeSpecification`, the :t:`type` is inferred form the usage of the :t:`closure parameter`.

* :dp:`fls_mPWkIxTJErqx`
  Otherwise the :t:`type` is the specified :t:`type`.

:dp:`fls_r6gWLoNR7JMR`
The :t:`pattern` of a :t:`closure parameter` shall be an
:t:`irrefutable pattern`.

:dp:`fls_zsaTK9snhXs0`
The :t:`expected type` of the :t:`pattern` of a :t:`closure parameter` is the :t:`type` of the :t:`closure parameter`.

:dp:`fls_qPeOL6ZhXsgH`
The :t:`[binding]s` of all :t:`[pattern]s` of all :t:`[closure parameter]s` of a :t:`closure expression` shall not shadow another.

:dp:`fls_yn30xuejcfxo`
The :t:`type` of a :t:`closure expression` is the unique anonymous
:t:`closure type` defined by it.

:dp:`fls_sje6cdvifgv5`
The :t:`value` of a :t:`closure expression` is the :t:`value` of the unique
anonymous :t:`closure type` instantiated with the selected
:t:`[capture target]s`.

.. rubric:: Dynamic Semantics

:dp:`fls_f59fw17gsasn`
The :t:`evaluation` of a :t:`closure expression` proceeds as follows:

#. :dp:`fls_7w15ccc1zzxl`
   An anonymous :t:`value` of an unique anonymous :t:`closure type` is created.

.. rubric:: Examples

.. code-block:: rust

   fn do_ten_times<F>(consumer: F) where F: Fn(i32) {
       for times in 0 .. 10 {
           consumer(times);
       }
   }

   do_ten_times(|value: i32| { println!("value: {}", value)});

.. _fls_rr908hgunja7:

Loop Expressions
----------------

.. rubric:: Syntax

.. syntax::

   LoopExpression ::=
       Label? LoopContent

   Label ::=
       $$'$$ NonKeywordIdentifier $$:$$

   LoopContent ::=
       ForLoopExpression
     | InfiniteLoopExpression
     | WhileLetLoopExpression
     | WhileLoopExpression

   LoopBody ::=
       BlockExpression

.. rubric:: Legality Rules

.. glossary-entry:: loop
   :glossary-dp: fls_kdqa8zs8tk6g
   
   :glossary:
     :dp:`fls_omjnvxva07z2`
     For :dt:`loop`, see :t:`loop expression`.

.. glossary-entry:: loop expression
   :glossary-dp: fls_an1s2hnapd59
   
   :glossary:
     :dp:`fls_2yypq3m1kquj`
     A :dt:`loop expression` is an :t:`expression` that evaluates a
     :t:`block expression` continuously as long as some criterion holds true.
     
     :dp:`fls_o2dyznhq7rez`
     See :s:`LoopExpression`.
   :chapter:
     :dp:`fls_y1d8kd1bdlmx`
     A :t:`loop expression` is an :t:`expression` that evaluates a :t:`block
     expression` continuously as long as some criterion holds true.

.. glossary-entry:: loop body
   :glossary-dp: fls_5vt0Ph5BfDnU
   
   :glossary:
     :dp:`fls_fRWcWPeKgx9g`
     A :dt:`loop body` is the :t:`block expression` of a :t:`loop expression`.
     
     :dp:`fls_vWuR2TET712r`
     See :s:`LoopBody`.
   :chapter:
     :dp:`fls_BjZjuiFnPtFd`
     A :t:`loop body` is the :t:`block expression` of a :t:`loop expression`.

:dp:`fls_XEc0cIkpkyzJ`
The :t:`type` of the :t:`loop body` shall be the :t:`unit type`.

.. glossary-entry:: anonymous loop expression
   :glossary-dp: fls_du8uevac5q7j
   
   :glossary:
     :dp:`fls_csss2a8yk52k`
     An :dt:`anonymous loop expression` is a :t:`loop expression` without a
     :t:`label`.
   :chapter:
     :dp:`fls_eg93m93gvwal`
     An :t:`anonymous loop expression` is a :t:`loop expression` without a
     :t:`label`.

.. glossary-entry:: named loop expression
   :glossary-dp: fls_biwn3hxza37n
   
   :glossary:
     :dp:`fls_440dr5qix3ns`
     A :dt:`named loop expression` is a :t:`loop expression` with a :t:`label`.
   :chapter:
     :dp:`fls_phpoq9ho8f1v`
     A :t:`named loop expression` is a :t:`loop expression` with a :t:`label`.
     
     .. rubric:: Dynamic Semantics

.. glossary-entry:: terminated
   :glossary-dp: fls_ihv02usuziw8
   
   :glossary:
     :dp:`fls_med1l8vheb83`
     A :t:`loop expression` is :dt:`terminated` when its :t:`block expression` is no
     longer evaluated.
   :chapter:
     :dp:`fls_aw6qczl4zpko`
     A :t:`loop expression` is :t:`terminated` when its :t:`block expression` is no
     longer evaluated.

.. _fls_onfyolkcbeh3:

For Loops
~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   ForLoopExpression ::=
       $$for$$ Pattern $$in$$ SubjectExpression LoopBody

.. rubric:: Legality Rules

.. glossary-entry:: for loop
   :glossary-dp: fls_dwnvkq8n94h1
   
   :glossary:
     :dp:`fls_gmhh56arsbw8`
     For :dt:`for loop`, see :t:`for loop expression`.

.. glossary-entry:: for loop expression
   :glossary-dp: fls_vfkqbovqbw86
   
   :glossary:
     :dp:`fls_f0gp7qxoc4o4`
     A :dt:`for loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` as long as its :t:`subject expression` yields a
     :t:`value`.
     
     :dp:`fls_yn4d35pvmn87`
     See :s:`ForLoopExpression`.
   :chapter:
     :dp:`fls_1bh2alh37frz`
     A :t:`for loop expression` is a :t:`loop expression` that continues to evaluate
     its :t:`loop body` as long as its :t:`subject expression` yields a :t:`value`.

:dp:`fls_fkgbin6ydkm4`
The :t:`type` of a :t:`subject expression` shall implement the
:std:`core::iter::IntoIterator` :t:`trait`.

:dp:`fls_fo6Aa6Td6rMA`
The :t:`expected type` of the :t:`pattern` is the :t:`associated type` :std:`core::iter::IntoIterator::Item` of the :t:`subject expression`'s :std:`core::iter::IntoIterator` implementation.

:dp:`fls_bmTjhKdpfgCB`
The :t:`type` of a :t:`for loop expression` is the :t:`unit type`.

:dp:`fls_FkxLf91WKiIo`
The :t:`value` of a :t:`for loop expression` is the :t:`unit value`.

.. rubric:: Dynamic Semantics

:dp:`fls_kuxo0on3vit6`
The :t:`evaluation` of a :t:`for loop expression` of the form

.. code-block:: rust

   'label: for pattern in subject_expression {
       /* loop body */
   }

:dp:`fls_2lrzrtjhsdes`
is equivalent to the :t:`evaluation` of the following :t:`block expression`:

.. code-block:: rust

   {
       let result =
           match core::iter::IntoIterator::into_iter
               (subject_expression)
       {
           mut iter => 'label: loop {
               let mut next_value;
               match core::iter::Iterator::next(&mut iter) {
                   Option::Some(value) => next_value = value,
                   Option::None => break
               };
               let pattern = next_value;
               let () = { /* loop body */ };
           }
       };
       result
   }

.. rubric:: Examples

.. code-block:: rust

   let favorite_fruits = &["apples", "pears", "strawberries"];

   for fruit in favorite_fruits {
       println!("I like eating {}.", fruit);
   }

.. _fls_sf4qnd43z2wc:

Infinite Loops
~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   InfiniteLoopExpression ::=
       $$loop$$ LoopBody

.. rubric:: Legality Rules

.. glossary-entry:: infinite loop
   :glossary-dp: fls_kg9aeyrw822m
   
   :glossary:
     :dp:`fls_xpm53i3rkuu0`
     For :dt:`infinite loop`, see :t:`infinite loop expression`.

.. glossary-entry:: infinite loop expression
   :glossary-dp: fls_o2eei5aqgds6
   
   :glossary:
     :dp:`fls_mvplpa4t1f2p`
     An :dt:`infinite loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` indefinitely.
     
     :dp:`fls_2gipk6b62hme`
     See :s:`InfiniteLoopExpression`.
   :chapter:
     :dp:`fls_p11qw6mtxlda`
     An :t:`infinite loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` indefinitely.

:dp:`fls_b314wjbv0zwe`
The :t:`type` of an :t:`infinite loop expression` is determined as follows:

* :dp:`fls_rpedapxnv8w3`
  If the :t:`infinite loop expression` does not contain a :t:`break expression`,
  then the :t:`type` is the :t:`never type`.

* :dp:`fls_wf11yp1jwf53`
  If the :t:`infinite loop expression` contains at least one
  :t:`break expression`, then the :t:`type` is the :t:`unified type` of the
  :t:`[break type]s` of all :t:`[break expression]s`.

:dp:`fls_q3qpcf2fz7h`
The :t:`value` of an :t:`infinite loop expression` is determined as follows:

* :dp:`fls_2ulbzmuuny3g`
  If the :t:`infinite loop expression` does not contain a :t:`break expression`,
  then the :t:`value` is the :t:`unit value`.

* :dp:`fls_99imks9hj3kp`
  If the :t:`infinite loop expression` contains at least one
  :t:`break expression`, then the :t:`value` is the :t:`break value` of the
  :t:`break expression` that broke out of the :t:`loop expression`.

.. rubric:: Dynamic Semantics

:dp:`fls_w4tj5gofwih1`
The :t:`evaluation` of an :t:`infinite loop expression` proceeds as follows:

#. :dp:`fls_pg3r6nyl865`
   The :t:`block expression` is evaluated.

#. :dp:`fls_lp15ilkul2uv`
   Control restarts the :t:`evaluation` of the :t:`infinite loop expression`.

.. rubric:: Examples

.. code-block:: rust

   loop {
       println!("I am alive!");
   }

.. _fls_5jjm1kt43axd:

While Loops
~~~~~~~~~~~

.. glossary-entry:: while loop
   :glossary-dp: fls_od59yim9kasi
   
   :glossary:
     :dp:`fls_ug9cxoml9ged`
     For :dt:`while loop`, see :t:`while loop expression`.

.. rubric:: Syntax

.. syntax::

   WhileLoopExpression ::=
       $$while$$ IterationExpression LoopBody

   IterationExpression ::=
       SubjectExpression

.. rubric:: Legality Rules

.. glossary-entry:: while loop expression
   :glossary-dp: fls_1qxi3h3qmgso
   
   :glossary:
     :dp:`fls_fq0zyup4djyh`
     A :dt:`while loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
     true.
     
     :dp:`fls_7htwpbmyq83u`
     See :s:`WhileLoopExpression`.
   :chapter:
     :dp:`fls_ajby242tnu7c`
     A :t:`while loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` as long as its :t:`iteration expression` holds
     true.

.. glossary-entry:: iteration expression
   :glossary-dp: fls_orde7iunolyx
   
   :glossary:
     :dp:`fls_suz163n1x1xm`
     An :dt:`iteration expression` is an :t:`expression` that provides the criterion
     of a :t:`while loop expression`.
     
     :dp:`fls_jw5lj2hgjl8v`
     See :s:`IterationExpression`.
   :chapter:
     :dp:`fls_13hmhzqz82v6`
     An :t:`iteration expression` is an :t:`expression` that provides the criterion
     of a :t:`while loop expression`.

:dp:`fls_d7ofrq3777kq`
The :t:`type` of an :t:`iteration expression` shall be :t:`type` :c:`bool`.

:dp:`fls_P8iyTN6KZCVA`
The :t:`type` of a :t:`while loop expression` is the :t:`unit type`.

:dp:`fls_s6hRa5spz64w`
The :t:`value` of a :t:`while loop expression` is the :t:`unit value`.

.. rubric:: Dynamic Semantics

:dp:`fls_1i7hm645h7ox`
The :t:`evaluation` of a :t:`while loop expression` proceeds as follows:

#. :dp:`fls_5x0du3u1jwd3`
   The :t:`iteration expression` is evaluated.

#. :dp:`fls_23uluvhhoct6`
   If the :t:`iteration expression` evaluated to ``true``, then:

   #. :dp:`fls_k7g4cac93617`
      The :t:`block expression` is evaluated.

   #. :dp:`fls_j08k3brdpgno`
      Control restarts the :t:`evaluation` of the :t:`while loop expression`.

.. rubric:: Examples

.. code-block:: rust

   let mut counter = 0;

   while counter < 5 {
       counter += 1;
       println("iteration {}", counter);
   }

.. _fls_m6kd5i9dy8dx:

While Let Loops
~~~~~~~~~~~~~~~

.. glossary-entry:: while let loop
   :glossary-dp: fls_8hcsablipi17
   
   :glossary:
     :dp:`fls_ovutw52qtx71`
     For :dt:`while let loop`, see :t:`while let loop expression`.

.. rubric:: Syntax

.. syntax::

   WhileLetLoopExpression ::=
       $$while$$ $$let$$ Pattern $$=$$ SubjectLetExpression LoopBody

.. rubric:: Legality Rules

.. glossary-entry:: while let loop expression
   :glossary-dp: fls_gme4odk59x6d
   
   :glossary:
     :dp:`fls_g35gn7n88acp`
     A :dt:`while let loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` as long as its :t:`subject let expression` yields a
     :t:`value` that can be matched against its :t:`pattern`.
     
     :dp:`fls_q3jcb4nodqba`
     See :s:`WhileLetLoopExpression`.
   :chapter:
     :dp:`fls_fmdlyp9r9zl7`
     A :t:`while let loop expression` is a :t:`loop expression` that continues to
     evaluate its :t:`loop body` as long as its :t:`subject let expression` yields
     a :t:`value` that can be matched against its :t:`pattern`.

:dp:`fls_bC60ZSC9yUOI`
The :t:`expected type` of the :t:`pattern` is the :t:`type` of the :t:`subject let expression`.

:dp:`fls_gTfSLePwHTES`
The :t:`type` of a :t:`while let loop expression` is the :t:`unit type`.

:dp:`fls_pTq4LIGIoAtN`
The :t:`value` of a :t:`while let loop expression` is the :t:`unit value`.

.. rubric:: Dynamic Semantics

:dp:`fls_z2ht5iaat5ag`
The :t:`evaluation` of a :t:`while let loop expression` of the form

.. code-block:: rust

   'label: let pattern = subject_let_expression {
       /* loop body */
   }

:dp:`fls_pacf1uavh1qt`
shall be equivalent to the :t:`evaluation` the following :t:`infinite loop`:

.. code-block:: rust

   'label: loop {
       match subject_let_expression {
           pattern => { /* loop body */ },
           _ => break
       }
   }

.. rubric:: Examples

.. code-block:: rust

   let mut favorite_animals = vec!["cats", "dogs", "otters"];

   while let Some(animal) = favorite_animals.pop() {
       println!("I like petting {}", animal);
   }

.. _fls_uusi0zej55is:

Loop Labels
~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   LabelIndication ::=
       $$'$$ NonKeywordIdentifier

.. rubric:: Legality Rules

.. glossary-entry:: label
   :glossary-dp: fls_uVUoHmNtPRtS
   
   :glossary:
     :dp:`fls_iAAf2rLmgmGQ`
     A :dt:`label` is the :t:`name` of a :t:`loop expression`.
     
     :dp:`fls_HicurdHIiLX2`
     See :s:`Label`.

.. glossary-entry:: label indication
   :glossary-dp: fls_dw5s7jhk4v8s
   
   :glossary:
     :dp:`fls_sso322p7adt0`
     A :dt:`label indication` is a :t:`construct` that indicates a :t:`label`.
     
     :dp:`fls_g6iqfqooz8th`
     See :s:`LabelIndication`.
   :chapter:
     :dp:`fls_tx5u743391h7`
     A :t:`label indication` is a :t:`construct` that indicates a :t:`label`.

:dp:`fls_7hc8yboeaho0`
A :t:`label indication` shall indicate a :t:`label` of an enclosing
:t:`named block expression` or :t:`named loop expression` that does not pass a
:t:`control flow boundary` in order to reach the enclosing
:t:`named block expression` or :t:`named loop expression`.

.. _fls_jr4tpuyksr75:

Break Expressions
~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   BreakExpression ::=
       $$break$$ LabelIndication? Operand?

.. rubric:: Legality Rules

.. glossary-entry:: break expression
   :glossary-dp: fls_xki2cerozblt
   
   :glossary:
     :dp:`fls_8ys8hlqgizoa`
     A :dt:`break expression` is an :t:`expression` that terminates a
     :t:`loop expression` or a :t:`named block expression`.
     
     :dp:`fls_fd1xpst5fki2`
     See :s:`BreakExpression`.
   :chapter:
     :dp:`fls_i5ko1t2wbgxe`
     A :t:`break expression` is an :t:`expression` that terminates a
     :t:`loop expression` or a :t:`named block expression`.

:dp:`fls_jiykbp51909f`
A :t:`break expression` shall appear within a :t:`loop body` or a
:t:`named block expression`.

:dp:`fls_gnupTkuafKNi`
If a :t:`break expression` appears within a :t:`named block expression`, then
the :t:`break expression` shall have a :t:`label indication`.

:dp:`fls_7frvr2nm2mcj`
The :t:`label indication` of a :t:`break expression` shall resolve to the
:t:`label` of an enclosing :t:`named block expression` or
:t:`named loop expression`.

:dp:`fls_54d5uydc87td`
A :t:`break expression` with a :t:`label indication` is associated with the
:t:`named block expression` or :t:`named loop expression` whose :t:`label` is
indicated by the :t:`label indication`.

:dp:`fls_ghxns2nggffj`
A :t:`break expression` without a :t:`label indication` is associated with the
innermost enclosing :t:`loop expression`.

:dp:`fls_3hI7FU42sVyX`
If a :t:`break expression` appears within a :t:`loop expression`, then the
:t:`break expression` shall have an :t:`operand` only when it is associated
with an :t:`infinite loop`.

:dp:`fls_dnnq1zym8ii0`
The :t:`type` of a :t:`break expression` is the :t:`never type`.

.. glossary-entry:: break type
   :glossary-dp: fls_ff2zt3ww2yw3
   
   :glossary:
     :dp:`fls_jvm1vsqmslxn`
     :dt:`Break type` is the :t:`type` of the :t:`operand` of a
     :t:`break expression`.
   :chapter:
     :dp:`fls_1wdybpfldj7q`
     :t:`Break type` is the :t:`type` of the :t:`operand` of a :t:`break expression`.

:dp:`fls_8yore99adr22`
The :t:`break type` is determined as follows:

* :dp:`fls_60imbzwg3e2x`
  If the :t:`break expression` lacks an :t:`operand`, then the :t:`break type`
  is the :t:`unit type`.

* :dp:`fls_l0c05wa9q97w`
  If the :t:`break expression` has an :t:`operand`, then the :t:`break type` is
  the :t:`type` of its :t:`operand`.

.. glossary-entry:: break value
   :glossary-dp: fls_owtptuvleeb
   
   :glossary:
     :dp:`fls_kpka4jf2qr5l`
     :dt:`Break value` is the :t:`value` of the :t:`operand` of a
     :t:`break expression`.
   :chapter:
     :dp:`fls_bgd7d5q69q0g`
     :t:`Break value` is the :t:`value` of the :t:`operand` of a
     :t:`break expression`.

:dp:`fls_yb8jv4mkmki0`
The :t:`break value` is determined as follows:

* :dp:`fls_d7l1y2qbe8br`
  If the :t:`break expression` lacks an :t:`operand`, then the :t:`break value`
  is the :t:`unit value`.

* :dp:`fls_56szfyilc06`
  If the :t:`break expression` has an :t:`operand`, then the :t:`break value` is
  the :t:`value` of its :t:`operand`.

.. rubric:: Dynamic Semantics

:dp:`fls_jnpx8mx1oa7n`
If a :t:`break expression` appears within a :t:`loop expression`, then the
:t:`evaluation` of the :t:`break expression` proceeds as follows:

#. :dp:`fls_l2kp8mw6bjj0`
   The :t:`operand` is evaluated.

#. :dp:`fls_2nmadhe3ismj`
   All enclosing :t:`[loop expression]s` upto and including the associated
   :t:`loop expression` are :t:`terminated`.

:dp:`fls_XpFLrL78QMe1`
If a :t:`break expression` appears within a :t:`named block expression`, then
the :t:`evaluation` of the :t:`break expression` proceeds as follows:

#. :dp:`fls_WFAW1PG1YXdM`
   The :t:`operand` is evaluated.

#. :dp:`fls_AurifMM8RpDp`
   All enclosing :t:`[named block expression]s` upto and including the
   associated :t:`named block expression` are terminated.

.. rubric:: Examples

:dp:`fls_32fwis9pxh77`
The following break expression terminates both the inner and the outer loop.

.. code-block:: rust

   'outer: loop {
       'inner: loop {
           break 'outer;
       }
   }

.. _fls_sjwrlwvpulp:

Continue Expressions
~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   ContinueExpression ::=
       $$continue$$ LabelIndication?

.. glossary-entry:: continue expression
   :glossary-dp: fls_doazu99vos8x
   
   :glossary:
     :dp:`fls_waxam3m9plfj`
     A :dt:`continue expression` is an :t:`expression` that first terminates and
     then restarts a :t:`loop expression`.
     
     :dp:`fls_smwcz2xw9o1f`
     See :s:`ContinueExpression`.

.. rubric:: Legality Rules

:dp:`fls_wzs6kz9ffqzt`
A :t:`continue expression` shall appear within a :t:`loop expression`.

:dp:`fls_r5ke7b9n7k3s`
A :t:`continue expression` without a :t:`label indication` is associated with
the innermost enclosing :t:`loop expression`.

:dp:`fls_ckm6i9c3s6j8`
A :t:`continue expression` with a :t:`label indication` is associated with a
:t:`named loop expression` whose :t:`label` is indicated by the
:t:`label indication`.

:dp:`fls_d0bmw8xiw5nk`
The :t:`type` of a :t:`continue expression` is the :t:`never type`.

.. rubric:: Dynamic Semantics

:dp:`fls_vmyuuptfnwek`
The :t:`evaluation` of a :t:`continue expression` proceeds as follows:

#. :dp:`fls_gm74eo754rq9`
   If the :t:`continue expression` appears with a :t:`label indication`, then
   all enclosing :t:`[loop expression]s` upto and including the associated
   :t:`loop expression` are :t:`terminated`.

#. :dp:`fls_gvuesa5ekeif`
   The :t:`evaluation` of the associated :t:`loop expression` is restarted.

.. rubric:: Examples

:dp:`fls_767gv7zhqamh`
The following continue expression terminates and restarts ``game_loop``.

.. code-block:: rust

   'game_loop: loop {
       if is_paused() {
           continue;
       }
       . . .
   }

.. _fls_18swodqqzadj:

Range Expressions
-----------------

.. rubric:: Syntax

.. syntax::

   RangeExpression ::=
       RangeFromExpression
     | RangeFromToExpression
     | RangeFullExpression
     | RangeInclusiveExpression
     | RangeToExpression
     | RangeToInclusiveExpression

   RangeFromExpression ::=
       RangeExpressionLowBound $$..$$

   RangeFromToExpression ::=
       RangeExpressionLowBound $$..$$ RangeExpressionHighBound

   RangeFullExpression ::=
       $$..$$

   RangeInclusiveExpression ::=
       RangeExpressionLowBound $$..=$$ RangeExpressionHighBound

   RangeToExpression ::=
       $$..$$ RangeExpressionHighBound

   RangeToInclusiveExpression ::=
       $$..=$$ RangeExpressionHighBound

   RangeExpressionLowBound ::=
       Operand

   RangeExpressionHighBound ::=
       Operand

.. rubric:: Legality Rules

.. glossary-entry:: range expression
   :glossary-dp: fls_tbvugpuvcluj
   
   :glossary:
     :dp:`fls_bffrbucfwu7`
     A :dt:`range expression` is an :t:`expression` that constructs a range.
     
     :dp:`fls_1jk43yvxa8ks`
     See :s:`RangeExpression`.
   :chapter:
     :dp:`fls_bi82rusji8g0`
     A :t:`range expression` is an :t:`expression` that constructs a range.

.. glossary-entry:: full range expression
   :glossary-dp: fls_tWp1PLe8m83K
   
   :glossary:
     :dp:`fls_NIb9UOIRjMqa`
     A :dt:`full range expression` is a :t:`range expression` that covers the full
     range of a :t:`type`.

.. glossary-entry:: range expression low bound
   :glossary-dp: fls_smvgd160eynr
   
   :glossary:
     :dp:`fls_t10o1p950u00`
     A :dt:`range expression low bound` is an :t:`operand` that specifies the start
     of a range.
     
     :dp:`fls_vmb2z7oh6gzm`
     See :s:`RangeExpressionLowBound`.
   :chapter:
     :dp:`fls_msyv4oyk5zp9`
     A :t:`range expression low bound` is an :t:`operand` that specifies the start of
     a range.

.. glossary-entry:: range expression high bound
   :glossary-dp: fls_mdvdxr6u13fw
   
   :glossary:
     :dp:`fls_c70pj8w15nmc`
     A :dt:`range expression high bound` is an :t:`operand` that specifies the end
     of a range.
     
     :dp:`fls_yxem0ckicxav`
     See :s:`RangeExpressionHighBound`.
   :chapter:
     :dp:`fls_f648uuxxh4vk`
     A :t:`range expression high bound` is an :t:`operand` that specifies the end of
     a range.

:dp:`fls_9pl4629t54yq`
If a :t:`range expression` has two :t:`[operand]s`, then the :t:`[type]s` of the
:t:`[operand]s` shall be :t:`unifiable`.

.. glossary-entry:: range-from expression
   :glossary-dp: fls_iqpxlg7w3cvf
   
   :glossary:
     :dp:`fls_6enyv2oa4abq`
     A :dt:`range-from expression` is a :t:`range expression` that specifies an
     included :t:`range expression low bound`.
     
     :dp:`fls_e1smn0b478ik`
     See :s:`RangeFromExpression`.
   :chapter:
     :dp:`fls_xaumwogwbv3g`
     A :t:`range-from expression` is a :t:`range expression` that specifies an
     included :t:`range expression low bound`.

:dp:`fls_exa2ufugnpgc`
The :t:`type` of a :t:`range-from expression` is :std:`core::ops::RangeFrom`.

:dp:`fls_jqy0p155btca`
The :t:`value` of a :t:`range-from expression` is
``core::ops::RangeFrom { start: range_expression_low_bound }``.

.. glossary-entry:: range-from-to expression
   :glossary-dp: fls_125h4p4zt86q
   
   :glossary:
     :dp:`fls_nzf6y64jz83f`
     A :dt:`range-from-to expression` is a :t:`range expression` that specifies an
     included :t:`range expression low bound` and an excluded
     :t:`range expression high bound`.
     
     :dp:`fls_mjbxfjulryt`
     See :s:`RangeFromToExpression`.
   :chapter:
     :dp:`fls_ppustuqdji7b`
     A :t:`range-from-to expression` is a :t:`range expression` that specifies an
     included :t:`range expression low bound` and an excluded
     :t:`range expression high bound`.

:dp:`fls_ke2fpgodq84u`
The :t:`type` of a :t:`range-from-to expression` is :std:`core::ops::Range`.

:dp:`fls_zb6jk6qykun6`
The :t:`value` of a :t:`range-from-to expression` is
``core::ops::Range { start: range_expression_low_bound, end: range_expression_high_bound }``.

.. glossary-entry:: range-full expression
   :glossary-dp: fls_8z8nrblarxrv
   
   :glossary:
     :dp:`fls_6mchm7kb7i41`
     A :dt:`range-full expression` is a :t:`range expression` that covers the whole
     range of a :t:`type`.
     
     :dp:`fls_u7kd8w5g2icd`
     See :s:`RangeFullExpression`.
   :chapter:
     :dp:`fls_x67xo25n0qlz`
     A :t:`range-full expression` is a :t:`range expression` that covers the whole
     range of a :t:`type`.

:dp:`fls_m6n0gvg3ct1b`
The :t:`type` of a :t:`range-full expression` is :std:`core::ops::RangeFull`.

:dp:`fls_yvh5cdgzevni`
The :t:`value` of a :t:`range-full expression` is ``core::ops::RangeFull {}``.

.. glossary-entry:: range-inclusive expression
   :glossary-dp: fls_tie80ejz8s19
   
   :glossary:
     :dp:`fls_9vja0wev84a7`
     A :dt:`range-inclusive expression` is a :t:`range expression` that specifies an
     included :t:`range expression low bound` and an included
     :t:`range expression high bound`.
     
     :dp:`fls_lpcsb8dtldk3`
     See :s:`RangeInclusiveExpression`.
   :chapter:
     :dp:`fls_lh9my7g8oflq`
     A :t:`range-inclusive expression` is a :t:`range expression` that specifies an
     included :t:`range expression low bound` and an included
     :t:`range expression high bound`.

:dp:`fls_livflk52xaj9`
The :t:`type` of a :t:`range-inclusive expression` is
:std:`core::ops::RangeInclusive`.

:dp:`fls_vj213j9bj61y`
The :t:`value` of a :t:`range-inclusive expression` is
``core::ops::RangeInclusive::new(range_expression_low_bound, range_expression_high_bound)``.

.. glossary-entry:: range-to expression
   :glossary-dp: fls_etvgkb8zcfpd
   
   :glossary:
     :dp:`fls_urnfp1j9d5v4`
     A :dt:`range-to expression` is a :t:`range expression` that specifies an
     excluded :t:`range expression high bound`.
     
     :dp:`fls_lft9cd7h8cfv`
     See :s:`RangeToExpression`.
   :chapter:
     :dp:`fls_5a1uivj19kob`
     A :t:`range-to expression` is a :t:`range expression` that specifies an excluded
     :t:`range expression high bound`.

:dp:`fls_k611yoc8hk0n`
The :t:`type` of a :t:`range-to expression` is :std:`core::ops::RangeTo`.

:dp:`fls_m0slikrulnvd`
The :t:`value` of a :t:`range-to expression` is
``core::ops::RangeTo { end: range_expression_high_bound }``.

.. glossary-entry:: range-to-inclusive expression
   :glossary-dp: fls_ap5754dfltt5
   
   :glossary:
     :dp:`fls_t4fjanjvkd69`
     A :dt:`range-to-inclusive expression` is a :t:`range expression` that specifies
     an included :t:`range expression high bound`.
     
     :dp:`fls_krei7lc6lo8q`
     See :s:`RangeToInclusiveExpression`.
   :chapter:
     :dp:`fls_1gc436ee1nzm`
     A :t:`range-to-inclusive expression` is a :t:`range expression` that specifies
     an included :t:`range expression high bound`.

:dp:`fls_8sfjw83irpre`
The :t:`type` of a :t:`range-to-inclusive expression` is
:std:`core::ops::RangeToInclusive`.

:dp:`fls_5xw4opkbxhsc`
The :t:`value` of a :t:`range-to-inclusive expression` is
``core::ops::RangeToInclusive { end: range_expression_high_bound }``.

.. rubric:: Dynamic Semantics

:dp:`fls_ehseim1p479z`
The :t:`evaluation` of a :t:`range expression` evaluates its :t:`[operand]s` in
left-to-right order.

.. rubric:: Examples

.. code-block:: rust

   1 ..
   42 .. 86
   ..
   dawn ..= dusk
   ..= 5

.. _fls_nlzksiu8y3z9:

If and If Let Expressions
-------------------------

.. _fls_mkut7gut49gi:

If Expressions
~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   IfExpression ::=
       $$if$$ SubjectExpression BlockExpression ElseExpression?

   ElseExpression ::=
       $$else$$ (BlockExpression | IfExpression | IfLetExpression)

.. rubric:: Legality Rules

.. glossary-entry:: if expression
   :glossary-dp: fls_al9gtcy5b5og
   
   :glossary:
     :dp:`fls_rk0661mtdvsi`
     An :dt:`if expression` is an :t:`expression` that evaluates either a
     :t:`block expression` or an :t:`else expression` depending on the :t:`value`
     of its :t:`subject expression`.
     
     :dp:`fls_gdsufx2ns8bl`
     See :s:`IfExpression`.
   :chapter:
     :dp:`fls_2i4fbxbbvpf1`
     An :t:`if expression` is an :t:`expression` that evaluates either a
     :t:`block expression` or an :t:`else expression` depending on the :t:`value` of
     its :t:`subject expression`.

.. glossary-entry:: else expression
   :glossary-dp: fls_ff5zp7m9d5ot
   
   :glossary:
     :dp:`fls_inp7luoqkjc5`
     An :dt:`else expression` is an :t:`expression` that represents either a
     :t:`block expression`, an :t:`if expression`, or an :t:`if let expression`.
     
     :dp:`fls_2jniy6bkq1hn`
     See :s:`ElseExpression`.
   :chapter:
     :dp:`fls_5azwlk7hav1k`
     An :t:`else expression` is an :t:`expression` that represents either a
     :t:`block expression`, an :t:`if expression`, or an :t:`if let expression`.

:dp:`fls_r7gzxo16esri`
The :t:`type` of the :t:`subject expression` of an :t:`if expression` shall be
:t:`type` :c:`bool`.

:dp:`fls_iv9t4nfs4f6w`
The :t:`type` of an :t:`if expression` is the :t:`type` of its
:t:`block expression`.

:dp:`fls_i9sxf2q5jjqt`
The :t:`value` of an :t:`if expression` is the :t:`value` of its
:t:`block expression`.

:dp:`fls_1e8qer6bh2f3`
The :t:`type` of an :t:`else expression` is the :t:`type` of its
:t:`block expression`, :t:`if expression`, or :t:`if let expression`.

:dp:`fls_p5pjxk5xfcbx`
The :t:`value` of an :t:`else expression` is the :t:`value` of its
:t:`block expression`, :t:`if expression`, or :t:`if let expression`.

:dp:`fls_mpq7gicosgkt`
The :t:`type` of an :t:`if expression` and the :t:`type` of an
:t:`else expression` shall be :t:`unifiable`.

.. rubric:: Dynamic Semantics

:dp:`fls_yhlyzef9h97q`
The :t:`evaluation` of an :t:`if expression` proceeds as follows:

#. :dp:`fls_w7lq4dkoyuf7`
   The :t:`subject expression` is evaluated.

#. :dp:`fls_5udx9zyeg5ga`
   If the :t:`subject expression` evaluated to ``true``, then the
   :t:`block expression` is evaluated.

#. :dp:`fls_67l4j48n6p7o`
   If the :t:`subject expression` evaluated to ``false`` and the
   :t:`if expression` has an :t:`else expression`, then the :t:`else expression`
   is evaluated.

:dp:`fls_e8gd5lzcaifw`
The :t:`evaluation` of an :t:`else expression` evaluates its
:t:`block expression`, :t:`if expression`, or :t:`if let expression`.

.. rubric:: Examples

.. code-block:: rust

   if age <= 14 {
       println!("child");
   } else if age <= 24 {
       println!("youth");
   } else if age <=64 {
       println!("adult");
   } else {
       println!("senior");
   }

.. _fls_p0t1ch115tra:

If Let Expressions
~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   IfLetExpression ::=
       $$if$$ $$let$$ Pattern $$=$$ SubjectLetExpression BlockExpression
         ElseExpression?

.. rubric:: Legality Rules

.. glossary-entry:: if let expression
   :glossary-dp: fls_j9wb2wtqp5u8
   
   :glossary:
     :dp:`fls_ky6ng7jy1g6z`
     An :dt:`if let expression` is an :t:`expression` that evaluates either a
     :t:`block expression` or an :t:`else expression` depending on whether its
     :t:`pattern` can be matched against its :t:`subject let expression`.
     
     :dp:`fls_kczg3c6n3psu`
     See :s:`IfLetExpression`.
   :chapter:
     :dp:`fls_dsrjup2umr9`
     An :t:`if let expression` is an :t:`expression` that evaluates either a
     :t:`block expression` or an :t:`else expression` depending on whether its
     :t:`pattern` can be matched against its :t:`subject let expression`.

:dp:`fls_okVOYzTT6fBK`
The :t:`expected type` of the :t:`pattern` is the :t:`type` of the :t:`subject let expression`.

:dp:`fls_4vyrufo4qdeg`
The :t:`type` of an :t:`if let expression` is the :t:`type` of its
:t:`block expression`.

:dp:`fls_qfnwwvzxsl3`
The :t:`value` of an :t:`if let expression` is the :t:`value` of its
:t:`block expression`.

:dp:`fls_lEr4iqwdBcbA`
The :t:`type` of an :t:`if let expression` and the :t:`type` of an
:t:`else expression` shall be :t:`unifiable`.

.. rubric:: Dynamic Semantics

:dp:`fls_ijo73wtz1sy`
The :t:`evaluation` of an :t:`if let expression` of the form

.. code-block:: rust

   if let pattern = subject_let_expression {
       /* body */
   }

:dp:`fls_qeho5iqiy59`
is equivalent to the :t:`evaluation` of the following :t:`match expression`:

.. code-block:: rust

   match subject_let_expression {
       pattern => { /* body */ },
       _ => ()
   }

:dp:`fls_nhngr8y850dt`
The :t:`evaluation` of an :t:`if let expression` of the form

.. code-block:: rust

   if let pattern = subject_let_expression {
       /* body */
   } else {
       /* else */
   }

:dp:`fls_8fg2ufaxjkv5`
is equivalent to the :t:`evaluation` of the following :t:`match expression`:

.. code-block:: rust

   match subject_let_expression {
       pattern => { /* body */ },
       _ => { /* else */ }
   }

.. rubric:: Examples

.. code-block:: rust

   let dish = ("Ham", "Eggs");

   if let ("Ham", side) = dish {
       println!("Ham is served with {}", side);
   }

.. _fls_e5td0fa92fay:

Match Expressions
-----------------

.. rubric:: Syntax

.. syntax::

   MatchExpression ::=
       $$match$$ SubjectExpression $${$$
         InnerAttributeOrDoc*
         MatchArmList?
       $$}$$

   MatchArmList ::=
       IntermediateMatchArm* FinalMatchArm

   IntermediateMatchArm ::=
       MatchArmMatcher $$=>$$
         $$($$ ExpressionWithBlock $$,$$? | ExpressionWithoutBlock $$,$$ $$)$$

   FinalMatchArm ::=
       MatchArmMatcher $$=>$$ Operand $$,$$?

   MatchArmMatcher ::=
       OuterAttributeOrDoc* Pattern MatchArmGuard?

   MatchArmGuard ::=
       $$if$$ Operand

.. rubric:: Legality Rules

.. glossary-entry:: match expression
   :glossary-dp: fls_w15uouo0sjao
   
   :glossary:
     :dp:`fls_2ohrphptjny6`
     A :dt:`match expression` is an :t:`expression` that tries to match one of
     its multiple :t:`[pattern]s` against its :t:`subject expression` and if it
     succeeds, evaluates an :t:`operand`.
     
     :dp:`fls_wkalvzkmp95y`
     See :s:`MatchExpression`.
   :chapter:
     :dp:`fls_ei4pbeksd1v8`
     A :t:`match expression` is an :t:`expression` that tries to match one of its
     multiple :t:`[pattern]s` against its :t:`subject expression` and if it succeeds,
     evaluates an :t:`operand`.

.. glossary-entry:: match arm
   :glossary-dp: fls_fizf1byuspv2
   
   :glossary:
     :dp:`fls_z5qsy5z2zak3`
     A :dt:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
     and a :t:`match arm body`.
   :chapter:
     :dp:`fls_l45i24ikfavm`
     A :t:`match arm` is a :t:`construct` that consists of a :t:`match arm matcher`
     and a :t:`match arm body`.

.. glossary-entry:: intermediate match arm
   :glossary-dp: fls_7rj914fhginh
   
   :glossary:
     :dp:`fls_l6pemxmdllvl`
     An :dt:`intermediate match arm` is any :t:`non-[final match arm]` of a
     :t:`match expression`.
     
     :dp:`fls_8713j5lrwqvs`
     See :s:`IntermediateMatchArm`.
   :chapter:
     :dp:`fls_d9gerg12hm2d`
     An :t:`intermediate match arm` is any :t:`non-[final match arm]` of a
     :t:`match expression`.

.. glossary-entry:: final match arm
   :glossary-dp: fls_mj9mmkar8c6f
   
   :glossary:
     :dp:`fls_btoz8jioisx9`
     A :dt:`final match arm` is the last :t:`match arm` of a :t:`match expression`.
     
     :dp:`fls_v7ockjwbeel1`
     See :s:`FinalMatchArm`.
   :chapter:
     :dp:`fls_oj8dg28xw5yp`
     A :t:`final match arm` is the last :t:`match arm` of a :t:`match expression`.

.. glossary-entry:: match arm matcher
   :glossary-dp: fls_i3omadaygum2
   
   :glossary:
     :dp:`fls_paz9358w4cpu`
     A :dt:`match arm matcher` is a :t:`construct` that consists of a :t:`pattern`
     and a :t:`match arm guard`.
     
     :dp:`fls_j7i2bjvzz1tx`
     See :s:`MatchArmMatcher`.
   :chapter:
     :dp:`fls_lrdrtedyz28i`
     A :t:`match arm matcher` is a :t:`construct` that consists of a :t:`pattern` and
     a :t:`match arm guard`.

:dp:`fls_zJQ4LecT1HYd`
The :t:`expected type` of the :t:`pattern` of the :t:`match arm matcher` is the :t:`type` of the :t:`subject expression`.

.. glossary-entry:: match arm body
   :glossary-dp: fls_q7lcdtxuy1ac
   
   :glossary:
     :dp:`fls_33e7oefx0xqm`
     A :dt:`match arm body` is the :t:`operand` of a :t:`match arm`.
   :chapter:
     :dp:`fls_8wjdichfxp0y`
     A :t:`match arm body` is the :t:`operand` of a :t:`match arm`.

.. glossary-entry:: match arm guard
   :glossary-dp: fls_aa1x6ajl4zid
   
   :glossary:
     :dp:`fls_uhn07jmvv9ea`
     A :dt:`match arm guard` is a :t:`construct` that provides additional filtering
     to a :t:`match arm matcher`.
     
     :dp:`fls_ykf70vbng54n`
     See :s:`MatchArmGuard`.
   :chapter:
     :dp:`fls_hs1rr54hu18w`
     A :t:`match arm guard` is a :t:`construct` that provides additional filtering to
     a :t:`match arm matcher`.

:dp:`fls_RPMOAaZ6lflI`
:t:`[Binding]s` introduced in the :t:`pattern` of a :t:`match arm matcher` are
:t:`immutable` in the :t:`match arm guard`.

:dp:`fls_knv1affr2o8t`
The :t:`type` of the :t:`subject expression` and the :t:`[type]s` of all
:t:`[pattern]s` of all :t:`[match arm matcher]s` shall be :t:`unifiable`.

:dp:`fls_bzhz5wjd90ii`
The :t:`type` of the :t:`operand` of a :t:`match arm guard` shall be :t:`type`
:c:`bool`.

:dp:`fls_17ag0wzdbxv6`
The :t:`[type]s` of all :t:`match arm bodies <match arm body>` shall be
:t:`unifiable`.

:dp:`fls_5w964phrru82`
The :t:`type` of a :t:`match expression` is the :t:`unified type` of the
:t:`[type]s` of the :t:`[operand]s` of all :t:`[match arm]s`.

:dp:`fls_g6xyz0beps3o`
A :t:`match arm` is selected when its :t:`pattern` matches the
:t:`value` of the :t:`subject expression` and its :t:`match arm guard` (if any) evaluates to
``true``.

:dp:`fls_8dba4o5qg8js`
:t:`Match arm` selection happens in declarative order.

:dp:`fls_e02um1gb89d0`
The :t:`[pattern]s` of all :t:`[match arm]s` taken together shall exhaustively
match the :t:`[subject expression]'s` :t:`type`.

:dp:`fls_4sh2yrslszvb`
The :t:`value` of a :t:`match expression` is the :t:`value` of the :t:`operand`
of the selected :t:`match arm`.

.. rubric:: Dynamic Semantics

:dp:`fls_g551l8r8yh6d`
The :t:`evaluation` of a :t:`match expression` proceeds as follows:

#. :dp:`fls_y44jzkbv74bv`
   The :t:`subject expression` is evaluated.

#. :dp:`fls_jwxykea99psw`
   Each :t:`match arm` is evaluated in declarative order as follows:

   #. :dp:`fls_pgulnjeoxwtj`
      The :t:`match arm matcher` of the :t:`match arm` is evaluated.

   #. :dp:`fls_2dg7wl68z7ar`
      If the :t:`match arm matcher` succeeds, then

      #. :dp:`fls_yv11febo0kyb`
         The :t:`operand` of the :t:`match arm` is evaluated.

      #. :dp:`fls_mvi9z1x836qu`
         Control stops the :t:`evaluation` of the :t:`match expression`.

   #. :dp:`fls_81nnizrxgrsm`
      Otherwise control proceeds with the :t:`evaluation` of the next
      :t:`match arm`.

:dp:`fls_4dv7x9nh2h4e`
The :t:`evaluation` of a :t:`match arm matcher` proceeds as follows:

#. :dp:`fls_k7kliy101m0f`
   The :t:`pattern` of the :t:`match arm matcher` is evaluated.

#. :dp:`fls_k68zkb6jv0vz`
   If the :t:`pattern` succeeds, then

   #. :dp:`fls_gbb6wbmher5z`
      If the :t:`match arm matcher` has a :t:`match arm guard`, then

      #. :dp:`fls_jl4av757yx8j`
         The :t:`match arm guard` is evaluated.

      #. :dp:`fls_wkh5wztauwhu`
         If the :t:`match arm guard` evaluates to ``true``, then the
         :t:`match arm matcher` succeeds.

   #. :dp:`fls_f5f0x8jstp1g`
      Otherwise the :t:`match arm matcher` fails.

#. :dp:`fls_yk8l9zjh7i0d`
   Otherwise the :t:`match arm matcher` fails.

:dp:`fls_sbtx1l6n2tp2`
The :t:`evaluation` of a :t:`match arm guard` evaluates its :t:`operand`. A
:t:`match arm guard` evaluates to ``true`` when its :t:`operand` evaluates to
``true``, otherwise it evaluates to ``false``.

.. rubric:: Examples

.. code-block:: rust

   fn quantify(number_of_things: i32) {
       match number_of_things {
           0 | 1 => println!("not many"),
           2 ..= 9 => println!("a few"),
           _ if number_of_things < 0 => println!("you owe me"),
           _ => println!("lots")
       }
   }

.. _fls_8l74abhlxzdl:

Return Expressions
------------------

.. rubric:: Syntax

.. syntax::

   ReturnExpression ::=
       $$return$$ Expression?

.. rubric:: Legality Rules

.. glossary-entry:: return expression
   :glossary-dp: fls_7tl9qo8yj8xh
   
   :glossary:
     :dp:`fls_vnupfc6s0s7b`
     A :dt:`return expression` is an :t:`expression` that optionally yields a
     :t:`value` and causes control flow to return to the caller.
     
     :dp:`fls_phd8zrsyuzu7`
     See :s:`ReturnExpression`.
   :chapter:
     :dp:`fls_u7jk4j8gkho`
     A :t:`return expression` is an :t:`expression` that optionally yields a
     :t:`value` and causes control flow to return to the end of the enclosing
     :t:`control flow boundary`.

:dp:`fls_5v3j5ghhw8j8`
A :t:`return expression` shall appear within a :t:`control flow boundary`.

:dp:`fls_7Ck4LMQMeQCv`
The :t:`type` of a :t:`return expression` is the :t:`never type`.

:dp:`fls_r610t5vsi7bx`
The :t:`value` returned by a :t:`return expression` is determined as follows:

* :dp:`fls_njndlx2rps2k`
  If the :t:`return expression` has an :t:`operand`, then the :t:`value` is the
  :t:`value` of the :t:`operand`.

* :dp:`fls_tjksia7prao1`
  If the :t:`return expression` does not have an :t:`operand`, then the
  :t:`value` is the :t:`unit value`.

.. rubric:: Dynamic Semantics

:dp:`fls_bqmwlona6l5w`
The :t:`evaluation` of a :t:`return expression` proceeds as follows:

#. :dp:`fls_d9avvfi548t7`
   If the :t:`return expression` has an :t:`operand`, then

   #. :dp:`fls_o3fc1z2mn8zc`
      The :t:`operand` is evaluated.

   #. :dp:`fls_bbf54ukld7j9`
      The :t:`value` of the :t:`operand` is :t:`passed <passing convention>`
      :t:`by move` into the designated output location of the enclosing
      :t:`control flow boundary`.

#. :dp:`fls_99ea30a5mulj`
   Control destroys the current activation frame.

#. :dp:`fls_ubwj8uj6sbgt`
   Control is transferred to the caller frame.

.. rubric:: Examples

.. code-block:: rust

   fn max(left: i32, right: i32) -> i32 {
       if left > right {
           return left;
       }
       return right;
   }

.. _fls_hyrbmfmf6r8g:

Await Expressions
-----------------

.. rubric:: Syntax

.. syntax::

   AwaitExpression ::=
       FutureOperand $$.$$ $$await$$

   FutureOperand ::=
       Operand

.. rubric:: Legality Rules

.. glossary-entry:: await expression
   :glossary-dp: fls_n4oo89apywk4
   
   :glossary:
     :dp:`fls_psbc3b8pec47`
     An :dt:`await expression` is an :t:`expression` that polls a :t:`future`,
     suspending the execution of the future until the future is ready.
     
     :dp:`fls_29gkp9bpo1hi`
     See :s:`AwaitExpression`.
   :chapter:
     :dp:`fls_sjz5s71hwm7l`
     An :t:`await expression` is an :t:`expression` that polls a :t:`future`,
     suspending the :t:`execution` of the :t:`future` until the :t:`future` is ready.

.. glossary-entry:: future operand
   :glossary-dp: fls_dvk8ccb46abk
   
   :glossary:
     :dp:`fls_fold1inh5jev`
     A :dt:`future operand` is an :t:`operand` whose :t:`future` is being awaited by
     an :t:`await expression`.
     
     :dp:`fls_tbfpowv90u5w`
     See :s:`FutureOperand`.
   :chapter:
     :dp:`fls_vhchgab59jvd`
     A :t:`future operand` is an :t:`operand` whose :t:`future` is being awaited by
     an :t:`await expression`.

:dp:`fls_k9pncajmhgk1`
An :t:`await expression` shall appear within an
:t:`async control flow boundary`. Only the innermost :t:`control flow boundary`
shall be considered.

:dp:`fls_9uw5pd7kbrx3`
The :t:`type` of a :t:`future operand` shall implement the
:std:`core::future::IntoFuture` :t:`trait`.

:dp:`fls_c6mxfzef2qop`
The :t:`type` of an :t:`await expression` is
``<_ as core::future::IntoFuture>::Output``.

:dp:`fls_l396mo6k9ox7`
The :t:`value` of an :t:`await expression` is the :t:`value` held by
:std:`core::task::Poll::Ready`.

.. rubric:: Dynamic Semantics

:dp:`fls_1ppywe40s62c`
The :t:`evaluation` of an :t:`await expression` proceeds as follows:

#. :dp:`fls_eymcs2rgv3qw`
   The :t:`future operand` is evaluated to a :t:`temporary` by invoking
   :std:`core::future::IntoFuture::into_future` with the :t:`future operand`.

#. :dp:`fls_qshnnpirkasz`
   The :t:`temporary` is pinned using :std:`core::pin::Pin::new_unchecked`.

#. :dp:`fls_umevprl99y6c`
   The pinned :t:`temporary` is polled using :std:`core::future::Future::poll`,
   passing in the :std:`core::task::Context` of the current task.

#. :dp:`fls_k76d8ady623m`
   If :std:`core::future::Future::poll` returns
   :std:`core::task::Poll::Pending`, then the current :t:`future` yields.

#. :dp:`fls_frwtufwe8dya`
   If :std:`core::future::Future::poll` returns :std:`core::task::Poll::Ready`,
   then

   #. :dp:`fls_u72ylhlmqge3`
      The :t:`value` held within is unwrapped.

   #. :dp:`fls_tn3vwidct3ks`
      Control stops the evaluation of the :t:`await expression`.

.. rubric:: Examples

.. code-block:: rust

   let future = async { expensive_function() };
   future.await;

.. _fls_kw25194gpael:

Expression Precedence
---------------------

.. rubric:: Legality Rules

:dp:`fls_cwt7afsbgs7w`
Certain :t:`[expression]s` are subject to :t:`precedence` and
:t:`associativity`.

.. glossary-entry:: precedence
   :glossary-dp: fls_ukvdoqo68y5b
   
   :glossary:
     :dp:`fls_sz93844rqc4r`
     :dt:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
     presence of other expressions.
   :chapter:
     :dp:`fls_ya23jjg5wjl`
     :t:`Precedence` is the order by which :t:`[expression]s` are evaluated in the
     presence of other :t:`[expression]s`.

.. glossary-entry:: associativity
   :glossary-dp: fls_fczijre8123c
   
   :glossary:
     :dp:`fls_7i7o23mi2i33`
     :dt:`Associativity` is the order by which :t:`[operand]s` are evaluated within
     a single :t:`expression`.
   :chapter:
     :dp:`fls_bezkcuwp5qol`
     :t:`Associativity` is the order by which :t:`[operand]s` are evaluated within a
     single :t:`expression`.

:dp:`fls_48br7odx6nke`
The :t:`precedence` and :t:`associativity` of qualifying :t:`[expression]s` are
as follows:

.. list-table::

   * - :dp:`fls_mk2yk99p6nvp`
     - **Expression**
     - **Precedence**
     - **Associativity**
   * - :dp:`fls_jtdnf0vmn6xt`
     - :t:`Array expression`

       :t:`Block expression`

       :t:`Continue expression`

       :t:`If expression`

       :t:`If let expression`

       :t:`Literal expression`

       :t:`Loop expression`

       :t:`Match expression`

       :t:`Parenthesized expression`

       :t:`Path expression`

       :t:`Struct expression`

       :t:`Tuple expression`

       :t:`Underscore expression`
     - highest
     - none
   * - :dp:`fls_qurz25skmryg`
     - :t:`Method call expression`
     -
     - none
   * - :dp:`fls_ywqn5nixelkz`
     - :t:`Await expression`

       :t:`Field access expression`
     -
     - left-to-right
   * - :dp:`fls_k3ohh8k888c`
     - :t:`Call expression`

       :t:`Index expression`
     -
     - none
   * - :dp:`fls_41n6z85h1z47`
     - :t:`Error propagation expression`
     -
     - none
   * - :dp:`fls_f39rzauxrlcl`
     - :t:`Borrow expression`

       :t:`Dereference expression`

       :t:`Negation expression`
     -
     - none
   * - :dp:`fls_djphr5mk0t6f`
     - :t:`Type cast expression`
     -
     - left-to-right
   * - :dp:`fls_sif2aqky96j6`
     - :t:`Division expression`

       :t:`Multiplication expression`

       :t:`Remainder expression`
     -
     - left-to-right
   * - :dp:`fls_d7x817v8xzea`
     - :t:`Addition expression`

       :t:`Subtraction expression`
     -
     - left-to-right
   * - :dp:`fls_1f5ibdkz3l51`
     - :t:`Shift left expression`

       :t:`Shift right expression`
     -
     - left-to-right
   * - :dp:`fls_t1zqnab8a752`
     - :t:`Bit and expression`
     -
     - left-to-right
   * - :dp:`fls_f6in3h5cj8i6`
     - :t:`Bit xor expression`
     -
     - left-to-right
   * - :dp:`fls_hxa1avitfvrq`
     - :t:`Bit or expression`
     -
     - left-to-right
   * - :dp:`fls_sy2xzzq06i0x`
     - :t:`Comparison expression`
     -
     - requires parentheses
   * - :dp:`fls_hish3qfmawd`
     - :t:`Lazy and expression`
     -
     - left-to-right
   * - :dp:`fls_ruy7e6yccsqk`
     - :t:`Lazy or expression`
     -
     - left-to-right
   * - :dp:`fls_9qcm0dx9rolw`
     - :t:`Range expression`
     -
     - requires parentheses
   * - :dp:`fls_1l3rgtm6o54s`
     - :t:`Assignment expression`

       :t:`Compound assignment expression`
     -
     - right-to-left
   * - :dp:`fls_hr4kokysrjop`
     - :t:`Break expression`

       :t:`Closure expression`

       :t:`Return expression`
     - lowest
     - none

.. _fls_jmjn8jkbzujm:

Capturing
---------

.. rubric:: Legality Rules

.. glossary-entry:: capturing expression
   :glossary-dp: fls_cl3lpsfgt5eb
   
   :glossary:
     :dp:`fls_awtny282gtud`
     A :dt:`capturing expression` is either an :t:`async block expression` or a
     :t:`closure expression`.
   :chapter:
     :dp:`fls_iamnzlm430ef`
     A :t:`capturing expression` is either an :t:`async block expression` or a
     :t:`closure expression`.

.. glossary-entry:: capture target
   :glossary-dp: fls_c6qwfwsyizya
   
   :glossary:
     :dp:`fls_xmhcp4x8wblz`
     A :dt:`capture target` is either a :t:`binding` or a :t:`field` of a
     :t:`binding`.
   :chapter:
     :dp:`fls_eca6tl7j0afx`
     A :t:`capture target` is either a :t:`variable` or a :t:`field` of a
     :t:`variable`.

.. glossary-entry:: capturing environment
   :glossary-dp: fls_yfk2xfifltxy
   
   :glossary:
     :dp:`fls_7br4azaay3wu`
     The :dt:`capturing environment` of a :t:`capturing expression` consists of all
     :t:`[capture target]s` that are defined outside the :t:`capturing expression`.
   :chapter:
     :dp:`fls_e70ywb8191h`
     The :t:`capturing environment` of a :t:`capturing expression` consists of the
     :t:`[value]s` of all :t:`captured` :t:`[capture target]s`.

.. glossary-entry:: capturing
   :glossary-dp: fls_kvu447p6j61k
   
   :glossary:
     :dp:`fls_4achbk2ewyyb`
     :dt:`Capturing` is the process of saving the :t:`[capture target]s` of a
     :t:`[capturing expression]'s` :t:`capturing environment`.
   :chapter:
     :dp:`fls_1y2ttb466m9c`
     :t:`Capturing` is the process of saving the :t:`[capture target]s` of a
     :t:`[capturing expression]'s` :t:`capturing environment`.

:dp:`fls_ip81lt2mm940`
A :t:`capture target` requires :t:`capturing` when it is used by
the :t:`capturing expression` and it is defined outside of the
:t:`capturing expression`. Such a :t:`capture target` is said to be
:dt:`captured`.

.. glossary-entry:: capture mode
   :glossary-dp: fls_s78gd8yxx2yv
   
   :glossary:
     :dp:`fls_beer0d7wva1d`
     :dt:`Capture mode` is the mechanism by which a :t:`capture target` is captured.
   :chapter:
     :dp:`fls_y9n1i4hbq8sf`
     :t:`Capture mode` is the mechanism by which a :t:`capture target` is captured.

:dp:`fls_O6WYL8AUyPje`
A :t:`captured` :t:`capture target` with :t:`capture mode` :dt:`by value capture`
:t:`passes <passing convention>` the :t:`value` of the :t:`capture target` into
the :t:`capturing environment`.

:dp:`fls_aCxt2Ovmb5He`
A :t:`captured` :t:`capture target` with :t:`capture mode`
:dt:`by immutable reference capture` binds an :t:`immutable reference` to the
:t:`capture target` and passes the :t:`immutable reference` into the
:t:`capturing environment`.

:dp:`fls_xTNFfkxHm5yy`
A :t:`captured` :t:`capture target` with :t:`capture mode`
:dt:`by mutable reference capture` binds a :t:`mutable reference` to the
:t:`capture target` and passes the :t:`mutable reference` into the
:t:`capturing environment`.

:dp:`fls_8HLaLAIZgYfs`
A :t:`captured` :t:`capture target` with :t:`capture mode`
:dt:`by unique immutable reference capture` binds a
:t:`unique immutable reference` to the :t:`capture target` and passes the
:t:`mutable reference` into the :t:`capturing environment`.

.. glossary-entry:: unique immutable reference
   :glossary-dp: fls_Is9hWLC6Q0g5
   
   :glossary:
     :dp:`fls_eXrivAmNxzmv`
     A :dt:`unique immutable reference` is an :t:`immutable reference` produced by
     :t:`capturing` what is asserted to be the only live :t:`reference` to a
     :t:`value` while the :t:`reference` exists.

:dp:`fls_t695ps4lfh6z`
The :t:`capture mode` is determined based on the use of the :t:`capture target`
within the :t:`capturing expression`, as follows:

#. :dp:`fls_6j8cr7d5zs1l`
   If the :t:`capturing expression` is subject to :t:`keyword` ``move``, then
   the :t:`capture mode` is :t:`by value capture`.

#. :dp:`fls_l8e98pyhm08g`
   Otherwise the :t:`capture mode` is determined based on the following
   precedence:

   #. :dp:`fls_33hfay24hx8u`
      :t:`By immutable reference capture`.

   #. :dp:`fls_wmxsd0i2yemf`
      :t:`By unique immutable reference capture` mode, if the
      :t:`capture target` is a :t:`mutable reference` that is being modified.

   #. :dp:`fls_lu779ufqhggl`
      :t:`By mutable reference capture` mode.

   #. :dp:`fls_uqy5w9uc8gla`
      :t:`By value capture`.

:dp:`fls_wvob7114tfat`
A tool selects the first :t:`capture mode` that is compatible with the use of
the :t:`capture target`.

.. _fls_ZfIBiJMf8qE1:

Arithmetic Overflow
-------------------

.. glossary-entry:: arithmetic overflow
   :glossary-dp: fls_vZ1H57x9OFSZ
   
   :glossary:
     :dp:`fls_jbytOQvIddAl`
     An :dt:`arithmetic overflow` occurs if an :t:`arithmetic expression` or a
     :t:`negation expression` computes a :t:`value` of a :t:`scalar type` that lies
     outside of the range of valid :t:`[value]s` for the :t:`scalar type`.
   :chapter:
     :dp:`fls_oFIRXBPXu6Zv`
     An :t:`arithmetic overflow` occurs when an :t:`operator expression` computes a
     :t:`value` of a :t:`scalar type` that lies outside of the range of valid
     :t:`[value]s` for the :t:`scalar type` or when one or more :t:`operand` of an
     :t:`operator expression` lies outside of the range of valid :t:`[value]s` for
     the operation.

.. rubric:: Dynamic Semantics

:dp:`fls_8fU3h8PLasqA`
There are two allowed behaviors for :t:`arithmetic overflow`:

#. :dp:`fls_R48VKcEIbfXC`
   :t:`Evaluation` of the :t:`expression` may result in a :t:`panic`.

#. :dp:`fls_QMpI8K43K2yU`
   The resulting :t:`value` of the :t:`expression` may be truncated, discarding
   the most significant bits that do not fit in the target :t:`type`.
