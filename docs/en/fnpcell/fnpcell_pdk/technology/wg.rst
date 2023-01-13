Module fnpcell.pdk.technology.wg
==================================

Classes
--------

CurvePaintWaveguideType
++++++++++++++++++++++++++

::
    
    class CurvePaintWaveguideType(curve_paint: ICurvePaint, initial_type: IWaveguideType, 
                                    final_type: IWaveguideType, port_names: Tuple[Union[None, str, Hidden], 
                                    Union[None, str, Hidden]] = ('op_0', 'op_1'))

CurvePaintWaveguideType(args: Any, \*kwargs: Any).

Ancestors
___________

::
    
    WaveguideType, IWaveguideType, ILinkTyp, IUpdatable

Class variables
_________________

::
    
    var curve_paint: ICurvePaint
    var final_type: IWaveguideType
    var initial_type: IWaveguideType
    var port_names: Tuple[Union[None, str, Hidden], Union[None, str, Hidden]]

Methods
___________

::
    
    def band(self) -> IBand

::
    
    def port_width(self) -> float

ProfileWaveguideType
++++++++++++++++++++++

::
    
    class ProfileWaveguideType(*args: Any, **kwargs: Any)

Providing overridable profile property to express the structure of a waveguide.

Attributes
_____________

profile::
    
    readonly. Structure: [ (layer0, [ (offset00, [width000, width001, …], (start_extension00, end_extension00)), 
    (offset01, [width010, width011, …], (start_extension01, end_extension01)), ]), 
    (layer1, [ (offset10, [width101, width101, …], (start_extension10, end_extension10)) ]), ] 
    where layer0, layer1, … are layers to draw,

    <code>offset00</code>, <code>offset01</code>, ... are offset to the curve, positive value means offset towards 
    the left-side,negative value means offset towards the right-side

    <code>width000</code>, <code>width001</code>, ... are widths and the largest width is used to draw, 
    others are used to generate on-grid-fixing points.

    <code>start\_extension00</code>, <code>end\_extension01</code>, ... are extension lengths for 
    the curve/waveguide.

Ancestors
___________

::
    
    WaveguideType, IWaveguideType, ILinkType, IUpdatable

Class variables
_________________

::
    
    var bend_factory: IBendWaveguideFactory
    var port_names: Tuple[Union[None, str, Hidden], Union[None, str, Hidden]]
    var straight_factory: IStraightWaveguideFactory

Instance variables
___________________

::
    
    var profile: Sequence[Tuple[ILayer, Sequence[Tuple[float, Sequence[float]]], Tuple[float, float]]]

Methods
___________

::
    
    def tapered(self, *, taper_function: ITaperCallable = TaperFunctionLinear(), 
                final_type: Optional[~_Self] = None, **kwargs: Any) -> IWaveguideType

WaveguideType
++++++++++++++++

::
    
    class WaveguideType(*args: Any, **kwargs: Any)

Ancestors
___________

::
    
    IWaveguideType, ILinkType, IUpdatable

Subclasses
_____________

::
    
    CurvePaintWaveguideType, ProfileWaveguideType

Class variables
_________________

::
    
    var bend_factory: IBendWaveguideFactory
    var port_names: Tuple[Union[None, str, Hidden], Union[None, str, Hidden]]
    var straight_factory: IStraightWaveguideFactory

Methods
___________

::
    
    def ports(self, curve: ICurve, *, initial_type: Optional[IWaveguideType] = None, 
                final_type: Optional[IWaveguideType] = None, 
                names: Sequence[Union[None, str, Hidden]] = ('op_0', 'op_1'), 
                offset: float = 0, final_offset: Optional[float] = None) -> Tuple[IPort, IPort]

WaveguideTypeMeta
+++++++++++++++++++++

::
    
    class WaveguideTypeMeta(*args, **kwargs)

Metaclass for unique values.

Ancestors
_____________

::
    
    Type2TypeMeta, UniqueMeta, abc.ABCMeta, builtins.type