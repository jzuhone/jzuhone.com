:title: Mixing of the ICM and Gas Heating
:status: hidden
:url: research/mixing/
:save_as: pages/research/mixing.html

As clusters of galaxies merge with each other, the gas undergoes significant heating. This is accomplished by shocks, the dissipation of turbulence, and the mixing of gases of different entropies. The degree to which these processes are able to efficiently heat the ICM is somewhat dependent on the microphysical properties of the ICM. My work in this area has focused on the effectiveness of gas mixing under different assumptions of the gas physics. The question of how the cluster gas is heated is an important once, since clusters largely fall into two distinct groups, those with a "cool" core (a temperature decline toward the cluster center due to the radiative cooling of the gas) and those without. The formed is believed to be the more "relaxed" state of galaxy clusters, so what is it that transforms a cluster from this state into one with a hotter core temperature?

Some previous simulation works have argued that gas mixing is
ineffective in cluster mergers, and therefore this is not an important
process for heating the ICM (`Ritchie & Thomas
2001 <http://adsabs.harvard.edu/abs/2002MNRAS.329..675R>`_, `Poole et al
2009 <http://adsabs.harvard.edu/abs/2008MNRAS.391.1163P>`_). These
simulations utilized one particular method for simulating
hydrodynamics, the Lagrangian `smoothed particle hydrodynamics (SPH)
method <http://en.wikipedia.org/wiki/Smoothed_particle_hydrodynamics>`_. This
method has been shown in some instances to artificially suppress fluid instabilities and gas mixing. `Mitchell et al 2009 <http://adsabs.harvard.edu/abs/2009MNRAS.395..180M>`_ performed identical cluster merger simulations using the SPH code `Gadget <http://www.mpa-garching.mpg.de/gadget/>`_ and the `Eulerian <http://en.wikipedia.org/wiki/Continuum_mechanics#Eulerian_description>`_ code `FLASH <http://flash.uchicago.edu>`_, demonstrating that the temperature and entropy of the merger remnant's core were much higher in the FLASH simulation, and attributed this difference to the efficient mixing of the gas of the two clusters in this simulation.

In `ZuHone 2011 <http://adsabs.harvard.edu/abs/2011ApJ...728...54Z>`_, I presented the results of a series of merger simulations with varying mass ratio and impact parameter, focusing specifically on the mixing of the gas and the resulting increase in entropy of the cluster core. I found that in all cases mixing and gas heating is very efficient. Volume-rendered movies of the behavior of the gas and dark matter components, as well as a variable that tracks the mixing of the gas are presented below.

.. raw:: html

  <div align="center">

  <iframe src="http://player.vimeo.com/video/64479138?title=0&amp;byline=0&amp;portrait=0"
  width="300" height="275" frameborder="0" webkitAllowFullScreen mozallowfullscreen
  allowFullScreen></iframe>

  <iframe src="http://player.vimeo.com/video/64479274?title=0&amp;byline=0&amp;portrait=0"
  width="300" height="275" frameborder="0" webkitAllowFullScreen mozallowfullscreen
  allowFullScreen></iframe>

  <iframe src="http://player.vimeo.com/video/64479137?title=0&amp;byline=0&amp;portrait=0"
  width="300" height="275" frameborder="0" webkitAllowFullScreen mozallowfullscreen
  allowFullScreen></iframe>

  <iframe src="http://player.vimeo.com/video/64532445?title=0&amp;byline=0&amp;portrait=0"
  width="300" height="275" frameborder="0" webkitAllowFullScreen mozallowfullscreen
  allowFullScreen></iframe>

  <iframe src="http://player.vimeo.com/video/66967617?title=0&amp;byline=0&amp;portrait=0"
  width="300" height="275" frameborder="0" webkitAllowFullScreen mozallowfullscreen
  allowFullScreen></iframe>

  <iframe src="http://player.vimeo.com/video/64756388?title=0&amp;byline=0&amp;portrait=0"
  width="300" height="275" frameborder="0" webkitAllowFullScreen mozallowfullscreen
  allowFullScreen></iframe>

  </div>

However, the efficiency of mixing and the resulting increase in entropy can be inhibited by more complex gas physics. In `ZuHone et al 2010 <http://adsabs.harvard.edu/abs/2010ApJ...717..908Z>`_ and `ZuHone et al 2011 <http://adsabs.harvard.edu/abs/2011ApJ...743...16Z>`_, I examined the phenomenon of gas sloshing in the cores of galaxy clusters. Even though this is the result of more gentle interactions with smaller subclusters, it is still capable of mixing hot gas from higher radii in the cluster with the core gas, raising its temperature and entropy. These simulations showed that this mixing is strongly inhibited by viscosity and magnetic fields. In fact, simulations with a high core magnetic field or Spitzer-level viscosity showed essentially no change in the properties of the cluster core after the sloshing period. More investigations of this phenomena are necessary to understand to what degree mixing in the ICM is suppressed due to some combination of magnetic fields and viscosity.
