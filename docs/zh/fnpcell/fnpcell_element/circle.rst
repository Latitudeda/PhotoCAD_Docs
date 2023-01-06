Module fnpcell.element.circle
===============================

Functions
-----------

::
    
    def Circle(*, radius: float, initial_radians: Optional[float] = None,
                 initial_degrees: Optional[float] = None, final_radians: Optional[float] = None,
                 final_degrees: Optional[float] = None, origin: Optional[Tuple[float, float]] = None,
                 transform: Affine2D = Affine2D.identity(), layer: ILayer) -> IPolygon

Create a Circle.