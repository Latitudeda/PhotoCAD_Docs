Module fnpcell.pdk.technology.metal
====================================

Classes
---------

CurvePaintMetalLineType
++++++++++++++++++++++++++

::
    
    class CurvePaintMetalLineType(curve_paint: ICurvePaint, initial_type: IMetalLineType, 
                                    final_type: IMetalLineType, port_names: Tuple[Union[None, str, Hidden], 
                                    Union[None, str, Hidden]] = ('ep_0', 'ep_1'))

CurvePaintMetalLineType(args: Any, \*kwargs: Any)

Ancestors
___________

::
    
    MetalLineType, IMetalLineType, ILinkType, IUpdatable

Class variables
_________________

::
    
    var curve_paint: ICurvePaint
    var final_type: IMetalLineType
    var initial_type: IMetalLineType
    var port_names: Tuple[Union[None, str, Hidden], Union[None, str, Hidden]]

Methods
___________

::
    
    def ports(self, curve: ICurve, *, initial_type: Optional[IMetalLineType] = None, 
                final_type: Optional[IMetalLineType] = None, 
                names: Sequence[Union[None, str, Hidden]] = ('ep_0', 'ep_1'), 
                offset: float = 0, final_offset: Optional[float] = None) -> Tuple[IPin, IPin]

**Inherited from:** MetalLineType.ports

Create two new electrial pins of a metal line.

MetalLineType
+++++++++++++++

::
    
    class MetalLineType(*args: Any, **kwargs: Any)

Ancestors
____________

::
    
    IMetalLineType, ILinkType, IUpdatable

Subclasses
___________

::
    
    CurvePaintMetalLineType, ProfileMetalLineType

Class variables
__________________

::
    
    var line_width: float

Methods
___________

::
    
    def ports(self, curve: ICurve, *, initial_type: Optional[IMetalLineType] = None, 
                final_type: Optional[IMetalLineType] = None, 
                names: Sequence[Union[None, str, Hidden]] = ('ep_0', 'ep_1'), 
                offset: float = 0, final_offset: Optional[float] = None) -> Tuple[IPin, IPin]

Create two new electrial pins of a metal line.

MetalLineTypeMeta
++++++++++++++++++

::
    
    class MetalLineTypeMeta(*args, **kwargs)

Metaclass for unique values.

Ancestors
___________

::
    
    Type2TypeMeta, UniqueMeta, abc.ABCMeta, builtins.type

ProfileMetalLineType
+++++++++++++++++++++++

::
    
    class ProfileMetalLineType(*args: Any, **kwargs: Any)

Providing overridable profile property to express the structure of a metal line.

Attributes
_________________

profile::
    
    readonly. Structure: [ (offset0, [width00, width01, …]), (offset1, [width10, width11, …]), ] 
    where offset0, offset1, … are offset to the curve, positive value means offset towards the 
    left-side, negative value means offset towards the right-side

    <code>width00</code>, <code>width01</code>, ... are widths and the largest width is used to draw, 
    others are used to generate on-grid-fixing points.

Ancestors
____________

::
    
    MetalLineType, IMetalLineType, ILinkType, IUpdatable

Class variables
_________________

::
    
    var line_width: float

Instance variables
___________________

::
    
    var profile: Sequence[Tuple[ILayer, Sequence[Tuple[float, Sequence[float]]], Tuple[float, float]]]

Methods
___________

::
    
    def ports(self, curve: ICurve, *, initial_type: Optional[IMetalLineType] = None, 
                final_type: Optional[IMetalLineType] = None, '
                'names: Sequence[Union[None, str, Hidden]] = ('ep_0', 'ep_1'), 
                offset: float = 0, final_offset: Optional[float] = None) -> Tuple[IPin, IPin]

**Inherited from:** MetalLineType.ports

Create two new electrial pins of a metal line.