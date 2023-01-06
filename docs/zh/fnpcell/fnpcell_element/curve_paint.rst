Module fnpcell.element.curve_paint
====================================

Classes
---------

::
    
    class CompositeCurvePaint(curve_paints: Tuple[ICurvePaint, ...])

    CompositeCurvePaint(args, *kwds)

Ancestors
+++++++++++

::

    ICurvePaint, typing.Protocol, typing.Generic

Class variables
+++++++++++++++++

::
    
    var curve_paints: Tuple[ICurvePaint, ...]

::
    
    class ContinuousLayerCurvePaint(layer: ILayer, offset: float, width: float, extension: Tuple[float, float],
                                     miter_limit: float, final_offset: float, final_width: float,
                                     taper_function: ITaperCallable, end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]])

    ContinuousLayerCurvePaint(args, *kwds)

Ancestors
+++++++++++

::
    
    ICurvePaint, typing.Protocol, typing.Generic

Subclasses
++++++++++++

::
    
    CrackedLayerCurvePaint, SlottedLayerCurvePaint

Class variables
++++++++++++++++++

::
    
    var end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]]
    var extension: Tuple[float, float]
    var final_offset: float
    var final_width: float
    var layer: ILayer
    var miter_limit: float
    var offset: float
    var taper_function: ITaperCallable
    var width: float

Methods
+++++++++

::
    
    def with_cracks(self, max_width: float = 35, spacing: float = 3)

::
    
    def with_slots(self, max_width: float = 35, slot_width: float = 3, slot_length: float = 30,
                     min_slot_length: float = 30, slot_gap: float = 10, stagger_offset: float = 15)

::
    
    class CrackedLayerCurvePaint(layer: ILayer, offset: float, width: float, extension: Tuple[float, float],
                                 miter_limit: float, final_offset: float, final_width: float,
                                 taper_function: ITaperCallable, end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]],
                                 max_width: float = 35, spacing: float = 3)

    CrackedLayerCurvePaint(args, *kwds)

Ancestors
+++++++++++

::
    
    ContinuousLayerCurvePaint, ICurvePaint, typing.Protocol, typing.Generic


Class variables
++++++++++++++++

::

    var max_width: float
    var spacing: float

Instance variables
+++++++++++++++++++++

::

    var count_of_lanes

Methods
++++++++

::
    
    def offset_widths(self, width: Optional[float] = None, offset: float = 0) -> Sequence[Tuple[float, Sequence[float]]]

    classCurvePaint

Static methods
+++++++++++++++

::
    
    def Composite(paints: Iterable[ICurvePaint], /)

::
    
    def ContinuousLayer(*, layer: ILayer, width: float, offset: float = 0, extension: Tuple[float, float] = (0, 0),
                         miter_limit: float = inf, final_offset: Optional[float] = None,
                         final_width: Optional[float] = None, taper_function: ITaperCallable = TaperFunctionLinear(),
                         end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]] = ((), ()))

::
    
    def PeriodicSampling(*, pattern: IElement, period: float, reserved_ends: Tuple[float, float] = (0, 0),
                         offset: float = 0, final_offset: Optional[float] = None, miter_limit: float = inf,
                         taper_function: ITaperCallable = TaperFunctionLinear(), rotate: bool = True)

::
    
    def from_profile(profile: Sequence[Tuple[ILayer, Sequence[Tuple[float, Sequence[float]]], Tuple[float, float]]], *,
                     miter_limit: float = inf, taper_function: ITaperCallable = TaperFunctionLinear(),
                     final_profile: Optional[Sequence[Tuple[ILayer, Sequence[Tuple[float, Sequence[float]]],
                     Tuple[float, float]]]] = None, end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]] = ((), ()))

::
    
    class PeriodicSamplingCurvePaint(pattern: IElement, period: float, reserved_ends: Tuple[float, float],
                                     offset: float, final_offset: float, miter_limit: float,
                                     taper_function: ITaperCallable, rotate: bool = True)
    
    PeriodicSamplingCurvePaint(args, *kwds)

Ancestors
+++++++++++

::
    
    ICurvePaint, typing.Protocol, typing.Generic

Class variables
++++++++++++++++++

::
    
    var final_offset: float
    var miter_limit: float
    var offset: float
    var pattern: IElement
    var period: float
    var reserved_ends: Tuple[float, float]
    var rotate: bool
    var taper_function: ITaperCallable

::
    
    class SlottedLayerCurvePaint(layer: ILayer, offset: float, width: float,
                                 extension: Tuple[float, float], miter_limit: float, final_offset: float,
                                 final_width: float, taper_function: ITaperCallable,
                                 end_hints: Tuple[Tuple[float, ...], Tuple[float, ...]],
                                 max_width: float = 35, slot_width: float = 3, slot_length: float = 30,
                                 min_slot_length: float = 30, slot_gap: float = 10, stagger_offset: float = 15)

    SlottedLayerCurvePaint(args, *kwds)

Ancestors
++++++++++

::
    
    ContinuousLayerCurvePaint, ICurvePaint, typing.Protocol, typing.Generic

Class variables
+++++++++++++++++

    var max_width: float
    var min_slot_length: float
    var slot_gap: float
    var slot_length: float
    var slot_width: float
    var stagger_offset: float