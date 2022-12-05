Welcome to PhotoCAD's documentation!
===================================

**PhotoCAD** is a computer-aided design platform for photonic
integrated circuit layout design based on Python language. The PhotoCAD
platform includes two tools-pPCell, or photonic PCell and pLink, or
photonic Link, which correspond to the parametric device layout design
and the circuit-level layout design of the photonic integrated circuit layout
design.

PhotoCAD is written in Python language, which is widely used in the
industry. The algorithm for generating layouts has been carefully
researched and specially optimized by photonic integrated circuit
designers. It has unique advantages among similar tools worldwide, such
as no distortion of layout at any angle, tearing and other issues.

pPCell is a tool for parametric component layout design in the
PhotoCAD platform. It covers the common active and passive components
in current photonic integrated chips. The waveguide used in the
components covers FWG (Full etch waveguide) and MWG (Medium etch
waveguide), and SWG (Shallow etch waveguide) types. In pPcell, all
parameterized components (i.e. Parameterized Cell, PCell) are defined in
the function through Python scripts, and the user can flexibly adjust the
parameters in the function to achieve a specific cell when calling and using
it in a component layout design.

pLink is a tool for automatic component interconnection design in the
PhotoCAD platform. In addition to instantiating the components and
setting the placement of the components in the script, the user can also
use pLink to complete the automatic interconnection design of the
components through a simple port connection definition. pLink will call
the corresponding waveguide transition unit according to the waveguide
type of the component port to realize the transition of the waveguide type
at the port, and instantiate the corresponding straight and bend
waveguides to complete the connection between the component ports
according to the position of the component port.

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is under active development.

Contents
--------

.. toctree::

   usage
   api
