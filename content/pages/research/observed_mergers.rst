:title: Simulating Observed Cluster Mergers
:status: hidden
:url: research/observed_mergers
:save_as: pages/research/observed_mergers.html

Reproducing the properties of observed galaxy cluster mergers is an
essential task for numerical simulations. This is especially the case
if quality data exists in a number of wavebands. Reproducing specific
mergers aids in the interpretation of observed data and helps to
constrain models for the underlying physics of the cluster galaxies,
gas, and dark matter. 

.. figure:: {filename}/images/cl0024_image.png
   :align: right
   :width: 100%
   :figwidth: 300px

   Figure 1: Mock counts image of our simulated clusters.

In this vein, I performed simulations of the cluster Cl0024+17, which
is believed to be a high-velocity merger of two clusters that is
occuring along the line of sight. This interpretation is supported by
optical (`Czoske et al 2002 <http://adsabs.harvard.edu/abs/2002A%26A...386...31C>`_) and X-ray (`Ota et al 2004 <http://adsabs.harvard.edu/abs/2004ApJ...601..120O>`_) data. 

The former indicates a superposition of two distinct groups of cluster galaxies
in redshift space, separated by a relative velocity of ~3000 km/s. The
latter indicates a superposition of two X-ray surface brightness
components. In `ZuHone et al 2009a <http://adsabs.harvard.edu/abs/2009ApJ...699.1004Z>`_, using mock Chandra observations (Figure 1), we showed that in such a merger scenario the X-ray surface brightness profile of the system is much better fit by a superposition of two cluster model profiles rather that one (Figure 2).

Using these profiles and the temperature profile of the system, we
showed that (in accordance with observations) the estimated
hydrostatic mass of the system is accurately determined (to within
~20%) by assuming the existence of these two components, which is also
in accordance with the existing X-ray observations and the weak
lensing mass reconstrction of `Jee et al 2007 <http://adsabs.harvard.edu/abs/2007ApJ...661..728J>`_.

.. figure:: {filename}/images/model_fits.png
   :figwidth: 100 %

   Figure 2: Model fits to our clusters' surface brightness profile. Left: One model fit 
   and residuals. Right: Two-model fit and residuals.

The weak lensing mass reconstruction of `Jee et al 2007
<http://adsabs.harvard.edu/abs/2007ApJ...661..728J>`_ suggested the
existence of a "ring" of dark matter surrounding the system. They
suggested that the ring feature could be the result of such a
collision, and produced a cluster merger simulation which resulted in
the formation of a dark matter ring when viewed in projection along
the merger axis. To determine under what conditions such a feature
would form, in `ZuHone et al 2009b <http://adsabs.harvard.edu/abs/2009ApJ...696..694Z>`_ we performed a suite of simulations of the merger scenario for Cl0024+17, varying the velocity anisotropy of the dark matter particles. We found that distinct dark matter rings only formed when the velocity dispersion tensor of the dark matter particles was highly tangentially anisotropic (Figure 3). This is in strong conflict with simulations of the formation of dark matter halos from cosmological simulations, indicating that an explanation is lacking for the formation of the suggested dark matter ring in Cl0024+17.

.. figure:: /images/dmring.png
   :figwidth: 100 %

   Figure 3: A dark matter ring forming in a cluster merger collision where the
   particles have initially mostly tangential velocities.

