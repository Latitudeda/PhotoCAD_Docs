Module fnpcell.element.rect
============================

Functions
-----------

::
    
    def Rect(*, width: float, height: float, corner_radius: Union[float, Iterable[float]] = 0,
             bottom_left: Optional[Tuple[float, float]] = None, origin: Optional[Tuple[float, float]] = None,
             center: Optional[Tuple[float, float]] = None, transform: Affine2D = Affine2D.identity(),
             layer: ILayer) -> IPolygon
             
Create a rect with layer.