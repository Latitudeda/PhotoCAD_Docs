Manually add ports/pins on PCells
===========================================

* Under build method:

  * For waveguide ports: ``ports += fp.Port(name, position, waveguide_type, orientation)``

  * For metal pins: ``ports += fp.Pin(name, position, metal_line_type, orientation)``
