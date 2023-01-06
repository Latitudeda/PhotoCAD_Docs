Module fnpcell.element.box
============================

Functions
------------

::
    
    def Box(*, width: float, height: float, stroke_width: float = 1,
             origin: Optional[Tuple[float, float]] = None,
             transform: Affine2D = Affine2D.identity(), layer: ILayer) -> IPolygon

Create a box with layer.