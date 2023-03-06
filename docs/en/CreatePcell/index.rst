Create Parametrized Cell(PCell)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section is a tutorial for users how to create Pcells from the basic components of a photonics integrated circuits.

In the first section ``BendEuler``, the Pcell is created by several geometries (curves) to generate the shape of the cell, some other examples can be found in ``Straight``, ``Taper``.

The second section ``Splitter`` is created by the Pcells generated in the first section by defining the parameters and locations of each PCells in section I, then connect them together to generate a Pcell with a higher level.

Finally, the third section ``Mzm`` is created by calling the Pcells either in section I or II and then defining parameterizable parameters, rearranging and connecting them to generate the PCell with the highest level.

.. toctree::
 bendeuler
 splitter
 mzm
 fpPinPort
