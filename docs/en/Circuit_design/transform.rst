Common used transformation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transformation functions are useful when one needs to move or mirror the instance(PCells) to other places. These functions can be used for the PCells multiple times and combine them together.

1. translated_
2. scaled_
3. rotated_
4. mirrored_

translated
^^^^^^^^^^^^^^^^^^

* Usage: insts.translated()
* parameters: tx, ty
* ``DirectionalCouplerBend().translated(10, 10)``: origin of the cell is translated to (10, 10).
* The origin of the cell can be defined in the PCell

scaled
^^^^^^^^^

* Usage: insts.scaled()
* parameters: sx, sy
* ``DirectionalCouplerBend().scaled(3)``: the cell is magnify both x and y coordinate to three times larger than origin.
* ``DirectionalCouplerBend().scaled(3, 2)``: the cell is magnify three time larger on the x-axis and two times larger on the y-axis than origin.

rotated
^^^^^^^^

* Usage: insts.rotated()
* parameters: degrees, radians, origin
* ``DirectionalCouplerBend().rotated(degrees=90)``: the cell rotated 90 degree based on the origin of the cell.

mirrored
^^^^^^^^^^^^^^^

* Usage: insts.*_mirrored()

* c_mirrored(): mirroring the cell with regard to the origin (0, 0).

* v_mirrored(): mirroring the cell with regard to the y-axis.

* h_mirrored(): mirroring the cell with regard to the x-axis.