Module fnpcell.pdk.place
=========================

Functions
-----------

place
++++++

::
    
    def place(device: ~_T, port: str, *, at: Union[Tuple[float, float], IPositioned, IRay]) -> ~_T

Returns a translated device with the given port at the new point. 
When the at parameter is Point2D, the device orientation is unchanged. 
When the at parameter is not Point2D, the device rotates to the direction 
that its given port is opposite to other device ports.

Usage::
    
    dc = pdk.DirectionalCouplerSBend(waveguide_type=TECH.WG.SWG.C.WIRE, coupler_spacing=2, bend_degrees=60) 
    fp.place(s0, "op_0", at=(0, 0))