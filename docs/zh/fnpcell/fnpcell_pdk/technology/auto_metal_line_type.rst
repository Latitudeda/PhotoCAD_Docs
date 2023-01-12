Module fnpcell.pdk.technology.auto_metal_line_type
======================================================

Classes
---------

AutoMetalLineType
+++++++++++++++++++

::
    
    class AutoMetalLineType(registry: Optional[Mapping[str, Callable[[Optional[float]], IMetalLineType]]] = None, /)

Registry for auto metal line type, used in fp.Linked / fp.LinkBetween.

Usage::
    
    # (see gpdk.technology.auto_metal_line_type)

    from fnpcell.pdk.technology import all as fpt
    from gpdk.technology import get_technology, MetalLineType

    def _mt(line_width: Optional[float] = None, line_style: Optional[IMetalLineStyle] = None):
        if line_width is None:
            line_width = TECH.METAL.DEFAULT_LINE_WIDTH
        return MetalLineType.MT(line_width=line_width, line_layout_style=line_style)

    auto_metal_line_type = fpt.AutoMetalLineType()
    auto_metal_line_type += TECH.LAYER.MT_DRW, _mt

Methods
_________


::
    
    def get(self, layer: ILayer, default: Optional[Callable[[Optional[float]], 
            IMetalLineType]] = None) -> Optional[Callable[[Optional[float]], IMetalLineType]]

::
    
    def updated(self, entries: Sequence[Tuple[ILayer, Callable[[Optional[float]], IMetalLineType]]])