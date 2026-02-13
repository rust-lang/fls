.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Ferrocene Developers

.. default-domain:: spec

.. _fls_l21tjqjkkaa0:

Associated Items
================

.. rubric:: Syntax

.. syntax::

   AssociatedItem ::=
       OuterAttributeOrDoc* (AssociatedItemWithVisibility | TerminatedMacroInvocation)

   AssociatedItemWithVisibility ::=
       VisibilityModifier? (
           ConstantDeclaration
         | FunctionDeclaration
         | TypeAliasDeclaration
       )

.. rubric:: Legality Rules

.. glossary-entry:: associated item
   :glossary-dp: fls_f3ferow5ugp
   
   :glossary:
     :dp:`fls_o5ysjk7l91ni`
     An :dt:`associated item` is an :t:`item` that appears within an
     :t:`implementation` or a :t:`trait`.
     
     :dp:`fls_44vtqu7tvhi2`
     See :s:`AssociatedItem`.
   :chapter:
     :dp:`fls_ckzd25qd213t`
     An :t:`associated item` is an :t:`item` that appears within an
     :t:`implementation` or a :t:`trait`.

.. glossary-entry:: associated constant
   :glossary-dp: fls_pjb22ylz5swp
   
   :glossary:
     :dp:`fls_hi9qa0k2nujb`
     An :dt:`associated constant` is a :t:`constant` that appears as an
     :t:`associated item`.
   :chapter:
     :dp:`fls_5y6ae0xqux57`
     An :t:`associated constant` is a :t:`constant` that appears as an
     :t:`associated item`.

.. glossary-entry:: incomplete associated constant
   :glossary-dp: fls_j44ow2k5va3s
   
   :glossary:
     :dp:`fls_bq48gl84bul0`
     An :dt:`incomplete associated constant` is an :t:`associated constant` without
     a :t:`constant initializer`.

.. glossary-entry:: associated function
   :glossary-dp: fls_vxiitesidcc2
   
   :glossary:
     :dp:`fls_zcy5pat39bq7`
     An :dt:`associated function` is a :t:`function` that appears as an
     :t:`associated item`.
   :chapter:
     :dp:`fls_lj7492aq7fzo`
     An :t:`associated function` is a :t:`function` that appears as an
     :t:`associated item`.

.. glossary-entry:: incomplete associated function
   :glossary-dp: fls_ga2n4nbm1pkk
   
   :glossary:
     :dp:`fls_iboondra204w`
     An :dt:`incomplete associated function` is an :t:`associated function` without
     a :t:`function body`.

.. glossary-entry:: associated type
   :glossary-dp: fls_zfs68g3yk0uw
   
   :glossary:
     :dp:`fls_rs0n72c2d8f`
     An :dt:`associated type` is a :t:`type alias` that appears as an
     :t:`associated item`.
   :chapter:
     :dp:`fls_8cz4rdrklaj4`
     An :t:`associated type` is a :t:`type alias` that appears as an
     :t:`associated item`.

.. glossary-entry:: incomplete associated type
   :glossary-dp: fls_n99acc2tr9qm
   
   :glossary:
     :dp:`fls_tka0gth8rc9x`
     An :dt:`incomplete associated type` is an :t:`associated type` without an
     :t:`initialization type`.

.. glossary-entry:: initialization type
   :glossary-dp: fls_pd30dl2envjn
   
   :glossary:
     :dp:`fls_crn87nne7k38`
     An :dt:`initialization type` is the :t:`type` a :t:`type alias` defines a
     :t:`name` for.
     
     :dp:`fls_3r85y1lh1oxo`
     See :s:`InitializationType`.

:dp:`fls_w8nu8suy7t5`
An :t:`associated type` shall not be used in the :t:`path expression` of a
:t:`struct expression`.

:dp:`fls_wasocqdnuzd1`
An :t:`associated type` with a :s:`TypeBoundList` shall appear only as an
:t:`associated trait type`.

.. glossary-entry:: generic associated type
   :glossary-dp: fls_nooYIxMnV8Ps
   
   :glossary:
     :dp:`fls_O4wckPZPmree`
     A :dt:`generic associated type` is an :t:`associated type` with
     :t:`[generic parameter]s`.
   :chapter:
     :dp:`fls_PeD0DzjK57be`
     A :t:`generic associated type` is an :t:`associated type` with
     :t:`[generic parameter]s`.

:dp:`fls_3foYUch29ZtF`
A :t:`lifetime parameter` of a :t:`generic associated type` requires a
:t:`bound` of the form ``T: 'lifetime``, where ``T`` is a :t:`type parameter`
or :c:`Self` and ``'lifetime`` is the :t:`lifetime parameter`, when

* :dp:`fls_SnQc0zZS57Cz`
  The :t:`generic associated type` is used in an :t:`associated function` of
  the same :t:`trait`, and

* :dp:`fls_6Z05BK2JSzpP`
  The corresponding :t:`lifetime argument` in the use is not the ``'static``
  :t:`lifetime` and has either an explicit :t:`bound` or an :t:`implied bound`
  that constrains the :t:`type parameter`, and

* :dp:`fls_AtItgS1UvwiX`
  The intersection of all such uses is not empty.

.. glossary-entry:: associated implementation constant
   :glossary-dp: fls_9mcx6h6irrlx
   
   :glossary:
     :dp:`fls_rfaxcrrrb5q9`
     An :dt:`associated implementation constant` is an :t:`associated constant` that
     appears within an :t:`implementation`.
   :chapter:
     :dp:`fls_l3iwn56n1uz8`
     An :t:`associated implementation constant` is an :t:`associated constant` that
     appears within an :t:`implementation`.

:dp:`fls_4ftfefcotb4g`
An :t:`associated implementation constant` shall have a :t:`constant
initializer`.

.. glossary-entry:: associated implementation function
   :glossary-dp: fls_n85fwe75ku60
   
   :glossary:
     :dp:`fls_7xbmvl3jrc27`
     An :dt:`associated implementation function` is an :t:`associated function` that
     appears within an :t:`implementation`.
   :chapter:
     :dp:`fls_qb5qpfe0uwk`
     An :t:`associated implementation function` is an :t:`associated function` that
     appears within an :t:`implementation`.

:dp:`fls_1zlkeb6fz10j`
An :t:`associated implementation function` shall have a :t:`function body`.

.. glossary-entry:: associated implementation type
   :glossary-dp: fls_c0hekhwpznyq
   
   :glossary:
     :dp:`fls_6g5t81gx9ayx`
     An :dt:`associated implementation type` is an :t:`associated type` that appears
     within an :t:`implementation`.
   :chapter:
     :dp:`fls_tw8u0cc5867l`
     An :t:`associated implementation type` is an :t:`associated type` that appears
     within an :t:`implementation`.

:dp:`fls_bx7931x4155h`
An :t:`associated implementation type` shall have an :t:`initialization type`.

.. glossary-entry:: associated trait item
   :glossary-dp: fls_J946yIcmlAyV
   
   :glossary:
     :dp:`fls_IlRrVLm05GTf`
     An :dt:`associated trait item` is an :t:`associated item` that appears
     within a :t:`trait`.
   :chapter:
     :dp:`fls_bnTcCbDvdp94`
     An :t:`associated trait item` is an :t:`associated item` that appears
     within a :t:`trait`.

.. glossary-entry:: associated trait implementation item
   :glossary-dp: fls_47xtji9Pk8Lw
   
   :glossary:
     :dp:`fls_PaENehzTVgfB`
     An :dt:`associated trait implementation item` is an :t:`associated item` that
     appears within a :t:`trait implementation`.
   :chapter:
     :dp:`fls_N3cdn4lCZ2Bf`
     An :t:`associated trait implementation item` is an :t:`associated item` that
     appears within a :t:`trait implementation`.

.. glossary-entry:: associated trait constant
   :glossary-dp: fls_8p8teeamua55
   
   :glossary:
     :dp:`fls_xhhsej8db74y`
     An :dt:`associated trait constant` is an :t:`associated constant` that appears
     within a :t:`trait`.
   :chapter:
     :dp:`fls_x564isbhobym`
     An :t:`associated trait constant` is an :t:`associated constant` that appears
     within a :t:`trait`.

.. glossary-entry:: associated trait function
   :glossary-dp: fls_4h7s8u1zumnq
   
   :glossary:
     :dp:`fls_r927r0pdkb6h`
     An :dt:`associated trait function` is an :t:`associated function` that appears
     within a :t:`trait`.
   :chapter:
     :dp:`fls_b6nns7oqvdpm`
     An :t:`associated trait function` is an :t:`associated function` that appears
     within a :t:`trait`.

:dp:`fls_2TRwCz38kuRz`
An :t:`associated trait function` shall not be subject to :t:`keyword` ``const``.

:dp:`fls_WnsVATJvUdza`
Every occurrence of an :t:`impl trait type` in the :t:`return type` of an
:t:`associated trait function` is equivalent to referring to a new
anonymous :t:`associated trait type` of the :t:`implemented trait`.

.. glossary-entry:: associated trait type
   :glossary-dp: fls_azz308k3ra99
   
   :glossary:
     :dp:`fls_dndsgkiq9r7i`
     An :dt:`associated trait type` is an :t:`associated type` that appears within
     a :t:`trait`.
   :chapter:
     :dp:`fls_yyhebj4qyk34`
     An :t:`associated trait type` is an :t:`associated type` that appears within
     a :t:`trait`.

:dp:`fls_kl9p3ycl5mzf`
An :t:`associated trait type` shall not have an :t:`initialization type`.

:dp:`fls_a5prbmuruma4`
An :t:`associated trait type` has an implicit :std:`core::marker::Sized`
:t:`bound`.

:dp:`fls_vp2ov6ykueue`
An :t:`associated trait type` of the form

.. code-block:: rust

   	trait T {
   	    type X: Bound;
   	}

:dp:`fls_5uf74nvdm64o`
is equivalent to a :t:`where clause` of the following form:

.. code-block:: rust

   	trait T where Self::X: Bound {
   	    type X;
   	}

.. glossary-entry:: associated trait implementation function
   :glossary-dp: fls_fufF4UmzLg5G
   
   :glossary:
     :dp:`fls_bzdXloUGlVSC`
     An :dt:`associated trait implementation function` is an :t:`associated function`
     that appears within a :t:`trait implementation`.
   :chapter:
     :dp:`fls_amWtS80fPtza`
     An :t:`associated trait implementation function` is an :t:`associated function`
     that appears within a :t:`trait implementation`.

:dp:`fls_Cu8FWrisrqz1`
Every occurrence of an :t:`impl trait type` in the :t:`return type` of an
:t:`associated trait implementation function` is equivalent to referring to the
corresponding :t:`associated trait type` of the corresponding :t:`associated
trait function`.

.. glossary-entry:: method
   :glossary-dp: fls_bi3g8xkk9ekf
   
   :glossary:
     :dp:`fls_n4opbiofu9q6`
     A :dt:`method` is an :t:`associated function` with a :t:`self parameter`.
   :chapter:
     :dp:`fls_oy92gzxgc273`
     A :t:`method` is an :t:`associated function` with a :t:`self parameter`.

:dp:`fls_WXnCWfJGoQx3`
The type of a :t:`self parameter` shall be one of the following:

* :dp:`fls_OaszUw4IFobz`
  A :t:`type specification` resolving to the :t:`implementing type` of the
  related :t:`implementation`, or

* :dp:`fls_Wd2FZRomB5yn`
  ``&T`` where ``T`` is one of the :t:`[type]s` listed in this enumeration,
  or

* :dp:`fls_lcEyToYIlcmf`
  ``&mut T`` where ``T`` is one of the :t:`[type]s` listed in this
  enumeration, or

* :dp:`fls_IKSPR7ZQMErU`
  :std:`core::pin::Pin<T> <core::pin::Pin>` where ``T`` is one of the :t:`[type]s` listed in this
  enumeration.

:dp:`fls_oHxzyaiT7Qm6`
The :t:`visibility modifier` of an :t:`associated trait item` or :t:`associated
trait implementation item` is rejected, but may still be consumed by
:t:`[macro]s`.

.. rubric:: Examples

.. code-block:: rust

   trait Greeter {
       const MAX_GREETINGS: i32;

       fn greet(self, message: &str);
   }

   struct Implementor {
       delivered_greetings: i32
   }

   impl Greeter for Implementor {
       const MAX_GREETINGS: i32 = 42;

       fn greet(mut self, message: &str) {
           if self.delivered_greetings < Self::MAX_GREETINGS {
               self.delivered_greetings += 1;
               println!("{}", message);
           }
       }
   }

:dp:`fls_znfADVeOvXHD`
Generic associated type with lifetime bound.

.. code-block:: rust

   trait LendingIterator {
       type Item<'x> where Self: 'x;

       fn next<'a>(&'a mut self) -> Self::Item<'a>;
   }
