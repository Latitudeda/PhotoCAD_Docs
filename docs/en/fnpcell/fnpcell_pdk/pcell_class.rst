Module fnpcell.pdk.pcell_class
================================

Functions
----------

pcell_class
++++++++++++

::
    
    def pcell_class(band: Union[str, IBand, Iterable[IBand]] = ()) -> Callable[[~_T], ~_T]

A decorator which is required for defining dataclass pcells.

Args

band::
    
    Optional, band of the device, maybe single band or a list of band that the device supports.

    If provided, pcell runtime might add some visual annotion to the cell using TECH.DEVICE.band_annotation method.

    And would check every optical port of the device to ensure none of them has wrong band

    TECH.DEVICE.band_annotation can be redefine in technology to provide customized visual annotation

    see gpdk.technology.device.DEVICE

Usage::
    
    from fnpcell import all as fp

    @fp.pcell_class(band=TECH.BAND.C)
    class UserDefinedClass(fp.PCell):
        def build(self):
            insts, elems, ports = super().build()
            ...
            return insts, elems, ports