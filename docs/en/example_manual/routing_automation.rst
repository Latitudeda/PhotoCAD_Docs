Routing automation between components ports
===================================================

``fp.Linked``, a functional module for port routing automation, is included in **PhotoCAD**. This module automates the routing of components in a layout by defining port connections in a Python script. For ports that require waveguide transition, the tool automatically selects the appropriate waveguide transition unit to convert the different waveguide types. After running the script file, a local folder is created to store the generated GDS, netlist, etc.



.. toctree::

 example_linked.py
 example_linked_elec.py
