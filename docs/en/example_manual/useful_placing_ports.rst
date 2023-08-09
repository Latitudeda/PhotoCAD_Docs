Placing PCell ports
==============================================================================================


* ``new_device_A = fp.place(device_A, “port_A”, at=device_B[”port_B”])``

     In this method, the two ports will be connected.

* ``new_device_A = fp.place(device_A, “port_A”, at=device_B[”port_B”].position)``

     In this method, ``port_A`` will be placing at the position of ``port_B`` but remaining the port orientation.

* ``new_device_A = fp.place(device_A, “port_A”, at=device_B[”port_B”]).translated(x, y)``

     In this method, ``port_A`` will first be aligned to ``port_B`` and move to ``(x, y)`` related to ``port_B``.


