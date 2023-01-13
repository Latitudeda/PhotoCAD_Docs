Module fnpcell.pdk.technology.metal_stack
===========================================

Classes
--------

MetalStack
+++++++++++++

::
    
    class MetalStack(*, layers: Iterable[ILayer], connectivity: Mapping[ILayer, Iterable[ILayer]])

MetalStack(\*, layers: Iterable[fnpcell.interfaces.ILayer], 
connectivity: Mapping[fnpcell.interfaces.ILayer, Iterable[fnpcell.interfaces.ILayer]])

Ancestors
____________

::
    
    IMetalStack, IUpdatable

Class variables
__________________

::
    
    var connectivity: Mapping[ILayer, FrozenSet[ILayer]]
    var layers: Tuple[ILayer, ...]

Methods
____________

::
    
    def is_metal(self, layer: ILayer) -> bool

::
    
    def via_layer(self, key: Tuple[ILayer, ILayer]) -> ILayer