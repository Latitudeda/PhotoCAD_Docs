Module fnpcell.cell.port
===========================

Functions
-----------

new_port
+++++++++++

::
    
    def new_port(*, name: Union[None, str, Hidden], position: Optional[Tuple[float, float]] = None,
                 orientation: Optional[float] = None, at: Optional[IRay] = None,
                 waveguide_type: IWaveguideType, shape: Optional[IShape] = None) -> IPort

Create a new optical port.
Orientation in radians.

Classes
---------

OwnedPort
+++++++++++

::
    
    class OwnedPort(name: Optional[str], raw: IPort, owner: ICellRef,
                     assigned_orientation: Optional[float] = None, hidden: bool = False)

OwnedPort is for defining a port owned by a CellRef.
OwnedPort with owner attribute can appoint to it's owner, 
owner is a CellRef Any modification will create new OwnedPort instead of modify the original OwnedPort.

Ancestors
___________

::
    
    fnpcell.cell.port._PortMixin, IOwnedPort, IPort, IOwnedTerminal, IOwned, 
    ITerminal, IUpdatable, IRay, IPositioned, IRunnable

Class variables
__________________

::
    
    var assigned_orientation: Optional[float]
    var hidden: bool
    var name: Optional[str]
    var owner: ICellRef
    var raw: IPort

Static methods
_________________

::
    
    def from_port(port: IPort, owner: ICellRef) -> IOwnedPort

Return OwnedPort.

Instance variables
_____________________

::
    
    var annotation

Return composite.

::
    
    var orientation: float

Return calculated orientation take owner's transform into account.

::
    
    var position: Tuple[float, float]

Return position.

::
    
    var shape: IShape

Return pin shape.

::
    
    var waveguide_type: IWaveguideType

Return waveguide_type.

Methods
___________

::
    
    def advanced(self: ~_Self, distance: float) -> ~_Self

**Inherited from:** IOwnedPort.advanced

Return an IRay with advanced position through orientation.

::
    
    def c_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedPort.c_mirrored

Owner center mirrored.

::

    def flatten(self) -> Port

Return port.

::
    
    def h_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedPort.h_mirrored

Owner horizontal mirrored.

::
    
    def opposite(self: ~_Self) -> ~_Self

**Inherited from:** IOwnedPort.opposite

Return an IRay with same position but opposite orientation.

::
    
    def repositioned(self, *, at: Union[Tuple[float, float], IPositioned, IRay]) -> IOwnedTerminal

**Inherited from:** IOwnedPort.repositioned

Positioned at new point,Owner will translated.

::

    def rotated(self, degrees: Optional[float] = None, radians: Optional[float] = None) -> IOwnedTerminal

**Inherited from:** IOwnedPort.rotated

Rotated both degrees and radians.

::
    
    def v_mirrored(self) -> IOwnedTerminal

**Inherited from:** IOwnedPort.v_mirrored

Owner vertical mirrored.

::
    
    def with_orientation(self, *, degrees: Optional[float] = None, radians: Optional[float] = None)

Return a new OwnedPort with the given orientation.

Port
++++++

::
    
    class Port(name: Optional[str], position: Tuple[float, float], orientation: float,
                 waveguide_type: IWaveguideType, shape: IShape, hidden: bool = False)

Port is for defining a optical Port .
Any modification will create new Port instead of modify the original Port. Orientation in radians.

Usage::
    
    from fnpcell import all as fp

    port = fp.Port(name="op_0", position=(0, 0),...)

Ancestors
__________

::
    
    fnpcell.cell.port._PortMixin, IPort, ITerminal, IUpdatable, IRay, IPositioned, IRunnable

Class variables
___________________

::
    
    var hidden: bool
    var name: Optional[str]
    var orientation: float
    var position: Tuple[float, float]
    var shape: IShape
    var waveguide_type: IWaveguideType

Instance variables
_____________________

::
    
    var annotation

Return port composite on the basis of waveguide_type.

Methods
__________

::
    
    def advanced(self: ~_Self, distance: float) -> ~_Self

**Inherited from:** IPort.advanced

Return an IRay with advanced position through orientation.

::
    
    def opposite(self: ~_Self) -> ~_Self

**Inherited from:** IPort.opposite

Return an IRay with same position but opposite orientation.