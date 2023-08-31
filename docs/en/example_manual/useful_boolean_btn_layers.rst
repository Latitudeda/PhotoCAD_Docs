Boolean operations between geometry and layers
===================================================

* Get the layers of the PCell: ``device.polygon_set(layer=TECH.LAYER.XXX)``

* A, B, and C are three different layers in device and D is the layer we wish to combine after Boolean operation of A, B, and C.

  * a = ``device.polygon_set(layer=TECH.LAYER.A)``

  * b = ``device.polygon_set(layer=TECH.LAYER.B)``

  * c = ``device.polygon_set(layer=TECH.LAYER.C)``

  * d = ``fp.el.PolygonSet((a.region - b.region) | c.region, layer = TECH.LAYER.D)``

