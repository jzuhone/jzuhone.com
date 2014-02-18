:title: Unworked Kepler Example
:url: education/kepler_unworked
:save_as: education/kepler_unworked.html
:status: hidden

.. code:: python

    from hw_problems import KeplersLaws

.. code:: python

    hw = KeplersLaws()

Problem 1
=========


Call ``problem1`` with one number, which is the eccentricity ``e``.

Example: ``hw.problem1(e=0.2)``

a) Try several different values of ``e`` within the range of 0 to 1 but
   **not** equal to 1. What shape is the orbit in general? What is the
   shape if ``e`` = 0?

b) Try setting ``e`` = 1. What is the shape of the orbit in this case?
   Is the planet bound to the star?

c) Repeat (b) but with values of ``e`` > 1.



Problem 2
=========


Call ``problem2`` with five numbers, in this order:

``e``: the eccentricity
``t1``: the first time marker
``t2``: the second time marker
``t3``: the third time marker
``t4``: the fourth time marker

Example: ``hw.problem2(e=0.3, t1=0.1, t2=0.2, t3=0.7, t4=0.8)``

a) Set ``e`` to a value between 0 and 1, choosing one of the values you
   used in Problem 1. Next, pick values for the time markers, such that:

-  they are all less than the time it takes to complete one orbit for
   the given ``e``
-  ``t2-t1`` and ``t4-t3`` are equal.

So, for example, you could choose ``e`` = 0.5, and ``t1`` = 0.1, ``t2``
= 0.2, ``t3`` = 0.7, and ``t4`` = 0.8, since ``t2-t1`` = ``t4-t3`` =
0.1.

Try this exercise several times for different values of ``e`` and the
time markers. Note the areas swept out by the planet in these time
intervals. Then, try unequal time intervals. What is the difference in
the areas when the time intervals are equal and when they are different?

b) Try (a) for a value of ``e`` greater than or equal to 1. Are the
   results same or different?

c) What physical principle does this illustrate?



Problem 3
=========


Call ``problem3`` with just the eccentricity ``e``.

Example: ``hw.problem3(e=0.5)``

a) Try this for several different values of ``e``. What is the
   relationship between the semi-major axis :math:`a` in AU and the
   orbital period :math:`P` in years? In other words, what is :math:`x`
   such that :math:`P = a^x`?

b) Using the following values of the orbital periods for the eight
   planets, compute the value of the semi-major axis for each:

\| Planet \| Period (years) \| \|------------\|----------------\| \|
Mercury \| 0.24 \| \| Venus \| 0.62 \| \| Earth \| 1.0 \| \| Mars \|
1.88 \| \| Jupiter \| 11.86 \| \| Saturn \| 29.46 \| \| Uranus \| 84.01
\| \| Neptune \| 164.8 \|

.. code:: python

    
