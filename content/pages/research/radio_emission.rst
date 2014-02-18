:title: Turbulence, Particle Acceleration, and Radio Emission in Galaxy Clusters
:status: hidden
:url: research/radio_emission/
:save_as: pages/research/radio_emission.html

A number of galaxy clusters contain diffuse, steep-spectrum radio
emission. The most obvious of these are large, extended sources (R ~ 1
Mpc) that are often found in merging clusters, known as 'radio halos.'
There is a second class of these features, found in the cool cores of
more relaxed galaxy clusters (R ~ 100-200 kpc), known as 'radio
minihalos.' To be observed at frequencies of 100s of MHz to 1 GHz, the
radio emission must be produced by relativistic electrons with
energies $\\gamma \\sim 10^3 - 10^4$. Since the time for electrons to diffuse across the cluster is much longer than their radiative loss time at these energies, the electrons must either be reaccelerated by some process or continuously injected *in situ*. 

.. figure:: /images/accel.png
   :width: 100%
   :figwidth: 300px
   :align: left

   Electron spectra at different epochs in our simulation. The
   initial spectrum with few high-energy particles is
   transformed into a power-law spectrum extending to high
   energies.

.. raw:: html

   <table align="right" width="300px" style="font-size:13px">
   <tr><td>
   <iframe
   src="http://player.vimeo.com/video/78989700?title=0&amp;byline=0&amp;portrait=0"
   width="300" height="300" align="right" frameborder="0" webkitAllowFullScreen  mozallowfullscreen allowFullScreen></iframe>
   </tr>
   <tr><td>
   The evolution of radio emission at a frequency of 327 MHz.
   </tr>
   </table>

Relativistic electrons with energies $\\gamma \\sim 10^2$ may build
up in the cluster volume due to acceleration by AGN and shocks and
production via hadronic processes. These electrons may then be
reaccelerated by MHD turbulence driven by cluster
mergers. Relativistic particle reacceleration provides a natural
explanation for the steepening of the spectrum at high (~1 GHz)
frequencies seen in many halos and minihalos, due to the competition
of reacceleration and radiative losses. In a cool core cluster,
interactions with subclusters produce sloshing of the gas, which is
observed in the X-ray band as spiral-shaped cold fronts. `Mazzotta & Giacintucci 2008 <http://adsabs.harvard.edu/abs/2008ApJ...675L...9M>`_ discovered a correlation between sloshing cold fronts and radio minihalo emission in two galaxy clusters, and other examples have been found since. 

In line with this evidence, in `ZuHone et al 2013
<http://adsabs.harvard.edu/abs/2013ApJ...762...78Z>`_ we performed a
MHD simulation of gas sloshing in a cool-core cluster and included the
The sloshing produces MHD turbulence with $\\delta{v}$ ~ 200 km/s onlength scales of ~10 kpc, which we showed is capable of accelerating
relativistic electrons up to the energies required for producing a
minihalo. The spatial distribution of the radio surface brightness and
its spectrum are consistent with observed minihalos. In particular,
the minihalo emission is bounded by the sloshing cold fronts. Also,
the minihalo is produced on a very short timescale (< 1 Gyr) and
decays afterward. This is in line with the fact that not all cool-core
clusters possess minihalos. 

Work is currently underway to study the results of the interplay of
sloshing and the injection of relativistic electrons via hadronic
interactions as an alternative hypothesis for the existence of radio
mini-halos. In this scenario, the confinement of the radio emission to
the volume bounded by the cold fronts is explained by the
amplification of the magnetic field below the cold fronts `(Keshet &
Loeb 2010) <http://adsabs.harvard.edu/abs/2010ApJ...722..737K>`_.

.. figure:: /images/minihalo1.png
   :width: 100%
   :figwidth: 300px
   :align: center

   X-ray image of RXJ1720.1+26 with radio contours overlaid.

.. figure:: /images/minihalo2.png
   :width: 100%
   :figwidth: 307px

   Mock X-ray image with mock radio contours overlaid from our simulation. 

..
