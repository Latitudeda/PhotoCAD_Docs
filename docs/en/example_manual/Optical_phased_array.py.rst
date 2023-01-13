Example: Optical Phased Array
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The integrated optical phased array (OPA) enables low-loss beam steering compared to the Bulk optics system and has applications in the following areas:

* Sensing
* Imaging
* Light Detection and Ranging (LiDAR)
* Displays
* Telecommunications

**PhotoCAD** design automation platform is well suited for OPA design because it is developed and used in Python 3.X with a powerful ecosystem and third-party toolkit support, and can call on a variety of simulation software under Python 3.X to **update structural parameters and simulate in real time**. By learning how to create OPAs in code below, designers can extend simple design concepts to large designs that are easy to simulate.


Introduction
------------------------------------------
The optical phased array (OPA) consists of a split tree with each output connected to a ``tin_heater``, another port of the ``tin_heater`` will be connected to a ``GratingCoupler``, two ``electrical ports`` exist on each ``tin_heater``, and the ``electrical port`` is connected to the ``BondPad`` by the ``LinkBetween`` function.

Full script
-----------------------------------------
