Advanced Waveguide Routing
==================================

In this section, you can find:
1. Routing option for DOE(Design of Experiment) with placing multiple components together.
2. Method to extend the length of the existing PCell ports.
3. Expand the footprint to downstream devices(HFanout).
4. Horizontalized the ports.

These functions can be found in ``gpdk >> routing``.

.. toctree::

  wg_adv_routing_compscan
  wg_adv_routing_extended
  wg_adv_routing_hfanout
  wg_adv_routing_hori
  wg_adv_routing_linkbetween
  wg_adv_routing_linked
  wg_adv_routing_linksmooth


Moreover, users are allowed to define their own waveguide connections, e.g, bend types, tapers, transitions, routing algorithm by:

1. Self-defined bend types and assign to ``bend_factory`` parameter in ``fp.LinkBetween``.
2. Connect different types of ports with auto transitions and bends.
3. Define control points and generate curved line for specific routing.


