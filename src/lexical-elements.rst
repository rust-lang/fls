.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Ferrocene Developers

.. default-domain:: spec

.. _fls_411up5z0b6n6:

Lexical Elements
================

.. informational-section::

:dp:`fls_pqwpf87b84tr`
The text of a Rust program consists of :t:`[module]s` organized into :t:`[source
file]s`. The text of a :t:`source file` is a sequence of :t:`[lexical
element]s`, each composed of characters, whose rules are presented in this
chapter.

.. _fls_2i089jvv8j5g:

Character Set
-------------

:dp:`fls_itcth8292ud6`
The program text of a Rust program is written using the :t:`Unicode` character
set.

.. glossary-entry:: Unicode
   :glossary-dp: fls_kafgmevvzl5t
   
   :glossary:
     :dp:`fls_y7gwku7pe1f4`
     :dt:`Unicode` is the universal character encoding standard for written
     characters and text described in the Unicode® Standard by the Unicode
     Consortium.

.. rubric:: Syntax

:dp:`fls_vfx8byq5zo8t`
A character is defined by this document for each cell in the coding space
described by :t:`Unicode`, regardless of whether or not :t:`Unicode` allocates a
character to that cell.

.. glossary-entry:: code point
   :glossary-dp: fls_aqovhozevngd
   
   :glossary:
     :dp:`fls_6xw8jtiomc2n`
     In :t:`Unicode`, a :dt:`code point` is a numeric :t:`value` that maps to a
     character.

.. glossary-entry:: plane
   :glossary-dp: fls_dr6wbsqjd2qm
   
   :glossary:
     :dp:`fls_x1wbguoqdsf9`
     In :t:`Unicode`, a :dt:`plane` is a continuous group of 65,536
     :t:`[code point]s`.

:dp:`fls_pvslhm3chtlb`
A :dt:`whitespace character` is one of the following characters:

* :dp:`fls_a5ec9cpn4sc8`
  0x09 (horizontal tabulation)

* :dp:`fls_dgyrj49y3c7c`
  0x0A (new line)

* :dp:`fls_5ocmngyur7by`
  0x0B (vertical tabulation)

* :dp:`fls_1aj0rgi9kpib`
  0x0C (form feed)

* :dp:`fls_bfzdxsbq2c2q`
  0x0D (carriage return)

* :dp:`fls_vw0kq2y1o63m`
  0x20 (space)

* :dp:`fls_ao296bmamwzh`
  0x85 (next line)

* :dp:`fls_6kymhq7embdh`
  0x200E (left-to-right mark)

* :dp:`fls_8mxmrxvhn3by`
  0x200F (right-to-left mark)

* :dp:`fls_bc6D1ATvmJJr`
  0x2028 (line separator)

* :dp:`fls_zfs15iel08y0`
  0x2029 (paragraph separator)

.. glossary-entry:: whitespace string
   :glossary-dp: fls_cxm8nw6qiryr
   
   :glossary:
     :dp:`fls_nljkmadklwdp`
     A :dt:`whitespace string` is a string that consists of one or more
     :t:`[whitespace character]s`.
   :chapter:
     :dp:`fls_7eifv4ksunu1`
     A :t:`whitespace string` is a string that consists of one or more
     :t:`[whitespace character]s`.

:dp:`fls_PIDKEm8GiLNL`
An :ds:`AsciiCharacter` is any :t:`Unicode` character in the range 0x00 - 0x7F, both inclusive.

.. rubric:: Legality Rules

:dp:`fls_2brw13n9ldgy`
The coded representation of a character is tool-defined.

.. _fls_fgnllgz5k3e6:

Lexical Elements, Separators, and Punctuation
---------------------------------------------

.. rubric:: Syntax

.. syntax::

   LexicalElement ::=
       Comment
     | Identifier
     | Keyword
     | Literal
     | Punctuation

   Punctuation ::=
       Delimiter
     | $$+$$
     | $$-$$
     | $$*$$
     | $$/$$
     | $$%$$
     | $$^$$
     | $$!$$
     | $$&$$
     | $$|$$
     | $$&&$$
     | $$||$$
     | $$<<$$
     | $$>>$$
     | $$+=$$
     | $$-=$$
     | $$*=$$
     | $$/=$$
     | $$%=$$
     | $$^=$$
     | $$&=$$
     | $$|=$$
     | $$<<=$$
     | $$>>=$$
     | $$=$$
     | $$==$$
     | $$!=$$
     | $$>$$
     | $$<$$
     | $$>=$$
     | $$<=$$
     | $$@$$
     | $$_$$
     | $$.$$
     | $$..$$
     | $$...$$
     | $$..=$$
     | $$,$$
     | $$;$$
     | $$:$$
     | $$::$$
     | $$->$$
     | $$=>$$
     | $$#$$
     | $$$$$
     | $$?$$

   Delimiter ::=
       $${$$
     | $$}$$
     | $$[$$
     | $$]$$
     | $$($$
     | $$)$$

.. rubric:: Legality Rules

:dp:`fls_d4nvxsvxj537`
The text of a :t:`source file` is a sequence of separate :t:`[lexical
element]s`. The meaning of a program depends only on the particular sequence of
:t:`[lexical element]s`, excluding :t:`non-[doc comment]s`.

.. glossary-entry:: lexical element
   :glossary-dp: fls_h2tqtmm5686y
   
   :glossary:
     :dp:`fls_nrxnbkatn63n`
     A :dt:`lexical element` is the most basic syntactic element in program
     text.
   :chapter:
     :dp:`fls_a1zylpqha73x`
     A :t:`lexical element` is the most basic syntactic element in program text.

:dp:`fls_jy6wifn5r2bu`
The text of a :t:`source file` is divided into :t:`[line]s`.

.. glossary-entry:: line
   :glossary-dp: fls_8qputmx0i7ku
   
   :glossary:
     :dp:`fls_oqf2439j3y7b`
     A :dt:`line` is a sequence of zero or more characters followed by an end of
     line.
   :chapter:
     :dp:`fls_efdfq9nhpmp5`
     A :t:`line` is a sequence of zero or more characters followed by an end of
     line.

:dp:`fls_go25sisi5fdp`
The representation of an end of line is tool-defined.

.. glossary-entry:: separator
   :glossary-dp: fls_at8q1svh3isg
   
   :glossary:
     :dp:`fls_128xny4qfcj5`
     A :dt:`separator` is a character or a string that separates adjacent
     :t:`[lexical element]s`.
   :chapter:
     :dp:`fls_a6t53o8h1vdk`
     A :t:`separator` is a character or a string that separates adjacent :t:`[lexical
     element]s`. A :t:`whitespace string` is a :t:`separator`.

.. glossary-entry:: punctuator
   :glossary-dp: fls_hdwmw3jbwefi
   
   :glossary:
     :dp:`fls_gwqgi0b7jxmu`
     A :dt:`punctuator` is a character or a sequence of characters in category
     :s:`Punctuation`.

:dp:`fls_8fv63w6f4udl`
A :dt:`simple punctuator` is one of the following special characters:

.. syntax::

   $$+$$
   $$-$$
   $$*$$
   $$/$$
   $$%$$
   $$^$$
   $$!$$
   $$&$$
   $$|$$
   $$=$$
   $$>$$
   $$<$$
   $$@$$
   $$_$$
   $$.$$
   $$,$$
   $$;$$
   $$:$$
   $$#$$
   $$$$$
   $$?$$
   $${$$
   $$}$$
   $$[$$
   $$]$$
   $$($$
   $$)$$

:dp:`fls_es0tz1q9cmoo`
A :dt:`compound punctuator` is one of the following two or more adjacent special
characters:

.. syntax::

   $$&&$$
   $$||$$
   $$<<$$
   $$>>$$
   $$+=$$
   $$-=$$
   $$*=$$
   $$/=$$
   $$%=$$
   $$^=$$
   $$&=$$
   $$|=$$
   $$<<=$$
   $$>>=$$
   $$==$$
   $$!=$$
   $$>=$$
   $$<=$$
   $$..$$
   $$...$$
   $$..=$$
   $$::$$
   $$->$$
   $$=>$$

:dp:`fls_vm86olkeecer`
The following :t:`[compound punctuator]s` are :dt:`[flexible compound
punctuator]s`.

.. syntax::

   $$&&$$
   $$||$$
   $$<<$$
   $$>>$$

:dp:`fls_5zxdgxy8tjrq`
A :t:`flexible compound punctuator` may be treated as a single :t:`compound
punctuator` or two adjacent :t:`[simple punctuator]s`.

:dp:`fls_x89vkq9rwlyt`
Each of the special characters listed for single character :t:`punctuator`
is a :t:`simple punctuator` except if this character is used as a character
of a :t:`compound punctuator`, or a character of a :t:`character literal`, a
:t:`comment`, a :t:`numeric literal`, or a :t:`string literal`.

:dp:`fls_bo3xh8r60ji1`
The following names are used when referring to :t:`[punctuator]s`:

.. list-table::

   * - :dp:`fls_sslkjuxjnteu`
     - **punctuator**
     - **name**
   * - :dp:`fls_9g1godm0jp0z`
     - ``+``
     - Plus
   * - :dp:`fls_6oith9q0soot`
     - ``-``
     - Minus
   * - :dp:`fls_1dledwdc8fa6`
     - ``*``
     - Star
   * - :dp:`fls_lunw7ucj5ius`
     - ``/``
     - Slash
   * - :dp:`fls_a4oiuhz95uiv`
     - ``%``
     - Percent
   * - :dp:`fls_137x9s6guj6h`
     - ``^``
     - Caret
   * - :dp:`fls_y0wdb09cpp1w`
     - ``!``
     - Not
   * - :dp:`fls_48b7mepiuupz`
     - ``&``
     - And
   * - :dp:`fls_g9h9bsvrsmk1`
     - ``|``
     - Or
   * - :dp:`fls_fxne2xd0zzzo`
     - ``&&``
     - And and, lazy boolean and
   * - :dp:`fls_il7zv5x3aw0q`
     - ``||``
     - Or or, lazy boolean or
   * - :dp:`fls_ovcs1qm86ss9`
     - ``<<``
     - Shift left
   * - :dp:`fls_wmhlvjm0b0j9`
     - ``>>``
     - Shift right
   * - :dp:`fls_gg42klb2gn9v`
     - ``+=``
     - Plus equals
   * - :dp:`fls_icahptg5enj4`
     - ``-=``
     - Minus equals
   * - :dp:`fls_baawlxoi7yd4`
     - ``*=``
     - Star equals
   * - :dp:`fls_m7gt3wfbtm81`
     - ``/=``
     - Slash equals
   * - :dp:`fls_6ewl7gn3sjm2`
     - ``%=``
     - Percent equals
   * - :dp:`fls_nb8q6oq8txv3`
     - ``^=``
     - Caret equals
   * - :dp:`fls_4nnky9ansr9j`
     - ``&=``
     - And equals
   * - :dp:`fls_h1gvudehmnn9`
     - ``|=``
     - Or equals
   * - :dp:`fls_6yj1c3lh691s`
     - ``<<=``
     - Shift left equals
   * - :dp:`fls_2d3oo9nou9vv`
     - ``>>=``
     - Shift right equals
   * - :dp:`fls_st2vhcy14ud9`
     - ``=``
     - Equals
   * - :dp:`fls_9gdyw71dl25`
     - ``==``
     - Equals equals, logical equality
   * - :dp:`fls_sp8ufz28l9w3`
     - ``!=``
     - Not equals
   * - :dp:`fls_7kdr8biodxvz`
     - ``>``
     - Greater than
   * - :dp:`fls_pf92l9bkte2u`
     - ``<``
     - Less than
   * - :dp:`fls_ui40thspgyav`
     - ``>=``
     - Greater than equals, greater than or equal to
   * - :dp:`fls_h33qzachmimc`
     - ``<=``
     - Less than equals, less than or equal to
   * - :dp:`fls_13ud1clgdnyv`
     - ``@``
     - At
   * - :dp:`fls_7fosi8l2ktz2`
     - ``_``
     - Underscore
   * - :dp:`fls_9qitp6r75ia6`
     - ``.``
     - Dot
   * - :dp:`fls_g0umao9roi2l`
     - ``..``
     - Dot dot, exclusive range
   * - :dp:`fls_lamrpdpko48`
     - ``...``
     - Dot dot dot, ellipsis
   * - :dp:`fls_s4lte9onbmqb`
     - ``..=``
     - Dot dot equals, inclusive range
   * - :dp:`fls_ywc297y8s0dt`
     - ``,``
     - Comma
   * - :dp:`fls_ijb0fws4gshu`
     - ``;``
     - Semicolon
   * - :dp:`fls_c25ur4xwbpk0`
     - ``:``
     - Colon
   * - :dp:`fls_9dd9479zzq30`
     - ``::``
     - Colon colon, path separator
   * - :dp:`fls_kwsu9d3ppv3f`
     - ``->``
     - Right arrow
   * - :dp:`fls_oh62j9unw4mg`
     - ``=>``
     - Fat arrow, Hashrocket
   * - :dp:`fls_g0tltt8qmbum`
     - ``#``
     - Pound
   * - :dp:`fls_ounkw8b8tk4f`
     - ``$``
     - Dollar sign
   * - :dp:`fls_8ywv8gftsfr1`
     - ``?``
     - Question mark
   * - :dp:`fls_hsn6zc29ifyx`
     - ``{``
     - Left curly brace
   * - :dp:`fls_o3amqe3ca82d`
     - ``}``
     - Right curly brace
   * - :dp:`fls_lkevfpj7sqd3`
     - ``[``
     - Left square bracket
   * - :dp:`fls_ff05ge2189z`
     - ``]``
     - Right square bracket
   * - :dp:`fls_nplkudde6oxf`
     - ``(``
     - Left parenthesis
   * - :dp:`fls_qwnrklmbz0b`
     - ``)``
     - Right parenthesis

.. _fls_21vnag69kbwe:

Identifiers
-----------

.. rubric:: Syntax

.. syntax::

   Identifier ::=
       NonKeywordIdentifier
     | RawIdentifier

   IdentifierList ::=
       Identifier ($$,$$ Identifier)* $$,$$?

   NonKeywordIdentifier ::=
       PureIdentifier
     | WeakKeyword

   RawIdentifier ::=
       $$r#$$ (PureIdentifier | RawIdentifierKeyword)

   PureIdentifier ::=
       XID_Start XID_Continue*
     | $$_$$ XID_Continue+

   IdentifierOrUnderscore ::=
       Identifier
     | $$_$$

   Renaming ::=
       $$as$$ IdentifierOrUnderscore

:dp:`fls_ls7ymvgd5kfa`
A :ds:`RawIdentifierKeyword` is any :t:`keyword` in category :s:`Keyword`,
except ``crate``, ``self``, ``Self``, and ``super``.

:dp:`fls_aqj9aguczgqs`
:ds:`XID_Start` and :ds:`XID_Continue` are defined in Unicode Standard Annex
#31.

.. rubric:: Legality Rules

.. glossary-entry:: identifier
   :glossary-dp: fls_kpsyz8yopova
   
   :glossary:
     :dp:`fls_14zc5bcm9d8o`
     An :dt:`identifier` is a :t:`lexical element` that refers to a :t:`name`.
     
     :dp:`fls_oddu2wzhczvq`
     See :s:`Identifier`.
   :chapter:
     :dp:`fls_xsdmun5uqy4c`
     An :t:`identifier` is a :t:`lexical element` that refers to a :t:`name`.

.. glossary-entry:: pure identifier
   :glossary-dp: fls_sgwvmnoio1ql
   
   :glossary:
     :dp:`fls_6pez8fyiew0k`
     A :dt:`pure identifier` is an :t:`identifier` that does not include
     :t:`[weak keyword]s`.
   :chapter:
     :dp:`fls_ktnf6zkrdy45`
     A :t:`pure identifier` is an :t:`identifier` that does not include :t:`[weak
     keyword]s`.

:dp:`fls_jpecw46eh061`
A :t:`pure identifier` shall follow the specification in Unicode Standard Annex
#31 for :t:`Unicode` version 16.0, with the following profile:

* :dp:`fls_lwcflgezgs5z`
  ``Start`` = ``XID_Start``, plus character 0x5F (low line).

* :dp:`fls_uts0hywaw1rq`
  ``Continue`` = ``XID_Continue``

* :dp:`fls_lju1avcn0pfd`
  ``Medial`` = empty

:dp:`fls_cs6cbw625np1`
Characters 0x200C (zero width non-joiner) and 0x200D (zero width joiner) shall
not appear in a :t:`pure identifier`.

:dp:`fls_irwcldiotei2`
A :t:`pure identifier` shall be restricted to characters in category
:s:`AsciiCharacter` in the following contexts:

* :dp:`fls_g72rxs2z5960`
  :t:`[Crate import]s`,

* :dp:`fls_w473jevurlt1`
  :t:`[Name]s` of external :t:`[crate]s` represented in a :t:`simple path`, when
  the :t:`simple path` starts with namespace qualifier ``::``,

* :dp:`fls_mt1u4m3simhc`
  :t:`[Name]s` of :t:`[outline module]s` that lack :t:`attribute` :c:`path`,

* :dp:`fls_e2v58o233lvd`
  :t:`[Name]s` of :t:`[item]s` that are subject to :t:`attribute`
  :c:`no_mangle`,

* :dp:`fls_op0lp1i065di`
  :t:`[Name]s` of :t:`[item]s` within :t:`[external block]s`.

:dp:`fls_vde7gev5rz4q`
:t:`[Identifier]s` are normalized using Normalization Form C as defined in
Unicode Standard Annex #15.

:dp:`fls_j9yh8j8jgdeu`
Two :t:`[identifier]s` are considered the same if they consist of the same
sequence of characters after performing normalization.

:dp:`fls_jejt5z8m1yew`
:t:`[Declarative macro]s` and :t:`[procedural macro]s` shall receive normalized
:t:`[identifier]s` in their input.

.. rubric:: Examples

.. code-block:: text

   foo
   _identifier
   r#true
   Москва
   東京

.. _fls_nrkd5wpi64oo:

Literals
--------

.. rubric:: Syntax

.. syntax::

   Literal ::=
       BooleanLiteral
     | ByteLiteral
     | ByteStringLiteral
     | CStringLiteral
     | CharacterLiteral
     | NumericLiteral
     | StringLiteral

.. rubric:: Legality Rules

.. glossary-entry:: literal
   :glossary-dp: fls_z850pyf9r1f4
   
   :glossary:
     :dp:`fls_ckbyt11pku9j`
     A :dt:`literal` is a fixed :t:`value` in program text.
     
     :dp:`fls_h1g46cevrqjv`
     See :s:`Literal`.
   :chapter:
     :dp:`fls_s76un78zyd0j`
     A :t:`literal` is a fixed :t:`value` in program text.

.. _fls_2ifjqwnw03ms:

Byte Literals
~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   ByteLiteral ::=
       $$b'$$ ByteContent $$'$$

   ByteContent ::=
       ByteCharacter
     | ByteEscape

   ByteEscape ::=
       $$\0$$
     | $$\"$$
     | $$\'$$
     | $$\t$$
     | $$\n$$
     | $$\r$$
     | $$\\$$
     | $$\x$$ OctalDigit HexadecimalDigit

:dp:`fls_3hpzf12h60u4`
A :ds:`ByteCharacter` is any character in category :s:`AsciiCharacter`
except characters 0x09 (horizontal tabulation), 0x0A (new line), 0x0D (carriage
return), 0x27 (apostrophe), and 0x5C (reverse solidus).

.. rubric:: Legality Rules

.. glossary-entry:: byte literal
   :glossary-dp: fls_e8rokiw23i9t
   
   :glossary:
     :dp:`fls_l67oo0u12zjb`
     A :dt:`byte literal` is a :t:`literal` that denotes a fixed byte :t:`value`.
     
     :dp:`fls_iu9twvm648dx`
     See :s:`ByteLiteral`.
   :chapter:
     :dp:`fls_q0qwr83frszx`
     A :t:`byte literal` is a :t:`literal` that denotes a fixed byte :t:`value`.

:dp:`fls_fggytrv5jvw0`
The :t:`type` of a :t:`byte literal` is :c:`u8`.

.. rubric:: Examples

.. code-block:: rust

   b'h'
   b'\n'
   b'\x1B'

.. _fls_fqaffyrjob7v:

Byte String Literals
~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   ByteStringLiteral ::=
       RawByteStringLiteral
     | SimpleByteStringLiteral

.. rubric:: Legality Rules

.. glossary-entry:: byte string literal
   :glossary-dp: fls_uwe7iomhvgtp
   
   :glossary:
     :dp:`fls_my4r1l3ilyt2`
     A :dt:`byte string literal` is a :t:`literal` that consists of multiple
     :s:`[AsciiCharacter]s`.
     
     :dp:`fls_4yhag19z61bl`
     See :s:`ByteStringLiteral`.
   :chapter:
     :dp:`fls_t63zfv5JdUhj`
     A :t:`byte string literal` is a :t:`literal` that consists of multiple
     :s:`[AsciiCharacter]s`.

:dp:`fls_Xd6LnfzMb7t7`
The character sequence 0x0D 0x0A (carriage return, new line) is replaced by 0x0A
(new line) inside of a :t:`byte string literal`.

.. _fls_msbaxfC09VkK:

Simple Byte String Literals
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::

   SimpleByteStringLiteral ::=
       $$b"$$ SimpleByteStringContent* $$"$$

   SimpleByteStringContent ::=
       ByteEscape
     | SimpleByteStringCharacter
     | StringContinuation

:dp:`fls_3dcqhuosqb84`
A :ds:`SimpleByteStringCharacter` is any character in category :s:`AsciiCharacter`
except characters 0x0D (carriage return), 0x22 (quotation mark), and 0x5C
(reverse solidus).

.. rubric:: Legality Rules

.. glossary-entry:: simple byte string literal
   :glossary-dp: fls_4GvXiDfcPlRD
   
   :glossary:
     :dp:`fls_XpbU4Up0Aza8`
     A :dt:`simple byte string literal` is a :t:`byte string literal` that consists
     of multiple :s:`[AsciiCharacter]s`.
     
     :dp:`fls_OfI70zK68TnQ`
     See :s:`SimpleByteStringLiteral`.
   :chapter:
     :dp:`fls_moe3zfx39ox2`
     A :t:`simple byte string literal` is a :t:`byte string literal` that consists of multiple
     :s:`[AsciiCharacter]s`.

:dp:`fls_vffxb6arj9jf`
The :t:`type` of a :t:`simple byte string literal` of size ``N`` is ``&'static [u8;
N]``.

.. rubric:: Examples

.. code-block:: rust

   b""
   b"a\tb"
   b"Multi\
   line"

.. _fls_jps9102q0qfi:

Raw Byte String Literals
^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::

   RawByteStringLiteral ::=
       $$br$$ RawByteStringContent

   RawByteStringContent ::=
       NestedRawByteStringContent
     | $$"$$ AsciiCharacter* $$"$$

   NestedRawByteStringContent ::=
       $$#$$ RawByteStringContent $$#$$

.. rubric:: Legality Rules

.. glossary-entry:: raw byte string literal
   :glossary-dp: fls_ipeh92kh17ze
   
   :glossary:
     :dp:`fls_8v5k3wemy4tl`
     A :dt:`raw byte string literal` is a :t:`simple byte string literal` that does
     not recognize :t:`[escaped character]s`.
     
     :dp:`fls_5x71i3ay3na2`
     See :s:`RawByteStringLiteral`.
   :chapter:
     :dp:`fls_yyw7nv651580`
     A :t:`raw byte string literal` is a :t:`simple byte string literal` that does not
     recognize :t:`[escaped character]s`.

:dp:`fls_5ybq0euwya42`
The :t:`type` of a :t:`raw byte string literal` of size ``N`` is ``&'static
[u8; N]``.

.. rubric:: Examples

.. code-block:: rust

   br""
   br#""#
   br##"left #"# right"##

.. _fls_U1gHCy16emVe:

C String Literals
~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   CStringLiteral ::=
       RawCStringLiteral
     | SimpleCStringLiteral

.. rubric:: Legality Rules

.. glossary-entry:: c string literal
   :glossary-dp: fls_roz4WXH5JZFj
   
   :glossary:
     :dp:`fls_g3NHtaOhTB7g`
     A :dt:`c string literal` is a :t:`literal` that consists of multiple characters
     with an implicit 0x00 byte appended to it.
     
     :dp:`fls_FZ6QSpjmVme5`
     See :s:`CStringLiteral`.
   :chapter:
     :dp:`fls_VKCW830CzhhN`
     A :t:`c string literal` is a :t:`literal` that consists of multiple characters
     with an implicit 0x00 byte appended to it.

:dp:`fls_XJprzaEn82Xs`
The character sequence 0x0D 0x0A (carriage return, new line) is replaced by 0x0A
(new line) inside of a :t:`c string literal`.

.. _fls_p090c5oTnElW:

Simple C String Literals
^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::

   SimpleCStringLiteral ::=
       $$c"$$ SimpleCStringContent* $$"$$

   SimpleCStringContent ::=
       AsciiEscape
     | SimpleStringCharacter
     | StringContinuation
     | UnicodeEscape

.. glossary-entry:: simple c string literal
   :glossary-dp: fls_fx2hhB0HHSUG
   
   :glossary:
     :dp:`fls_qoHXrmds9SgI`
     A :dt:`simple c string literal` is any :t:`Unicode` character except characters
     0x0D (carriage return), 0x22 (quotation mark), 0x5C (reverse solidus) and 0x00
     (null byte).
     
     :dp:`fls_ggm5FNUqg9EY`
     See :s:`SimpleCStringLiteral`.
   :chapter:
     :dp:`fls_fnwQHo7twAom`
     A :t:`simple c string literal` is any :t:`Unicode` character except characters
     0x0D (carriage return), 0x22 (quotation mark), 0x5C (reverse solidus) and 0x00
     (null byte).

.. rubric:: Legality Rules

:dp:`fls_nPI7j0siGP8G`
A :t:`simple c string literal` is a :t:`c string literal` where the characters are
:t:`Unicode` characters.

:dp:`fls_Ae7LM4Wg0NA7`
The :t:`type` of a :t:`simple string literal` is :std:`&'static
[core::ffi::CStr]`.

.. rubric:: Examples

.. code-block:: rust

   c""
   c"cat"
   c"\tcol\nrow"
   c"bell\x07"
   c"\u{B80a}"
   c"\
   multi\
   line\
   string"

.. _fls_G4LdypF3rL6i:

Raw C String Literals
^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::

   RawCStringLiteral ::=
       $$cr$$ RawCStringContent

   RawCStringContent ::=
       NestedRawCStringContent
     | $$"$$ ~[$$\r$$]* $$"$$

   NestedRawCStringContent ::=
       $$#$$ RawCStringContent $$#$$

.. rubric:: Legality Rules

.. glossary-entry:: raw c string literal
   :glossary-dp: fls_yGGvg3e0nPOh
   
   :glossary:
     :dp:`fls_qhWBzqoYZL0e`
     A :dt:`raw c string literal` is a :t:`simple c string literal` that does not
     recognize :t:`[escaped character]s`.
     
     :dp:`fls_WpFJyq6q4k6E`
     See :s:`RawCStringLiteral`.
   :chapter:
     :dp:`fls_gLrei65i8Uzq`
     A :t:`raw c string literal` is a :t:`simple c string literal` that does not
     recognize :t:`[escaped character]s`.

:dp:`fls_9nJHsg9dCi66`
The :t:`type` of a :t:`simple string literal` is :std:`&'static
[core::ffi::CStr]`.

.. rubric:: Examples

.. code-block:: rust

   cr""
   cr#""#
   cr##"left #"# right"##

.. _fls_hv9jtycp0o1y:

Numeric Literals
~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   NumericLiteral ::=
       FloatLiteral
     | IntegerLiteral

.. rubric:: Legality Rules

.. glossary-entry:: numeric literal
   :glossary-dp: fls_a0qsojiymgjy
   
   :glossary:
     :dp:`fls_978ndaqdv4r`
     A :dt:`numeric literal` is a :t:`literal` that denotes a number.
     
     :dp:`fls_swue4tma9fmf`
     See :s:`NumericLiteral`.
   :chapter:
     :dp:`fls_fqpqnku27v99`
     A :t:`numeric literal` is a :t:`literal` that denotes a number.

.. _fls_2ed4axpsy9u0:

Integer Literals
^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::

   IntegerLiteral ::=
       IntegerContent IntegerSuffix?

   IntegerContent ::=
       BinaryLiteral
     | DecimalLiteral
     | HexadecimalLiteral
     | OctalLiteral

   BinaryLiteral ::=
       $$0b$$ BinaryDigitOrUnderscore* BinaryDigit BinaryDigitOrUnderscore*

   BinaryDigitOrUnderscore ::=
       BinaryDigit
     | $$_$$

   BinaryDigit ::=
       [$$0$$-$$1$$]

   DecimalLiteral ::=
       DecimalDigit DecimalDigitOrUnderscore*

   DecimalDigitOrUnderscore ::=
       DecimalDigit
     | $$_$$

   DecimalDigit ::=
       [$$0$$-$$9$$]

   HexadecimalLiteral ::=
       $$0x$$ HexadecimalDigitOrUnderscore* HexadecimalDigit HexadecimalDigitOrUnderscore*

   HexadecimalDigitOrUnderscore ::=
       HexadecimalDigit
     | $$_$$

   HexadecimalDigit ::=
       [$$0$$-$$9$$ $$a$$-$$f$$ $$A$$-$$F$$]

   OctalLiteral ::=
       $$0o$$ OctalDigitOrUnderscore* OctalDigit OctalDigitOrUnderscore*

   OctalDigitOrUnderscore ::=
       OctalDigit
     | $$_$$

   OctalDigit ::=
       [$$0$$-$$7$$]

   IntegerSuffix ::=
       SignedIntegerSuffix
     | UnsignedIntegerSuffix

   SignedIntegerSuffix ::=
       $$i8$$
     | $$i16$$
     | $$i32$$
     | $$i64$$
     | $$i128$$
     | $$isize$$

   UnsignedIntegerSuffix ::=
       $$u8$$
     | $$u16$$
     | $$u32$$
     | $$u64$$
     | $$u128$$
     | $$usize$$

.. rubric:: Legality Rules

.. glossary-entry:: integer literal
   :glossary-dp: fls_e2kizieowvuh
   
   :glossary:
     :dp:`fls_23a1fjpf15qv`
     An :dt:`integer literal` is a :t:`numeric literal` that denotes a whole number.
     
     :dp:`fls_6qpj0nr0jpjr`
     See :s:`IntegerLiteral`.
   :chapter:
     :dp:`fls_vkk2krfn93ry`
     An :t:`integer literal` is a :t:`numeric literal` that denotes a whole number.

.. glossary-entry:: binary literal
   :glossary-dp: fls_or4o65fyt28y
   
   :glossary:
     :dp:`fls_hy54uj6u3nqw`
     A :dt:`binary literal` is an :t:`integer literal` in base 2.
     
     :dp:`fls_693r7vs2s7o7`
     See :s:`BinaryLiteral`.
   :chapter:
     :dp:`fls_nxqncu5yq4eu`
     A :t:`binary literal` is an :t:`integer literal` in base 2.

.. glossary-entry:: decimal literal
   :glossary-dp: fls_128iunbbiuql
   
   :glossary:
     :dp:`fls_lwv823lih69m`
     A :dt:`decimal literal` is an :t:`integer literal` in base 10.
     
     :dp:`fls_pxiba4se64y4`
     See :s:`DecimalLiteral`.
   :chapter:
     :dp:`fls_rn8xfd66yvst`
     A :t:`decimal literal` is an :t:`integer literal` in base 10.

.. glossary-entry:: hexadecimal literal
   :glossary-dp: fls_5uiij8eqln5g
   
   :glossary:
     :dp:`fls_8b6njsi8g68i`
     A :dt:`hexadecimal literal` is an :t:`integer literal` in base 16.
     
     :dp:`fls_vssa4z5wcgaa`
     See :s:`HexadecimalLiteral`.
   :chapter:
     :dp:`fls_2268lchxkzjp`
     A :t:`hexadecimal literal` is an :t:`integer literal` in base 16.

.. glossary-entry:: octal literal
   :glossary-dp: fls_q47u2zq6clon
   
   :glossary:
     :dp:`fls_pf4341vnqiin`
     An :dt:`octal literal` is an :t:`integer literal` in base 8.
     
     :dp:`fls_8u0n6xu0mizm`
     See ``OctalLiteral.``
   :chapter:
     :dp:`fls_4v7awnutbpoe`
     An :t:`octal literal` is an :t:`integer literal` in base 8.

.. glossary-entry:: integer suffix
   :glossary-dp: fls_bhvh8qwqy8ve
   
   :glossary:
     :dp:`fls_qazh8f8rs528`
     An :dt:`integer suffix` is a component of an :t:`integer literal` that
     specifies an explicit :t:`integer type`.
     
     :dp:`fls_jqagv350kw2m`
     See ``IntegerSuffix.``
   :chapter:
     :dp:`fls_f1e29aj0sqvl`
     An :t:`integer suffix` is a component of an :t:`integer literal` that specifies
     an explicit :t:`integer type`.

.. glossary-entry:: suffixed integer
   :glossary-dp: fls_bmbu11ycjpor
   
   :glossary:
     :dp:`fls_ltzetxu3sq7k`
     A :dt:`suffixed integer` is an :t:`integer literal` with an :t:`integer suffix`.
   :chapter:
     :dp:`fls_u83mffscqm6`
     A :t:`suffixed integer` is an :t:`integer literal` with an :t:`integer suffix`.

.. glossary-entry:: unsuffixed integer
   :glossary-dp: fls_d18nctsj8wu5
   
   :glossary:
     :dp:`fls_t419z3zder0q`
     An :dt:`unsuffixed integer` is an :t:`integer literal` without an
     :t:`integer suffix`.
   :chapter:
     :dp:`fls_g10nuv14q4jn`
     An :t:`unsuffixed integer` is an :t:`integer literal` without an :t:`integer
     suffix`.

:dp:`fls_hpkkvuj1z1ez`
The :t:`type` of a :t:`suffixed integer` is determined by its :t:`integer
suffix` as follows:

* :dp:`fls_7yq2fep848ky`
  Suffix ``i8`` specifies type :c:`i8`.

* :dp:`fls_bzm8lwq3qlat`
  Suffix ``i16`` specifies type :c:`i16`.

* :dp:`fls_l4cx36brc1r5`
  Suffix ``i32`` specifies type :c:`i32`.

* :dp:`fls_wthchinwx996`
  Suffix ``i64`` specifies type :c:`i64`.

* :dp:`fls_7uoaet2pm3am`
  Suffix ``i128`` specifies type :c:`i128`.

* :dp:`fls_p4rw583o2qbi`
  Suffix ``isize`` specifies type :c:`isize`.

* :dp:`fls_xrv4q56lmoo3`
  Suffix ``u8`` specifies type :c:`u8`.

* :dp:`fls_66e3q5um6cwc`
  Suffix ``u16`` specifies type :c:`u16`.

* :dp:`fls_5asyk66y7c9d`
  Suffix ``u32`` specifies type :c:`u32`.

* :dp:`fls_76fifqjka0lx`
  Suffix ``u64`` specifies type :c:`u64`.

* :dp:`fls_fsaimo419gf0`
  Suffix ``u128`` specifies type :c:`u128`.

* :dp:`fls_hvzacbu7yiwc`
  Suffix ``usize`` specifies type :c:`usize`.

:dp:`fls_50qipwqi3arw`
The :t:`type` of an :t:`unsuffixed integer` is determined by :t:`type inference`
as follows:

* :dp:`fls_idzhusp2l908`
  If an :t:`integer type` can be uniquely determined from the surrounding
  program context, then the :t:`unsuffixed integer` has that :t:`type`.

* :dp:`fls_qqrqyc6uhol`
  If the program context under-constrains the :t:`type`, then the :t:`inferred
  type` is :c:`i32`.

* :dp:`fls_pexi5jazthq6`
  If the program context over-constrains the :t:`type`, then this is considered
  a static error.

.. rubric:: Examples

.. code-block:: rust

   0b0010_1110_u8
   1___2_3
   0x4D8a
   0o77_52i128

.. _fls_29tlg1vyqay2:

Float Literals
^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::

   FloatLiteral ::=
       DecimalLiteral $$.$$
     | DecimalLiteral FloatExponent
     | DecimalLiteral $$.$$ DecimalLiteral FloatExponent?
     | DecimalLiteral ($$.$$ DecimalLiteral)? FloatExponent? FloatSuffix

   FloatExponent ::=
       ExponentLetter ExponentSign? ExponentMagnitude

   ExponentLetter ::=
       $$e$$
     | $$E$$

   ExponentSign ::=
       $$+$$
     | $$-$$

   ExponentMagnitude ::=
       DecimalDigitOrUnderscore* DecimalDigit DecimalDigitOrUnderscore*

   FloatSuffix ::=
       $$f32$$
     | $$f64$$

.. rubric:: Legality Rules

.. glossary-entry:: float literal
   :glossary-dp: fls_achdyw3nbme3
   
   :glossary:
     :dp:`fls_53o8dio9vpjh`
     A :dt:`float literal` is a :t:`numeric literal` that denotes a fractional
     number.
     
     :dp:`fls_hqeaakhsqxok`
     See :s:`FloatLiteral`.
   :chapter:
     :dp:`fls_rzi7oeqokd6e`
     A :t:`float literal` is a :t:`numeric literal` that denotes a fractional number.

.. glossary-entry:: float suffix
   :glossary-dp: fls_wgylj1n4wrqe
   
   :glossary:
     :dp:`fls_vka2z7frq9j8`
     A :dt:`float suffix` is a component of a :t:`float literal` that specifies an
     explicit :t:`floating-point type`.
     
     :dp:`fls_2k1ddqhsgxqk`
     See :s:`FloatSuffix`.
   :chapter:
     :dp:`fls_2ru1zyrykd37`
     A :t:`float suffix` is a component of a :t:`float literal` that specifies an
     explicit :t:`floating-point type`.

.. glossary-entry:: suffixed float
   :glossary-dp: fls_qar9v52smi9j
   
   :glossary:
     :dp:`fls_7reb4jp0x1wf`
     A :dt:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.
   :chapter:
     :dp:`fls_21mhnhplzam7`
     A :t:`suffixed float` is a :t:`float literal` with a :t:`float suffix`.

.. glossary-entry:: unsuffixed float
   :glossary-dp: fls_4ph9cact2scc
   
   :glossary:
     :dp:`fls_7wp6y0xeqqve`
     An :dt:`unsuffixed float` is a :t:`float literal` without a :t:`float suffix`.
   :chapter:
     :dp:`fls_drqh80k0sfkb`
     An :t:`unsuffixed float` is a :t:`float literal` without a :t:`float suffix`.

:dp:`fls_cbs7j9pjpusw`
The :t:`type` of a :t:`suffixed float` is determined by the :t:`float suffix`
as follows:

* :dp:`fls_b9w7teaw1f8f`
  Suffix ``f32`` specifies type :c:`f32`.

* :dp:`fls_eawxng4ndhv0`
  Suffix ``f64`` specifies type :c:`f64`.

:dp:`fls_yuhza1muo7o`
The :t:`type` of an :t:`unsuffixed float` is determined by :t:`type inference`
as follows:

* :dp:`fls_4sxt1ct7fyen`
  If a :t:`floating-point type` can be uniquely determined from the surrounding
  program context, then the :t:`unsuffixed float` has that :t:`type`.

* :dp:`fls_wa72rssp0jnt`
  If the program context under-constrains the :t:`type`, then the :t:`inferred
  type` is :c:`f64`.

* :dp:`fls_x2cw7g8g56f8`
  If the program context over-constrains the :t:`type`, then this is considered
  a static error.

.. rubric:: Examples

.. code-block:: rust

   45.
   8E+1_820
   3.14e5
   8_031.4_e-12f64

.. _fls_ypa86oqxhn9u:

Character Literals
~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   CharacterLiteral ::=
       $$'$$ CharacterContent $$'$$

   CharacterContent ::=
       AsciiEscape
     | CharacterLiteralCharacter
     | UnicodeEscape

   AsciiEscape ::=
       $$\0$$
     | $$\"$$
     | $$\'$$
     | $$\t$$
     | $$\n$$
     | $$\r$$
     | $$\\$$
     | $$\x$$ OctalDigit HexadecimalDigit

:dp:`fls_j9q9ton57rvl`
A :ds:`CharacterLiteralCharacter` is any :t:`Unicode` character except
characters 0x09 (horizontal tabulation), 0x0A (new line), 0x0D (carriage
return), 0x27 (apostrophe), and 0x5c (reverse solidus).

:dp:`fls_5v9gx22g5wPm`
A :ds:`UnicodeEscape` starts with a ``\u{`` literal, followed by 1 to 6
instances of a :s:`HexadecimalDigit`, inclusive, followed by a ``}`` character.
It can represent any :t:`Unicode` codepoint between U+00000 and U+10FFFF,
inclusive, except :t:`Unicode` surrogate codepoints, which exist between
the range of U+D800 and U+DFFF, inclusive.

.. rubric:: Legality Rules

.. glossary-entry:: character literal
   :glossary-dp: fls_cfphqaml82ik
   
   :glossary:
     :dp:`fls_8oah1cf8p0lb`
     A :dt:`character literal` is a :t:`literal` that denotes a fixed :t:`Unicode`
     character.
     
     :dp:`fls_sup0h5mvibzs`
     See :s:`CharacterLiteral`.
   :chapter:
     :dp:`fls_vag2oy4q7d4n`
     A :t:`character literal` is a :t:`literal` that denotes a fixed :t:`Unicode`
     character.

:dp:`fls_n8z6p6g564r2`
The :t:`type` of a :t:`character literal` is :c:`char`.

.. rubric:: Examples

.. code-block:: text

   'a'
   '\t'
   '\x1b'
   '\u{1F30}'

.. _fls_boyhlu5srp6u:

String Literals
~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   StringLiteral ::=
       RawStringLiteral
     | SimpleStringLiteral

.. rubric:: Legality Rules

.. glossary-entry:: string literal
   :glossary-dp: fls_cck2tmyzmpja
   
   :glossary:
     :dp:`fls_dphk5br0ag35`
     A :dt:`string literal` is a :t:`literal` that consists of multiple characters.
     
     :dp:`fls_z0t3ae24h5h5`
     See :s:`StringLiteral`.
   :chapter:
     :dp:`fls_7fuctvtvdi7x`
     A :t:`string literal` is a :t:`literal` that consists of multiple characters.

:dp:`fls_NyiCpU2tzJlQ`
The character sequence 0x0D 0x0A (carriage return, new line) is replaced by 0x0A
(new line) inside of a :t:`string literal`.

.. _fls_hucd52suu6it:

Simple String Literals
^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::

   SimpleStringLiteral ::=
       $$"$$ SimpleStringContent* $$"$$

   SimpleStringContent ::=
       AsciiEscape
     | SimpleStringCharacter
     | StringContinuation
     | UnicodeEscape

:dp:`fls_1pdzwkt5txfj`
A :ds:`SimpleStringCharacter` is any :t:`Unicode` character except characters
0x0D (carriage return), 0x22 (quotation mark), and 0x5C (reverse solidus).

:dp:`fls_wawtu6j3fiqn`
:ds:`StringContinuation` is the character sequence 0x5C 0x0A (reverse solidus,
new line).

.. rubric:: Legality Rules

.. glossary-entry:: simple string literal
   :glossary-dp: fls_dpod2gc7a0u
   
   :glossary:
     :dp:`fls_p6qyyptz8w8w`
     A :dt:`simple string literal` is a :t:`string literal` where the characters are
     :t:`Unicode` characters.
     
     :dp:`fls_osj0c4dmr6e0`
     See :s:`SimpleStringLiteral`.
   :chapter:
     :dp:`fls_ycy5ee6orjx`
     A :t:`simple string literal` is a :t:`string literal` where the characters are
     :t:`Unicode` characters.

:dp:`fls_6nt5kls21xes`
The :t:`type` of a :t:`simple string literal` is ``&'static str``.

.. rubric:: Examples

.. code-block:: rust

   ""
   "cat"
   "\tcol\nrow"
   "bell\x07"
   "\u{B80a}"
   "\
   multi\
   line\
   string"

.. _fls_usr6iuwpwqqh:

Raw String Literals
^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. syntax::

   RawStringLiteral ::=
       $$r$$ RawStringContent

   RawStringContent ::=
       NestedRawStringContent
     | $$"$$ ~[$$\r$$]* $$"$$

   NestedRawStringContent ::=
       $$#$$ RawStringContent $$#$$

.. rubric:: Legality Rules

.. glossary-entry:: raw string literal
   :glossary-dp: fls_echjohx6fjc
   
   :glossary:
     :dp:`fls_48t4v316951j`
     A :dt:`raw string literal` is a :t:`simple string literal` that does not
     recognize :t:`[escaped character]s`.
     
     :dp:`fls_26ol7lrnux94`
     See :s:`RawStringLiteral`.
   :chapter:
     :dp:`fls_36suwhbwmq1t`
     A :t:`raw string literal` is a :t:`simple string literal` that does not
     recognize :t:`[escaped character]s`.

:dp:`fls_ms43w1towz40`
The :t:`type` of a :t:`raw string literal` is ``&'static str``.

.. rubric:: Examples

.. code-block:: rust

   r""
   r#""#
   r##"left #"# right"##

.. _fls_jkab8eevzbte:

Boolean Literals
~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   BooleanLiteral ::=
       $$false$$
     | $$true$$

.. rubric:: Legality Rules

.. glossary-entry:: boolean literal
   :glossary-dp: fls_oz4tdyp3rvm4
   
   :glossary:
     :dp:`fls_5mrxdqh474vk`
     A :dt:`boolean literal` is a :t:`literal` that denotes the truth :t:`[value]s`
     of logic and Boolean algebra.
     
     :dp:`fls_i13qcchm9vkk`
     See :s:`BooleanLiteral`.
   :chapter:
     :dp:`fls_1lll64ftupjd`
     A :t:`boolean literal` is a :t:`literal` that denotes the truth :t:`[value]s` of
     logic and Boolean algebra.

:dp:`fls_pgngble3ilyx`
The :t:`type` of a :t:`boolean literal` is :c:`bool`.

.. rubric:: Examples

.. code-block:: rust

   true

.. _fls_q8l2jza7d9xa:

Comments
--------

.. rubric:: Syntax

.. syntax::

   Comment ::=
       BlockCommentOrDoc
     | LineCommentOrDoc

   BlockCommentOrDoc ::=
       BlockComment
     | InnerBlockDoc
     | OuterBlockDoc

   LineCommentOrDoc ::=
       LineComment
     | InnerLineDoc
     | OuterLineDoc

   LineComment ::=
       $$//$$
     | $$//$$ (~[$$!$$ $$/$$] | $$//$$) ~[$$\n$$]*

   BlockComment ::=
       $$/*$$ (~[$$!$$ $$*$$] | $$**$$ | BlockCommentOrDoc) (BlockCommentOrDoc | ~[$$*/$$])* $$*/$$
     | $$/**/$$
     | $$/***/$$

   InnerBlockDoc ::=
       $$/*!$$ (BlockCommentOrDoc | ~[$$*/$$ $$\r$$])* $$*/$$

   InnerLineDoc ::=
       $$//!$$ ~[$$\n$$ $$\r$$]*

   OuterBlockDoc ::=
       $$/**$$ (~[$$*$$] | BlockCommentOrDoc) (BlockCommentOrDoc | ~[$$*/$$ $$\r$$])* $$*/$$

   OuterLineDoc ::=
       $$///$$ (~[$$/$$] ~[$$\n$$ $$\r$$]*)?

.. rubric:: Legality Rules

.. glossary-entry:: comment
   :glossary-dp: fls_2moavfyeit0m
   
   :glossary:
     :dp:`fls_3xhoz9f7xy1t`
     A :dt:`comment` is a :t:`lexical element` that acts as an annotation or an
     explanation in program text.
     
     :dp:`fls_pi32rhfqghma`
     See :s:`Comment`.
   :chapter:
     :dp:`fls_8obn3dtzpe5f`
     A :t:`comment` is a :t:`lexical element` that acts as an annotation or an
     explanation in program text.

.. glossary-entry:: block comment
   :glossary-dp: fls_aa980vviqjue
   
   :glossary:
     :dp:`fls_a0ejcfs7y5uy`
     A :dt:`block comment` is a :t:`comment` that spans one or more :t:`[line]s`.
     
     :dp:`fls_21r4tblk8awi`
     See :s:`BlockComment`.
   :chapter:
     :dp:`fls_qsbnl11be35s`
     A :t:`block comment` is a :t:`comment` that spans one or more :t:`[line]s`.

.. glossary-entry:: line comment
   :glossary-dp: fls_k5ycqijslkxh
   
   :glossary:
     :dp:`fls_3e7asah7lkqj`
     A :dt:`line comment` is a :t:`comment` that spans exactly one :t:`line`.
     
     :dp:`fls_8j5j777dv2jm`
     See :s:`LineComment`.
   :chapter:
     :dp:`fls_nayisy85kyq2`
     A :t:`line comment` is a :t:`comment` that spans exactly one :t:`line`.

.. glossary-entry:: inner block doc
   :glossary-dp: fls_chbp2je32okc
   
   :glossary:
     :dp:`fls_f4nqkybpwj1a`
     An :dt:`inner block doc` is a :t:`block comment` that applies to an enclosing
     :t:`non-[comment]` :t:`construct`.
     
     :dp:`fls_lmpaznk198ga`
     See :s:`InnerBlockDoc`.
   :chapter:
     :dp:`fls_k3hj30hjkdhw`
     An :t:`inner block doc` is a :t:`block comment` that applies to an enclosing
     :t:`non-[comment]` :t:`construct`.

.. glossary-entry:: inner line doc
   :glossary-dp: fls_xgm53126q9c4
   
   :glossary:
     :dp:`fls_vtwavwjhgvlz`
     An :dt:`inner line doc` is a :t:`line comment` that applies to an enclosing
     :t:`non-[comment]` :t:`construct`.
     
     :dp:`fls_8cnikewkqs7`
     See :s:`InnerLineDoc`.
   :chapter:
     :dp:`fls_tspijl68lduc`
     An :t:`inner line doc` is a :t:`line comment` that applies to an enclosing
     :t:`non-[comment]` :t:`construct`.

.. glossary-entry:: inner doc comment
   :glossary-dp: fls_vR1ucGTBKjlH
   
   :glossary:
     :dp:`fls_6KunKwZf9QaF`
     An :dt:`inner doc comment` is either an :t:`inner block doc` or an
     :t:`inner line doc`.
   :chapter:
     :dp:`fls_KZp0yiFLTqxb`
     An :t:`inner doc comment` is either an :t:`inner block doc` or an
     :t:`inner line doc`.

.. glossary-entry:: outer block doc
   :glossary-dp: fls_toncretg92qh
   
   :glossary:
     :dp:`fls_531ggn1f8f6u`
     An :dt:`outer block doc` is a :t:`block comment` that applies to a subsequent
     :t:`non-[comment]` :t:`construct`.
     
     :dp:`fls_ddy9a66tpytp`
     See :s:`OuterBlockDoc`.
   :chapter:
     :dp:`fls_63gzofa9ktic`
     An :t:`outer block doc` is a :t:`block comment` that applies to a subsequent
     :t:`non-[comment]` :t:`construct`.

.. glossary-entry:: outer line doc
   :glossary-dp: fls_eqjbv8sovvfl
   
   :glossary:
     :dp:`fls_m3u30fu8uac3`
     An :dt:`outer line doc` is a :t:`line comment` that applies to a subsequent
     :t:`non-[comment]` :t:`construct`.
     
     :dp:`fls_1ppwidw7szk5`
     See :s:`OuterLineDoc`.
   :chapter:
     :dp:`fls_scko7crha0um`
     An :t:`outer line doc` is a :t:`line comment` that applies to a subsequent
     :t:`non-[comment]` :t:`construct`.

.. glossary-entry:: outer doc comment
   :glossary-dp: fls_PuTD100sWO5N
   
   :glossary:
     :dp:`fls_mgSEUNUPcPBs`
     An :dt:`outer doc comment` is either an :t:`outer block doc` or an
     :t:`outer line doc`.
   :chapter:
     :dp:`fls_RYVL9KgaxKvl`
     An :t:`outer doc comment` is either an :t:`outer block doc` or an
     :t:`outer line doc`.

.. glossary-entry:: doc comment
   :glossary-dp: fls_4nm1r57ntecm
   
   :glossary:
     :dp:`fls_wkc1w2xk7ebh`
     A :dt:`doc comment` is a :t:`comment` class that includes
     :t:`[inner block doc]s`, :t:`[inner line doc]s`, :t:`[outer block doc]s`,
     and :t:`[outer line doc]s`.
   :chapter:
     :dp:`fls_7n6d3jx61ose`
     A :t:`doc comment` is a :t:`comment` class that includes :t:`[inner block
     doc]s`, :t:`[inner line doc]s`, :t:`[outer block doc]s`, and :t:`[outer line
     doc]s`.

:dp:`fls_6fxcs17n4kw`
Character 0x0D (carriage return) shall not appear in a :t:`comment`.

:dp:`fls_uze7l7cxonk1`
:t:`[Block comment]s`, :t:`[inner block doc]s`, and :t:`[outer block doc]s`
shall extend one or more :t:`[line]s`.

:dp:`fls_gy23lwlqw2mc`
:t:`[Line comment]s`, :t:`[inner line doc]s`, and :t:`[outer line doc]s` shall
extend exactly one :t:`line`.

:dp:`fls_w7d0skpov1is`
:t:`[Outer block doc]s` and :t:`[outer line doc]s` shall apply to a subsequent
:t:`non-[comment]` :t:`construct`.

:dp:`fls_32ncjvj2kn7z`
:t:`[Inner block doc]s` and :t:`[inner line doc]s` shall apply to an enclosing
:t:`non-[comment]` :t:`construct`.

:dp:`fls_ok0zvo9vcmzo`
:t:`[Inner block doc]s` and :t:`[inner line doc]s` are equivalent to
:t:`attribute` :c:`doc` of the form ``#![doc = content]``, where ``content``
is a :t:`string literal` form of the :t:`comment` without the leading ``//!``,
``/*!`` and trailing ``*/`` characters.

:dp:`fls_nWtKuPi8Fw6v`
:t:`[Outer block doc]s` and :t:`[outer line doc]s` are equivalent to
:t:`attribute` :c:`doc` of the form ``#[doc = content]``, where ``content``
is a :t:`string literal` form of the :t:`comment` without the leading ``///``,
``/**`` and trailing ``*/`` characters.

.. rubric:: Examples

.. code-block:: rust

   // This is a stand-alone line comment. So is the next line.

   ////

   /* This is a stand-alone
      block comment. */

   /*
     /* This is a nested block comment */
   */

   /// This outer line comment applies to commented_module.

   /** This outer block comment applies to commented_module,
       and is considered documentation. */

   pub mod commented_module {

       //! This inner line comment applies to commented_mode.

       /*! This inner block comment applies to commented_module,
           and is considered documentation. */
   }

.. _fls_lish33a1naw5:

Keywords
--------

.. rubric:: Syntax

.. syntax::

   Keyword ::=
       ReservedKeyword
     | StrictKeyword
     | WeakKeyword

.. rubric:: Legality Rules

.. glossary-entry:: keyword
   :glossary-dp: fls_yjs58mp5fkxz
   
   :glossary:
     :dp:`fls_z3825koc9c1w`
     A :dt:`keyword` is a word in program text that has special meaning.
     
     :dp:`fls_yvnf2mu4pr75`
     See :s:`Keyword`.
   :chapter:
     :dp:`fls_dti0uu7rz81w`
     A :t:`keyword` is a word in program text that has special meaning.

:dp:`fls_sxg1o4oxql51`
:t:`[Keyword]s` are case sensitive.

.. _fls_mec5cg5aptf8:

Strict Keywords
~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   StrictKeyword ::=
       $$as$$
     | $$async$$
     | $$await$$
     | $$break$$
     | $$const$$
     | $$continue$$
     | $$crate$$
     | $$dyn$$
     | $$else$$
     | $$enum$$
     | $$extern$$
     | $$false$$
     | $$fn$$
     | $$for$$
     | $$if$$
     | $$impl$$
     | $$in$$
     | $$let$$
     | $$loop$$
     | $$match$$
     | $$mod$$
     | $$move$$
     | $$mut$$
     | $$pub$$
     | $$ref$$
     | $$return$$
     | $$self$$
     | $$Self$$
     | $$static$$
     | $$struct$$
     | $$super$$
     | $$trait$$
     | $$true$$
     | $$type$$
     | $$unsafe$$
     | $$use$$
     | $$where$$
     | $$while$$

.. rubric:: Legality Rules

.. glossary-entry:: strict keyword
   :glossary-dp: fls_bzhaq3q378ay
   
   :glossary:
     :dp:`fls_hza9spr6behn`
     A :dt:`strict keyword` is a :t:`keyword` that always holds its special meaning.
     
     :dp:`fls_67pzayd9qzzs`
     See :s:`StrictKeyword`.
   :chapter:
     :dp:`fls_bsh7qsyvox21`
     A :t:`strict keyword` is a :t:`keyword` that always holds its special meaning.

.. _fls_cbsgp6k0qa82:

Reserved Keywords
~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   ReservedKeyword ::=
       $$abstract$$
     | $$become$$
     | $$box$$
     | $$do$$
     | $$final$$
     | $$macro$$
     | $$override$$
     | $$priv$$
     | $$try$$
     | $$typeof$$
     | $$unsized$$
     | $$virtual$$
     | $$yield$$

.. rubric:: Legality Rules

.. glossary-entry:: reserved keyword
   :glossary-dp: fls_x7yd6o4akrrg
   
   :glossary:
     :dp:`fls_b67hj7fdbq4s`
     A :dt:`reserved keyword` is a :t:`keyword` that is not yet in use.
     
     :dp:`fls_hp9iqdrkt0cg`
     See :s:`ReservedKeyword`.
   :chapter:
     :dp:`fls_w4b97ewwnql`
     A :t:`reserved keyword` is a :t:`keyword` that is not yet in use.

.. _fls_9kjpxri0axvg:

Weak Keywords
~~~~~~~~~~~~~

.. rubric:: Syntax

.. syntax::

   WeakKeyword ::=
       $$macro_rules$$
     | $$'static$$
     | $$union$$
     | $$safe$$

.. rubric:: Legality Rules

.. glossary-entry:: weak keyword
   :glossary-dp: fls_iplp3gvfbcpw
   
   :glossary:
     :dp:`fls_4hiznltf5wlu`
     A :dt:`weak keyword` is a :t:`keyword` whose special meaning depends on the
     context.
     
     :dp:`fls_psah573fsrig`
     See :s:`WeakKeyword`.
   :chapter:
     :dp:`fls_bv87t1gvj7bz`
     A :t:`weak keyword` is a :t:`keyword` whose special meaning depends on the
     context.

:dp:`fls_bl55g03jmayf`
Word ``macro_rules`` acts as a :t:`keyword` only when used in the context of a
:s:`MacroRulesDefinition`.

:dp:`fls_c354oryv513p`
Word ``'static`` acts as a :t:`keyword` only when used in the context of a
:s:`LifetimeIndication`.

:dp:`fls_r9fhuiq1ys1p`
Word ``union`` acts as a :t:`keyword` only when used in the context of a
:s:`UnionDeclaration`.

:dp:`fls_g0JEluWqBpNc`
Word ``safe`` acts as a :t:`keyword` only when used as a qualifier of :s:`FunctionDeclaration` or :s:`StaticDeclaration` in the context of a :s:`ExternalBlock`.
