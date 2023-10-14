Get PCell information
=============================================

* PCell = ``device``

Get PCell name
-----------------
* name = ``device.name``

Get PCell region
--------------------

* region = ``fp.get_bounding_box(device)``

    * (min_x, min_y), (max_x, max_y) = fp.get_bounding_box(device)


Get ports information
--------------------------

* Get the number of ports:

    * Get total number of ports: ``len(device.ports)``

    * Get left ports: ``gpdk.port_util.get_left_ports(device)``

    * Get right ports: ``gpdk.port_util.get_right_ports(device)``

* orientation: ``device[”op_0”].orientation``

* waveguide_type: ``device[”op_0”].waveguide_type``

* waveguide width: ``device[”op_0”].waveguide_type.core_width``

* position (x, y): ``device[”op_0”].position[0]``, ``device[”op_0”].position[1]``


Get two points relative information
----------------------------------------

Here we would like to know some information e.g. distance, angle, between two points(points can be acquired by ``curve_points`` of a curve or the position of the ports)


* Distance of the two points: ``fp.distance_between(pointA, pointB)``
* Middle point of the two points: ``fp.midpoint_between(pointA, pointB)``
* Angle between two points: ``fp.angle_between(pointA, pointB)``
    * This function returns the radian of the angle.



