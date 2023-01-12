Module fnpcell.element.arc
============================

Functions
------------

Arc
++++++

::
    
    def Arc(*, radius: float, stroke_width: float = 1, final_stroke_width: Optional[float] = None,
             stroke_offset: float = 0, final_stroke_offset: Optional[float] = None,
             taper_function: ITaperCallable = TaperFunctionLinear(),
             end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]] = ((), ()),
             initial_radians: Optional[float] = None, initial_degrees: Optional[float] = None,
             final_radians: Optional[float] = None, final_degrees: Optional[float] = None,
             origin: Optional[Tuple[float, float]] = None,
             transform: Affine2D = Affine2D.identity(), layer: ILayer) -> Curve

Create a CircularArc.