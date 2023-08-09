Get PCell information
=============================================

* PCell = ``device``

* Get PCell name: ``device.name``

* Get PCell region:

  * region = ``fp.get_bounding_box(device)``

    * (min_x, min_y), (max_x, max_y) = fp.get_bounding_box(device)


* Get ports information:

  * Get the number of ports:

    * Get total number of ports: ``len(device.ports)``

    * Get left ports: ``gpdk.port_util.get_left_ports(device)``

    * Get right ports: ``gpdk.port_util.get_right_ports(device)``

  * orientation: ``device[”op_0”].orientation``

  * waveguide_type: ``device[”op_0”].waveguide_type``

  * waveguide width: ``device[”op_0”].waveguide_type.core_width``

  * position (x, y): ``device[”op_0”].position[0]``, ``device[”op_0”].position[1]``


