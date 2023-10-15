fp.g API
==================================

``fp.g`` API generates varies of curves which is often used with ``waveguide_type`` to define the path of a waveguide type. Cells create by ``fp.g.`` has no layer information hence cannot be as a element or an instance in the ``build`` function.

Here we list some examples where ``fp.g.`` is mostly often used.

#. ::

        euler_curve = fp.g.EulerBend() # define in raw_curve method
        wg = waveguide_type(curve=euler_curve) # define in build method
        insts += wg

``fp.g``
-----------------

The api for common graphics mainly contains::





