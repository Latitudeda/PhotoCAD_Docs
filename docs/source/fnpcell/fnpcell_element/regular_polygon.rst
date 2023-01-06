Module fnpcell.element.regular_polygon
========================================

Functions
-------------

::
    
    def RegularPolygon(*, sides: int, side_length: float, origin: Optional[Tuple[float, float]] = None,
                         transform: Affine2D = Affine2D.identity(), layer: ILayer) -> IPolygon

Create a regular polygon with layer.