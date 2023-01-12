Module fnpcell.cell.pin
==========================

Functions
----------

new_pin
+++++++++++

::

    def new_pin(*, name: Union[None, str, Hidden], position: Optional[Tuple[float, float]] = None,
                 orientation: float = nan, at: Optional[IRay] = None, metal_line_type: IMetalLineType,
                 shape: Optional[IShape] = None) -> IPin

Create a new electrial pin.

Classes
--------

OwnedPin
++++++++++

::

    class OwnedPin(name: Optional[str], raw: IPin, owner: ICellRef, assigned_orientation: Optional[float] = None,
                     hidden: bool = False)

OwnedPin is for defining a pin owned by a CellRef.

OwnedPin with owner attribute can appoint to it's owner, 
owner is a CellRef Any modification will create new OwnedPin instead of modify the original OwnedPin.

Ancestors
____________

::
    
    fnpcell.cell.pin._PinMixin, IOwnedPin, IPin, IOwnedTerminal, IOwned ITerminal, 
    IUpdatable, IRay, IPositioned, IRunnable

Class variables
__________________

::

    var assigned_orientation: Optional[float]
    var hidden: bool
    var name: Optional[str]
    var owner: ICellRef
    var raw: IPin

Static methods
_________________

::

    def from_pin(pin: IPin, owner: ICellRef) -> OwnedPin

Return OwnedPin.

Instance variables
_____________________

::

    var annotation

Return composite.

::
    
    var metal_line_type : IMetalLineType

Return pin metal_line_type.

::
    
    var orientation : float

Return calculated orientation take owner's transform into account.

::
    
    var position : Tuple[float, float]

Return pin position.

::
    
    var shape : IShape

Return pin shape.

Methods
_________

::
    
    def advanced(self: ~_Self, distance: float) -> ~_Self

**Inherited from:** IOwnedPin.advanced

Return an IRay with advanced position through orientation.

::
    
    def c_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedPin.c_mirrored

Owner center mirrored.

::
    
    def flatten(self) -> Pin

Return pin.

::

    def h_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedPin.h_mirrored

Owner horizontal mirrored.

::
    
    def opposite(self: ~_Self) -> ~_Self

**Inherited from:** IOwnedPin.opposite

Return an IRay with same position but opposite orientation.

::
    
    def repositioned(self, *, at: Union[Tuple[float, float], IPositioned, IRay]) -> IOwnedTerminal

**Inherited from:** IOwnedPin.repositioned

Positioned at new point,Owner will translated.

::
    
    def rotated(self, degrees: Optional[float] = None, radians: Optional[float] = None) -> IOwnedTerminal

**Inherited from:** IOwnedPin.rotated

Rotated both degrees and radians.

::
    
    def v_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedPin.v_mirrored

Owner vertical mirrored.

::
    
    def with_orientation(self, *, degrees: Optional[float] = None, radians: Optional[float] = None)

Return a new OwnedPin with the given orientation.

Pin
+++++

::
    
    class Pin(name: Optional[str], position: Tuple[float, float], shape: IShape,
                 metal_line_type: IMetalLineType, orientation: float = nan, hidden: bool = False)

Pin is for defining a electrial Pin .
Any modification will create new Pin instead of modify the original Pin.

Usage::
    
    from fnpcell import all as fp

    pin = fp.Pin(name="ep_0", position=(0, 0),...)

Ancestors
___________

::
    
    fnpcell.cell.pin._PinMixin, IPin, ITerminal, IUpdatable, IRay, IPositioned, IRunnable

Class variables
__________________

::

    var hidden: bool
    var metal_line_type: IMetalLineType
    var name: Optional[str]
    var orientation: float
    var position: Tuple[float, float]
    var shape: IShape
    
Instance variables
_____________________

::

    var annotation

Return composite.

Methods
_________

::

    def advanced(self: ~_Self, distance: float) -> ~_Self

**Inherited from:** IPin.advanced

Return an IRay with advanced position through orientation

::
    
    def opposite(self: ~_Self) -> ~_Self

**Inherited from:** IPin.opposite

Return an IRay with same position but opposite orientation

::
    
    def with_orientation(self, *, degrees: Optional[float] = None, radians: Optional[float] = None)

Return a new pin with the given orientation.