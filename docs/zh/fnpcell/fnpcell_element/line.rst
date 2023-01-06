Module fnpcell.element.line
=============================

Functions
-----------

::
    
    def Line(*, length: float, stroke_width: float = 1, final_stroke_width: Optional[float] = None,
             stroke_offset: float = 0, final_stroke_offset: Optional[float] = None,
             taper_function: ITaperCallable = TaperFunctionLinear(),
             end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]] = ((), ()),
             anchor: Anchor = Anchor.START, origin: Optional[Tuple[float, float]] = None,
             transform: Affine2D = Affine2D.identity(), layer: ILayer) -> Curve

Create a line with layer.

::
    
    def new_line(*, length: float, stroke_width: float = 1, final_stroke_width: Optional[float] = None,
                 stroke_offset: float = 0, final_stroke_offset: Optional[float] = None,
                 taper_function: ITaperCallable = TaperFunctionLinear(),
                 end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]] = ((), ()),
                 anchor: Anchor = Anchor.START, origin: Optional[Tuple[float, float]] = None,
                 transform: Affine2D = Affine2D.identity(), layer: ILayer) -> Curve

Create a line with layer.

::
    
    def new_line_between(start: Tuple[float, float], end: Tuple[float, float], *, stroke_width: float = 1,
                         final_stroke_width: Optional[float] = None, stroke_offset: float = 0,
                         final_stroke_offset: Optional[float] = None,
                         taper_function: ITaperCallable = TaperFunctionLinear(),
                         end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]] = ((), ()),
                         origin: Optional[Tuple[float, float]] = None,
                         transform: Affine2D = Affine2D.identity(), layer: ILayer) -> Curve