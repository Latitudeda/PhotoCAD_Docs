Get PCell information
=============================================

* PCell = ``device``

* Get PCell name: ``device.name``

* Get PCell region:

  * region = ``fp.get_bounding_box(device)``

    * x_min = ``region[0][0]``
    * x_max = ``region[0][1]``
    * y_min = ``region[1][0]``
    * y_max = ``region[1][1]``


* Get ports information:

  * Get the number of ports:

    * Get total number of ports: ``len(device.ports)``

    * Get left ports: ``port_util.get_left_ports(device)``

    * Get right ports: ``port_util.get_right_ports(device)``

  * orientation: ``device[”op_0”].orientation``

  * waveguide_type: ``device[”op_0”].waveguide_type``

  * waveguide width: ``device[”op_0”].waveguide_type.cor_width``

  * position (x, y): ``device[”op_0”].position[0]``, ``device[”op_0”].position[1]``


