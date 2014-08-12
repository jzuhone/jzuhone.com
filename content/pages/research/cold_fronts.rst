:title: Constraining the Transport Processes of the Intracluster Medium with Cold Fronts
:status: hidden
:url: research/cold_fronts/
:save_as: pages/research/cold_fronts.html

The latest generation of X-ray telescopes, including *Chandra* and
*XMM-Newton*, have revealed the existence of sharp surface brightness
discontinuities which betray the existence of sharp density jumps in
the intracluster medium (ICM) Spectral analysis demonstrates that
these are also jumps in temperature, with the denser side of the front
having a lower temperature. These features have been dubbed "cold
fronts" (for an extensive review see `Markevitch & Vikhlinin 2007
<http://adsabs.harvard.edu/abs/2007PhR...443....1M>`_). Simulations
indicate that cold fronts may form from merging activity, whether by
ram-pressure stripping or "ram-pressure slingshots" of cool, dense
gas. Cold fronts should be susceptible to heat conduction, which would
elminate the sharp temperature gradient on a short timescale, and
fluid instabilities, such as Kelvin-Helmholtz (K-H), which would
disrupt their smooth appearance.

.. raw:: html

   <table align="right" style="font-size:13px">
   <tr><td>
   <iframe src="http://player.vimeo.com/video/78989618?title=0&amp;byline=0&amp;portrait=0" width="300"
   height="275" align="right" frameborder="0" webkitAllowFullScreen
   mozallowfullscreen allowFullScreen></iframe>
   </td>
   <tr><td>
   Magnetic field strength.
   </td>
   </tr>
   </table>

   <table align="right" style="font-size:13px">
   <tr><td>
   <iframe src="http://player.vimeo.com/video/78989362?title=0&amp;byline=0&amp;portrait=0" width="300"
   height="275" align="right" frameborder="0" webkitAllowFullScreen
   mozallowfullscreen allowFullScreen></iframe> 
   </td>
   </tr>
   <tr>
   <td>
   Gas temperature.
   </td>
   </tr>
   </table>

However, most cold fronts are observed to be very smooth and sharp, so there must be a mechanism to
support the existence of these features. One possible mechanism is magnetic fields. The velocity shear
associated with a cold front can amplify the weak cluster magnetic
fields to near-equipartition strengths, and stretch the field lines
tangential to the front surface. Due to the small Larmor radii of
electrons in the $\\mu$G cluster magnetic field, heat conduction is
strongly anisotropic, occurring essentially only along the field
lines. Therefore, a magnetic field stretched parallel to the front
surface would shield the temperature gradient from heat conduction.In `ZuHone et al 2011 <http://adsabs.harvard.edu/abs/2011ApJ...743...16Z>`_ we performed a series of simulations of sloshing cold front formation in a magnetized ICM. We varied the overall magnetic field strength of the cluster and the degree to which it is tangled on small scales. We found that for initial magnetic field energies ~1% of the thermal energy, the field is stretched and amplified to such a degree that most cold fronts can be stabilized against the development of fluid instabilities. Large-radii cold fronts, where the field is weaker, are more susceptible to the development of instabilities. 

.. figure:: /images/temps.png
   :width: 100%
   :figwidth: 300px

   Slices of gas temperature for simulations with different initial
   plasma $\\beta$. 

.. figure:: /images/bfields.png
   :width: 100%
   :figwidth: 300px

   Slices of plasma $\\beta$. As the initial magnetic field strength is increased, Kelvin-Helmholtz
   instabilities are increasingly suppressed.


However, we found that the ability of magnetic fields to suppress heat
conduction across cold fronts in this scenario is limited. In `ZuHone et al 2013 <http://adsabs.harvard.edu/abs/2013ApJ...762...69Z>`_ we re-simulated our magnetized sloshing cold fronts with anisotropic thermal conduction. We found that despite the formation of magnetic field lines draped tangentially to the front surfaces, conduction is not fully suppressed and the temperature jumps can be significantly reduced, to the point where the corresponding surface brightness jumps would not be seen in observations. This is due to the fact that the magnetic field layers are not perfectly aligned with the cold front surfaces, and some heat flux is able to "leak through." This potentially places strong constraints on heat conduction in the bulk of the ICM. 

Another candidate for preventing the development of fluid
instabilities at cold front surfaces is viscosity. Little is currently
known about the Reynolds number of the cluster plasma. Even a modest
isotropic ion viscosity is capable of preventing the development of
K-H instabilities at sloshing cold fronts, as was shown to a certain
extent by `ZuHone et al 2010
<http://adsabs.harvard.edu/abs/2010ApJ...717..908Z>`_ and in fuller
depth by `Roediger et al 2012 <http://adsabs.harvard.edu/abs/2013ApJ...764...60R>`_. 

However, for
similar reasons as conduction, the ion viscosity in the ICM should be
highly anisotropic. Therefore, the suppression of instabilities will
be weaker and dependent upon the magnetic field direction. In `ZuHone et al 2014 <http://arxiv.org/abs/1406.4031>`_, we performed a set of simulations of gas sloshing with magnetic fields and various models for viscosity. We found that the combination of even weak magnetic fields and Braginskii (anisotropic) viscosity is sufficient to produce cold fronts that are consistent with observations in terms of supressing K-H instabilties. We also found that this situation may be approximated by an isotropic Spitzer viscosity with a suppression factor of f ~ 0.1. However, we also showed that the effect of the magnetic field is crucial; even if the viscosity is the same, simulations with and without magnetic fields produce qualitatively different results in terms of the degree of disruption of cold front surfaces by instabilities. 

.. figure:: /images/virgo_temp.png
   :width: 100%
   :figwidth: 440px

   Temperature slices for simulations with different models for viscosity. The "Inviscid"
   results in prevalent K-H instabilities along most of the fronts, whereas the 
   simulations with viscosity suppress these instabilities to varying degrees. 
   
.. figure:: /images/virgo_counts.png
   :width: 100%
   :figwidth: 400px

   Synthetic counts images of the same simulations (created using `yt's synthetic X-ray
   observation simulator <http://yt-project.org/doc/analyzing/analysis_modules/photon_simulator.html>`_)
