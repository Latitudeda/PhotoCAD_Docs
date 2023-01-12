Module fnpcell.element.elliptical_arc
========================================

Functions
-----------

EllipticalArc
++++++++++++++++

::
    
    def EllipticalArc(*, radius: Union[float, Iterable[float]], stroke_width: float = 1,
                         final_stroke_width: Optional[float] = None, stroke_offset: float = 0,
                         final_stroke_offset: Optional[float] = None, taper_function: ITaperCallable = TaperFunctionLinear(),
                         initial_radians: Optional[float] = None, initial_degrees: Optional[float] = None,
                         final_radians: Optional[float] = None, final_degrees: Optional[float] = None,
                         end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]] = ((), ()),
                         origin: Optional[Tuple[float, float]] = None, transform: Affine2D = Affine2D.identity(), layer: ILayer) -> Curve

Create a EllipticalArc.