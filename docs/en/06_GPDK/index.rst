gpdk (generic PDK)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**gpdk** is a package for creating parametric device layout units based on Python scripts in the PhotoCAD platform.

After creating a new project, you can find the complete contents of the gpdk package in the ``.venv_xxx`` > ``Lib`` > ``site-packages`` > ``gpdk`` of your current project, which contains subfolders:  ``components``, ``examples``, ``routing``, ``schematic``, ``symbols``, ``technology``, ``util`` and other folders.

``components``: Stores the built-in parametric photonic components of ``gpdk``. These components are implemented as PCells and are used to generate the actual layout geometries of photonic devices. The official documentation gives examples including ``Straight``, ``bend_circular``, ``Taper``, ``Transition``, ``grating_coupler``, and ``MMI``.

``examples``: Stores example scripts and functional design templates provided with ``gpdk``. These examples demonstrate how PhotoCAD components and functions are called in actual designs. Users can run these scripts to learn the corresponding design methods and obtain the generated layout results.

``routing``: Stores the routing functions used to connect device ports and construct waveguide connections. The official examples include ``AutoTransitioned``, ``CompScan``, ``Extended``, and other functions.

``schematic``: Defines the schematic-level representation and interfaces of PDK components, including their ports, parameters, properties, and circuit connections. It also provides interfaces for converting schematic circuits into layouts and simulations.

``symbols``: Contains the symbol definitions used in schematic design. Each symbol provides a schematic representation of a corresponding photonic component, allowing devices to be displayed and connected in the schematic environment while being associated with their corresponding layout components.

``technology``: Stores the technology and process definitions of ``gpdk``, including layer definitions, waveguide types, technology parameters, and other process-related configurations. This folder determines how the components are constructed according to the target fabrication process.

``util``: Contains the configuration files for ``gpdk``.

.. image:: image/gpdk_1.png

.. toctree::

 technology
 routing
