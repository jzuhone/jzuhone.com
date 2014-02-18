:title: Scientific Education
   
Communicating Science Using the IPython Notebook
------------------------------------------------

.. |unworked link| raw:: html

   <a
   href="http://nbviewer.ipython.org/url/jzuhone.com/files/Kepler_Unworked.ipynb"
   target="_blank">You can see the full unworked example of the problem set here.</a>

.. |worked link| raw:: html

   <a
   href="http://nbviewer.ipython.org/url/jzuhone.com/files/Kepler_Worked.ipynb"
   target="_blank">Here is the same notebook where the answers have
   been worked out.</a>

.. |full source| raw:: html

   <a href="http://github.com/jzuhone/ipynb_hw" target="_blank">To get
   the full source and run the notebook on your own system, go here.</a>

I've been doing some thinking recently about new approaches to
teaching science. Since I am big into `Python <http://www.python.org>`_, I'm naturally wondering
how we can use this simple yet powerful scripting/programming language
in this way. 

Interacting with scientific concepts in a 'hands-on' way is the best way to really
understand them, which is why labs are a crucial component of science
education. "Virtual experiments" involving are another option, especially for
astronomy, since it's not exactly easy to make a solar system in a
classroom! 

Python is an ideal language for designing and implementing such experiments, not only because of its simplicity and power but also because of the wide variety of scientific software libraries made for it. The combination of `NumPy <http://www.numpy.org>`_ and `SciPy <http://www.scipy.org>`_ allow nearly any computation to be carried out in Python, and `Matplotlib <http://matplotlib.org>`_ is a versatile plotting library. 

However, the key to really making interactive examples work is the `IPython Notebook <http://ipython.org/notebook.html>`_, a "web-based interactive computational environment where you can combine code execution, text, mathematics, plots and rich media into a single document." Homework sets or labs could be designed in Python, then loaded up on a notebook which could be executed by each student on a server. The examples could be worked out in the notebook itself, and the answers could also be typed in the notebook. 

Suppose, for example, that you wanted to teach `Kepler's laws of
planetary motion
<http://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion>`_
in a way that actually gave the students a chance to "see" the laws in
action. One way to do that would be to set up a simulation of a planet
orbiting a star, and let students interact with it to examine the
different aspects of orbital motion. In other words, the students
would be tasked with changing the initial conditions of the orbit and
seeing how this changed (or didn't change) aspects of the orbit's
properties. I have designed a mock problem set for demonstrating this functionality.

|unworked link|

|worked link| (Sorry, it takes a little while to completely load.)

|full source|

Here is a small snippet of this problem set, where the answer has been worked out:


------------

.. include:: problem2.txt

------------


Clearly, this idea needs a lot of work and more thought put into it to
work out the kinks and make it as simple as necessary for students to use, but I think it's a very intriguing start.
