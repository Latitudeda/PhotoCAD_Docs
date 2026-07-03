.. _com_straight :

Straight
=======================

The straight waveguide is one of the most fundamental building blocks in photonic integrated circuits. 

Basic Usage
------------------

The simplest way to create a straight waveguide is to instantiate the ``Straight`` class with desired parameters::

    from gpdk.technology import get_technology
    import fnpcell.all as fp
    from gpdk import all as pdk

    TECH = get_technology()

    # Create a 10μm straight waveguide using default settings
    straight = pdk.Straight( length=10, waveguide_type=TECH.WG.FWG.C.WIRE)

    # Plot the layout
    fp.plot(straight)

.. image:: image/straight_1.png

This produces a straight waveguide segment with optical ports at both ends.

Parameters Reference
---------------------------

The ``Straight`` class accepts the following arguments to customize its geometric and structural properties:

.. list-table:: 
   :widths: 20 20 35
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``length``
     - ``10``
     - The physical length of the waveguide in micrometers. Must be non-negative.
   * - ``waveguide_type``
     - ``FWG.C.WIRE``
     - The waveguide definition (core/cladding materials, width, etc.). Defaults to the technology's standard wire waveguide.
   * - ``anchor``
     - ``Anchor.START``
     - Controls where the origin of the cell is placed. Options: ``START``, ``CENTER``, ``END``.
   * - ``port_names``
     - ``("op_0", "op_1")``
     - A sequence containing custom names assigned to the input and output ports.


Connecting Two Coordinates
---------------------------------

Often, you will need to generate a straight waveguide that bridges two arbitrary coordinates dynamically. PhotoCAD provides a convenient utility function, ``StraightBetween``, for this exact scenario.

.. note::
   ``StraightBetween`` is not a separate component class. It is a wrapper function that calculates the required length and angle, internally instantiates the base ``Straight`` class, and applies the necessary rotation and translation to connect the two points.

.. code-block:: python

    def StraightBetween(
        *,
        start: fp.Point2D = (0, 0),
        end: fp.Point2D,
        waveguide_type: fp.IWaveguideType,
        port_names: fp.IPortOptions = ("op_0", "op_1"),
    ):
        """Create a straight waveguide exactly between two points."""
        length = fp.distance_between(end, start)
        orientation = fp.angle_between(end, start)
        straight = Straight(
            length=length, 
            waveguide_type=waveguide_type, 
            port_names=port_names
        ).rotated(radians=orientation).translated(start)
        return straight

**StraightBetween Parameters**

.. list-table:: 
   :widths: 20 20 35
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``start``
     - ``(0, 0)``
     - The starting coordinate (``fp.Point2D``) of the waveguide.
   * - ``end``
     - *Required*
     - The ending coordinate (``fp.Point2D``) of the waveguide.
   * - ``waveguide_type``
     - *Required*
     - The waveguide definition (core/cladding materials, width, etc.) to apply.
   * - ``port_names``
     - ``("op_0", "op_1")``
     - A sequence containing custom names assigned to the input and output ports.
     
**Example usage:**

.. code-block:: python

    s = StraightBetween(
        start=(0, 0),
        end=(100, 50),
        waveguide_type=TECH.WG.FWG.C.WIRE
    )

.. image:: image/straight_2.png

Anatomy of the Class
-------------------------------------------

To understand how PhotoCAD constructs components internally, it is highly instructive to look at the class definition. This component is heavily used internally by the routing engine and forms the backbone of most photonic layouts.

**1. The Raw Curve**

Every basic waveguide component should define a ``raw_curve`` property. This geometric primitive is used by routing functions (``Linked``, ``LinkBetween``, etc.) to automatically compute lengths and place components.

.. code-block:: python

    @cached_property
    def raw_curve(self):
        """Define the geometric path of the waveguide."""
        return fp.g.Line(
            length=self.length,
            anchor=self.anchor,
        )

When using routing functions, PhotoCAD will calculate the length between two ports and assign proper components based on this curve.

**2. Building the Layout**

Finally, the ``build()`` method assembles the layout by creating a waveguide instance from the chosen type and curve, adding the instance, and renaming ports.

.. code-block:: python

    def build(self) -> Tuple[fp.InstanceSet, fp.ElementSet, fp.PortSet]:
        """Build the layout by instantiating the waveguide."""
        insts, elems, ports = super().build()
        wg = self.waveguide_type(curve=self.raw_curve)
        insts += wg
        
        # Iterating through default ports to rename them based on user input
        ports += [port.with_name(self.port_names[i]) for i, port in enumerate(wg.ports)]
        return insts, elems, ports