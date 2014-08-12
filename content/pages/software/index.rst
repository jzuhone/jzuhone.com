:title: Scientific Software

.. _S-Z Effect: software/mock_SZ.html
.. _X-rays: software/photon_simulator.html
.. _Particles: software/flash_particles.html

Here are some examples of scientific simulation and analysis software
that I have made significant contributions to.

`My code on Bitbucket <http://bitbucket.org/jzuhone>`_

`My code on GitHub <http://github.org/jzuhone>`_

Mock Observations with `yt <http://yt-project.org>`_
-------------------------------------------------------------------------------

.. raw:: html

   <table align="left" style="font-size:12">
   <tr><td>
   <a href="http://yt-project.org/doc/analyzing/analysis_modules/sunyaev_zeldovich.html">S-Z Effect</a>
   </td>
   <tr><td>
   <a href="http://yt-project.org/doc/analyzing/analysis_modules/sunyaev_zeldovich.html"><img src="/images/sz_link.png" style="width:400px" /></a>
   </td>
   </tr>
   </table>

   <table align="left" style="font-size:12">
   <tr><td>
   <a href="http://yt-project.org/doc/analyzing/analysis_modules/photon_simulator.html">X-Rays</a>
   </td>
   <tr><td>
   <a href="http://yt-project.org/doc/analyzing/analysis_modules/photon_simulator.html"><img src="/images/photon_link.png"
   style="width:370px" /></a>
   </td>
   </tr>
   </table>

|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

``YT``, a Julia wrapper for ``yt``
----------------------------------

.. figure:: /images/ytjulia.png
   :align: left
   :width: 100%
   :figwidth: 200px

`Julia <http://julialang.org>`_ is an exciting new programming language for technical computing. Julia is fast due to its just-in-time compiler, and has most of the mathematical functionality for carrying out calculations for scientific computing built-in. 

To enable the analysis of astrophysical simulation data from within a Julia environment, I have written a package for Julia called ``YT``. ``YT`` exposes a number of the essential features of ``yt`` from within a Julia environment, including datasets, data containers, unit-aware quantities and arrays, and some of the plotting tools. 

To find out more visit http://www.jzuhone.com/yt_julia.

|
|
|

``pywwt``, a Python Interface for World Wide Telescope
------------------------------------------------------

.. figure:: /images/minihalo.png
   :align: right
   :width: 100%
   :figwidth: 200px

``pywwt`` is a Python interface for the Microsoft `World Wide Telescope <http://www.worldwidetelescope.org>`_
(WWT) Windows client, using the
`Layer Control API (LCAPI) <http://www.worldwidetelescope.org/Developers/?LayerControlAPI#load>`_.

The LCAPI provides an interface to WWT's Layer Manager by sending data and information in the form of strings over HTTP. ``pywwt`` simply provides a Python interface to make these
calls, enabling the control of WWT from scripts or an IPython notebook. Most importantly, it enables the passing of data created within a Python environment to
WWT.

To find out more visit http://www.jzuhone.com/pywwt.
