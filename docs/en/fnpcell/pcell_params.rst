PCell Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Classes
==============

.. _AnchorParam :

AnchorParam
===================

Parameter for Anchor, see :ref:`IParam` for details.

::
    
    class AnchorParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = fnpcell.interfaces.Anchor, 
                        required: bool = True, default: Optional[Anchor] = None, 
                        default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                        preprocessor: Optional[Callable[[Any], Any]] = None, 
                        frozen: bool = False, doc: Optional[str] = None)




Ancestors : :ref:`Param`, :ref:`IParam`
___________________________________________


Class variables
__________________

::
    
    var default: Optional[Anchor]
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Assign where the (0, 0) is.

Usage::
    
    from fnpcell import all as fp 
    Straight(name="", anchor=fp.Anchor.CENTER, …)

.. _BooleanParam :

BooleanParam
==================

Parameter for boolean, see :ref:`IParam` for details.

::
    
    class BooleanParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = builtins.bool, 
                        required: bool = True, default: Optional[bool] = None, 
                        default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                        preprocessor: Optional[Callable[[Any], Any]] = None, f
                        rozen: bool = False, doc: Optional[str] = None)

Ancestors : :ref:`Param`, :ref:`IParam`
___________________________________________

Class variables
__________________

::
    
    var default: Optional[bool]
    var doc: Optional[str]
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

bool(x) -> bool

Returns True when the argument x is true, False otherwise. The builtins True and 
False are the only two instances of the class bool. The class bool is a subclass 
of the class int, and cannot be subclassed.

.. _DegreeParam :

DegreeParam
================

Parameter for Angle in Degrees, see :ref:`IParam` for details.

::
    
    class DegreeParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = (<class 'float'>, <class 'int'>), 
                        required: bool = True, default: Optional[float] = None, 
                        default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                        preprocessor: Optional[Callable[[Any], Any]] = None, 
                        frozen: bool = False, doc: Optional[str] = None, 
                        min: Optional[float] = None, max: Optional[float] = None, 
                        invalid: Optional[Container[float]] = None, 
                        precision: Optional[float] = None)


Ancestors : :ref:`FloatParam`, :ref:`Param`, :ref:`IParam`
_______________________________________________________________

Class variables
__________________

::
    
    var default: Optional[float]
    var invalid: Optional[Container[float]]
    var max: Optional[float]
    var min: Optional[float]

.. _DeviceParam :

DeviceParam
=================

Parameter for Device, see :ref:`IParam` for details.

::
    
    class DeviceParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = fnpcell.interfaces.ICellRef, 
                        required: bool = True, default: Optional[ICellRef] = None, 
                        default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                        preprocessor: Optional[Callable[[Any], Any]] = None, 
                        frozen: bool = False, doc: Optional[str] = None, 
                        factory: Optional[Callable[..., ICellRef]] = None, 
                        port_count: Optional[int] = None, pin_count: Optional[int] = None)


Ancestors : :ref:`Param`, :ref:`IParam`
_____________________________________________

Class variables
__________________

::
    
    var default: Optional[ICellRef]
    var factory: Optional[Callable[..., ICellRef]]
    var pin_count: Optional[int]
    var port_count: Optional[int]
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Interface of CellRef.

Methods
___________

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any

.. _FloatParam :

FloatParam
=================

Parameter for Float, see :ref:`IParam` for details.

::
    
    class FloatParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = (<class 'float'>, <class 'int'>), 
                        required: bool = True, default: Optional[float] = None, 
                        default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                        preprocessor: Optional[Callable[[Any], Any]] = None, 
                        frozen: bool = False, doc: Optional[str] = None, min: Optional[float] = None, 
                        max: Optional[float] = None, invalid: Optional[Container[float]] = None, 
                        precision: Optional[float] = None)


Ancestors : :ref:`Param`, :ref:`IParam`
_____________________________________________


Subclasses : :ref:`DegreeParam`, :ref:`IntParam`, :ref:`NonNegFloatParam`, :ref:`PositiveFloatParam`
____________________________________________________________________________________________________________________


Class variables
__________________

::
    
    var default: Optional[float]
    var invalid: Optional[Container[float]]
    var max: Optional[float]
    var min: Optional[float]
    var precision: Optional[float]
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Methods
___________

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any

.. _IParam :

IParam
================

::
    
    class IParam

Attributes
____________

type::
    
    Optional, parameter value must be instance of type if provided

required::
    
    True, parameter value must not be None, if required is True

default::
    
    Optional, default value if parameter is not provided

default_factory::
    
    str or Callable, defaults to "_default_{name}"

    If default_factory is Callable, then it will be called during parameter resolution.

    If default_factory is str, then:

        In functional pcell, it will be ignored.

        In dataclass pcell, default_factory will be formated with parameter name, and if a method 
        of pcell has that name, it will be called and the return value is used as default value.

    If both default and default_factory is provided, then:

        In functional pcell, default_factory is called first, if it returns None, then default is used.

        In dataclass pcell, default is used as initial value, then default_factory is called to get the frozen value. 
        If it returns None, then default is used.

preprocessor::
    
    Optional, will be called on user-provided parameter value before default value resolution and validation.

    User may provide None as parameter value, and preprocessor should handle that.

    If preprocessor returns None, the parameter is treated as not provided by user and will run default value resolution.

doc::
    
    Optional, user provided short document text.

Subclasses : :ref:`Param`, ``fnpcell.pdk.pcell_params._NonNegMixin``, ``fnpcell.pdk.pcell_params._PositiveMixin``
_________________________________________________________________________________________________________________________



Class variables
__________________

::
    
    var default: Optional[Any]
    var default_factory: Union[str, Callable[[], Any]]
    var doc: Optional[str]
    var frozen: bool
    var preprocessor: Optional[Callable[[Any], Any]]
    var required: bool
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Methods
__________

::
    
    def as_field(self, repr: bool = True, hash: Optional[bool] = None, 
                    compare: bool = True) -> Any

::
    
    def resolve(self, runtime: Any, name: str, value: Optional[Any], 
                context: Optional[Any]) -> Any

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], 
                    context: Optional[Any]) -> Any

.. _IntParam:

IntParam                   
================

Parameter for Integer, see :ref:`IParam` for details.

::
    
    class IntParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = (<class 'float'>, <class 'int'>), 
                    required: bool = True, default: Optional[int] = None, 
                    default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                    preprocessor: Optional[Callable[[Any], Any]] = None, 
                    frozen: bool = False, doc: Optional[str] = None, min: Optional[int] = None, 
                    max: Optional[int] = None, invalid: Optional[Container[int]] = None, 
                    precision: Optional[float] = None)

Ancestors : :ref:`Param`, :ref:`IParam`, :ref:`FloatParam`
_______________________________________________________________



Subclasses : :ref:`NonNegIntParam`, :ref:`PositiveIntParam`
_____________________________________________________________


Class variables
__________________

::
    
    var default: Optional[int]
    var invalid: Optional[Container[int]]
    var max: Optional[int]
    var min: Optional[int]

Methods
__________

def validate(self, runtime: Any, name: str, value: Optional[Any], 
                context: Optional[Any]) -> Any

.. _LayerParam:

LayerParam
=================

Parameter for Layer, see :ref:`IParam` for details.

::
    
    class LayerParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = fnpcell.interfaces.ILayer, 
                        required: bool = True, default: Optional[ILayer] = None, 
                        default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                        preprocessor: Optional[Callable[[Any], Any]] = None, 
                        frozen: bool = False, doc: Optional[str] = None)


Ancestors : :ref:`Param`, :ref:`IParam`
_____________________________________________

Class variables
__________________

::
    
    var default: Optional[ILayer]
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Interface of Layer.

.. _ListParam:

ListParam
==================

Parameter for List, see :ref:`IParam` for details.

::
    
    class ListParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = typing.Iterable, 
                    required: bool = True, default: Optional[Iterable[Any]] = None, 
                    default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                    preprocessor: Optional[Callable[[Any], Any]] = None, 
                    frozen: bool = False, doc: Optional[str] = None, 
                    element_type: Optional[Type[Any]] = None, immutable: bool = False)


Ancestors : :ref:`Param`, :ref:`IParam`
_____________________________________________

Class variables
__________________

::
    
    var default: Optional[Iterable[Any]]
    var element_type: Optional[Type[Any]]
    var immutable: bool
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Methods
__________

::
    
    def resolve(self, runtime: Any, name: str, value: Optional[Any], 
                context: Optional[Any]) -> Any

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], 
                    context: Optional[Any]) -> Any

.. _MappingParam:

MappingParam
=================

Parameter for Mapping, see :ref:`IParam` for details.

::
    
    class MappingParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = typing.Mapping, 
                        required: bool = True, default: Optional[Dict[Any, Any]] = None, 
                        default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                        preprocessor: Optional[Callable[[Any], Any]] = None, frozen: bool = False, 
                        doc: Optional[str] = None, K: Optional[Type[Any]] = None, 
                        V: Optional[Type[Any]] = None, immutable: bool = False)


Ancestors : :ref:`Param`, :ref:`IParam`
_____________________________________________

Class variables
__________________

::
    
    var K: Optional[Type[Any]]
    var V: Optional[Type[Any]]
    var default: Optional[Dict[Any, Any]]
    var immutable: bool
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Methods
__________

::
    
    def resolve(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any

.. _MetalLineTypeParam:

MetalLineTypeParam
=========================

Parameter for MetalLineType, see :ref:`IParam` for details.

::
    
    class MetalLineTypeParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = fnpcell.interfaces.IMetalLineType, 
                                required: bool = True, default: Optional[Any] = None, 
                                default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                                preprocessor: Optional[Callable[[Any], Any]] = None, 
                                frozen: bool = False, doc: Optional[str] = None, 
                                band: Union[IBand, Container[IBand], None] = None)


Ancestors : :ref:`Param`, :ref:`IParam`
_____________________________________________

Class variables
__________________

::
    
    var band: Union[IBand, Container[IBand], None]
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Methods
__________

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any

.. _NameListParam:

NameListParam
====================

Parameter for Name List, eg. ["op_0", "op_1", "op_2", "op_3"], see :ref:`IParam` for details.

::
    
    class NameListParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = typing.Iterable, 
                        required: bool = True, default: Optional[Sequence[str]] = None, 
                        default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                        preprocessor: Optional[Callable[[Any], Any]] = None, 
                        frozen: bool = False, doc: Optional[str] = None, min_count: int = 0, 
                        max_count: int = 9223372036854775807, count: Optional[int] = None)


Ancestors : :ref:`Param`, :ref:`IParam`
_____________________________________________

Class variables
__________________

::
    
    var count: Optional[int]
    var default: Optional[Sequence[str]]
    var max_count: int
    var min_count: int
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Methods
__________

::
    
    def resolve(self, runtime: Any, name: str, value: Optional[Any], 
                context: Optional[Any]) -> Any

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], 
                    context: Optional[Any]) -> Any

.. _NameParam:

NameParam
===============

Parameter for PCell Name, see :ref:`IParam` for details.


::
    
    class NameParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = builtins.str, 
                    required: bool = False, default: Optional[str] = None, 
                    default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                    preprocessor: Optional[Callable[[Any], Any]] = None, 
                    frozen: bool = False, doc: Optional[str] = None, prefix: Optional[str] = None)


Ancestors : :ref:`Param`, :ref:`IParam`, :ref:`TextParam`
____________________________________________________________


Class variables
__________________

::
    
    var default: Optional[str]
    var prefix: Optional[str]
    var required: bool
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

**Inherited from:** TextParam.type

str(object='') -> str str(bytes_or_buffer[, encoding[, errors]]) -> str …

Methods
__________

::
    
    def resolve(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any

.. _NonNegFloatParam:

NonNegFloatParam
========================

Parameter for non negative Float, see :ref:`IParam` for details.


::
    
    class NonNegFloatParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = (<class 'float'>, <class 'int'>), 
                            required: bool = True, default: Optional[float] = None, 
                            default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                            preprocessor: Optional[Callable[[Any], Any]] = None, 
                            frozen: bool = False, doc: Optional[str] = None, min: float = 0, 
                            max: Optional[float] = None, invalid: Optional[Container[float]] = None, 
                            precision: Optional[float] = None)



Ancestors : :ref:`Param`, :ref:`FloatParam`, :ref:`IParam`, ``fnpcell.pdk.pcell_params._NonNegMixin``
______________________________________________________________________________________________________
    


Class variables
__________________

::
    
    var default: Optional[float]
    var invalid: Optional[Container[float]]
    var max: Optional[float]
    var min: float

.. _NonNegIntParam:


NonNegIntParam
===================

Parameter for non negative integral, see :ref:`IParam` for details.

::
    
    class NonNegIntParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = (<class 'float'>, <class 'int'>), 
                            required: bool = True, default: Optional[int] = None, 
                            default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                            preprocessor: Optional[Callable[[Any], Any]] = None, frozen: bool = False, 
                            doc: Optional[str] = None, min: int = 0, max: Optional[int] = None, 
                            invalid: Optional[Container[int]] = None, precision: Optional[float] = None)

Ancestors : :ref:`Param`, :ref:`FloatParam`, :ref:`IParam`, :ref:`IntParam`, ``fnpcell.pdk.pcell_params._NonNegMixin``
_________________________________________________________________________________________________________________________


Class variables
_________________

::
    
    var default: Optional[int]
    var invalid: Optional[Container[int]]
    var max: Optional[int]
    var min: int

.. _Param :

Param
==========

General parameter definition, and if there's no proper XXXParam, then use :ref:`Param`, see :ref:`IParam` for details.

::
    
    class Param(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = None, 
                required: bool = True, default: Optional[Any] = None, 
                default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                preprocessor: Optional[Callable[[Any], Any]] = None, 
                frozen: bool = False, doc: Optional[str] = None)



Ancestors : :ref:`IParam`
___________________________

Subclasses
____________

::
    
    AnchorParam, BooleanParam, DeviceParam, FloatParam, LayerParam, ListParam, 
    MappingParam, MetalLineTypeParam, NameListParam, PointsParam, PortOptionsParam, 
    PositionParam, SetParam, TextParam, TransformParam, WaveguideTypeParam

Class variables
_________________

::
    
    var default: Optional[Any]
    var default_factory: Union[str, Callable[[], Any]] 
    var doc: Optional[str]
    var frozen: bool
    var preprocessor: Optional[Callable[[Any], Any]]
    var required: bool
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

.. _PointsParam:

PointsParam
==================

Parameter for Point, see :ref:`IParam` for details.

::
    
    class PointsParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = typing.Iterable, 
                        required: bool = True, default: Optional[Iterable[Tuple[float, float]]] = None, 
                        default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                        preprocessor: Optional[Callable[[Any], Any]] = None, frozen: bool = False, 
                        doc: Optional[str] = None, min_count: int = 0)



Ancestors : :ref:`Param`, :ref:`IParam`
__________________________________________________


Class variables
_________________

::
    
    var default: Optional[Iterable[Tuple[float, float]]]
    var min_count: int
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Methods
__________

::
    
    def resolve(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any

.. _PortOptionsParam:

PortOptionsParam
======================

Parameter for PortOptions, eg: ports=(None, "op_1"), and None will disable port in the position, see :ref:`IParam` for details.

::
    
    class PortOptionsParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = typing.Sequence, 
                            required: bool = True, default: Optional[Sequence[Union[None, str, Hidden]]] = None, 
                            default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                            preprocessor: Optional[Callable[[Any], Any]] = None, frozen: bool = False, 
                            doc: Optional[str] = None, count: Optional[int] = None)


Ancestors : :ref:`Param`, :ref:`IParam`
__________________________________________________

Class variables
__________________

::
    
    var count: Optional[int]
    var default: Optional[Sequence[Union[None, str, Hidden]]]
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Methods
__________

::
    
    def resolve(self, runtime: Any, name: str, value: Optional[Any], 
                    context: Optional[Any]) -> Any

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], 
                    context: Optional[Any]) -> Any

.. _PositionParam:

PositionParam
====================

Parameter for Position, see :ref:`IParam` for details.


::
    
    class PositionParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = typing.Tuple, 
                        required: bool = True, default: Optional[Tuple[float, float]] = None, 
                        default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                        preprocessor: Optional[Callable[[Any], Any]] = None, 
                        frozen: bool = False, doc: Optional[str] = None)


Ancestors : :ref:`Param`, :ref:`IParam`
__________________________________________________

Class variables
_________________

::
    
    var default: Optional[Tuple[float, float]]
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Methods
__________

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any


.. _PositiveFloatParam:

PositiveFloatParam
====================

Parameter for Positive Float, see :ref:`IParam` for details.


::
    
    class PositiveFloatParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = (<class 'float'>, <class 'int'>), 
                                required: bool = True, default: Optional[float] = None, 
                                default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                                preprocessor: Optional[Callable[[Any], Any]] = None, 
                                frozen: bool = False, doc: Optional[str] = None, min: Optional[float] = None, 
                                max: Optional[float] = None, invalid: Optional[Container[float]] = None, 
                                precision: Optional[float] = None)

Ancestors : :ref:`Param`, :ref:`FloatParam`, :ref:`IParam`, ``fnpcell.pdk.pcell_params._PositiveMixin``
_________________________________________________________________________________________________________________________
    


Class variables
__________________

::
    
    var default: Optional[float]
    var invalid: Optional[Container[float]]
    var max: Optional[float]
    var min: Optional[float]

.. _PositiveIntParam:

PositiveIntParam
====================

Parameter for Positive Integral, see :ref:`IParam` for details.

::
    
    class PositiveIntParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = (<class 'float'>, <class 'int'>), 
                            required: bool = True, default: Optional[int] = None, 
                            default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                            preprocessor: Optional[Callable[[Any], Any]] = None, frozen: bool = False, 
                            doc: Optional[str] = None, min: Optional[int] = None, max: Optional[int] = None, 
                            invalid: Optional[Container[int]] = None, precision: Optional[float] = None)


Ancestors : :ref:`Param`, :ref:`FloatParam`, :ref:`IParam`, :ref:`IntParam`, ``fnpcell.pdk.pcell_params._PositiveMixin``
_________________________________________________________________________________________________________________________




Class variables
__________________

::
    
    var default: Optional[int]
    var invalid: Optional[Container[int]]
    var max: Optional[int]
    var min: Optional[int]

.. _SetParam:

SetParam
====================

Parameter for Set, see :ref:`IParam` for details.


::
    
    class SetParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = typing.Iterable, 
                    required: bool = True, default: Optional[Iterable[Any]] = None, 
                    default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                    preprocessor: Optional[Callable[[Any], Any]] = None, frozen: bool = False, 
                    doc: Optional[str] = None, element_type: Optional[Type[Any]] = None, 
                    immutable: bool = False)

Ancestors : :ref:`Param`, :ref:`IParam`
__________________________________________



Class variables
_________________

::
    
    var default: Optional[Iterable[Any]]
    var element_type: Optional[Type[Any]]
    var immutable: bool
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Methods
__________

::
    
    def resolve(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], context: Optional[Any]) -> Any

.. _TextParam:

TextParam
===================

Parameter for Text, see :ref:`IParam` for details.

::
    
    class TextParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = builtins.str, 
                    required: bool = True, default: Optional[str] = None, 
                    default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                    preprocessor: Optional[Callable[[Any], Any]] = None, frozen: bool = False, 
                    doc: Optional[str] = None)

Ancestors : :ref:`Param`, :ref:`IParam`
__________________________________________

Subclasses : :ref:`NameParam`
_________________________________



Class variables
__________________

::
    
    var default: Optional[str]
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

str(object='') -> str str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or errors is specified, 
then the object must expose a data buffer that will be decoded using the given encoding 
and error handler. Otherwise, returns the result of object.str() (if defined) or repr(object). 
encoding defaults to sys.getdefaultencoding(). errors defaults to 'strict'.

Methods
__________

::
    
    def validate(self, runtime: Any, name: str, value: Optional[Any], 
                    context: Optional[Any]) -> Any

.. _TransformParam:

TransformParam
=========================

Parameter for Transformations, see :ref:`IParam` for details.


::
    
    class TransformParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = fnpcell.transform.Affine2D, 
                            required: bool = False, default: Optional[Affine2D] = None, 
                            default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                            preprocessor: Optional[Callable[[Any], Any]] = None, 
                            frozen: bool = False, doc: Optional[str] = None)


Ancestors : :ref:`Param`, :ref:`IParam`
__________________________________________

Class variables
_________________

::
    
    var default: Optional[Affine2D]
    var required: bool
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Affine2D transformation matrix.

Usage::
    
    from fnpcell import all as fp

    t = fp.translate(10, 0)
    r = fp.rotate(degrees=30)
    transform = t @ r

    assert transform == fp.translate(10, 0).rotate(degrees=30)

    points = [(0, 0), (1, 0), (1, 1)]
    transformed_points = transform(points)  # equals to transform.transform_points(points)

Methods
__________

::
    
    def resolve(self, runtime: Any, name: str, value: Optional[Any], 
                context: Optional[Any]) -> Any

.. _WaveguideTypeParam:

WaveguideTypeParam
===========================

Parameter for WaveguideType, see :ref:`IParam` for details.


::
    
    class WaveguideTypeParam(type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None] = fnpcell.interfaces.IWaveguideType, 
                                required: bool = True, default: Optional[Any] = None, 
                                default_factory: Union[str, Callable[[], Any]] = '_default_{name}', 
                                preprocessor: Optional[Callable[[Any], Any]] = None, 
                                frozen: bool = False, doc: Optional[str] = None, 
                                band: Union[IBand, Container[IBand], None] = None)



Ancestors : :ref:`Param`, :ref:`IParam`
__________________________________________

Class variables
__________________

::
    
    var band: Union[IBand, Container[IBand], None]
    var type: Union[type, Tuple[Union[type, Tuple[type, ...]], ...], None]

Methods
__________

::
    
    def validate(self, runtime: Any, name: str, 
                    value: Optional[Any], context: Optional[Any]) -> Any