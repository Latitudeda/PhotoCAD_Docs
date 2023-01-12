Module fnpcell.cell.cell
==========================

Classes
---------

Cell
++++++++

::

    class Cell(content: Tuple[IElement, ...], ports: Tuple[ITerminal, ...], 
                bands: Optional[FrozenSet[IBand]] = None, name: Optional[str] = None)
    
Cell is for defining a cell with name content and ports.

Any modification will create new cell instead of modify the original cell. A cell is a composite with ports.

Ancestors
___________

::

    fnpcell.cell.cell._CellMixin, ICell, IUpdatable, IRunnableContainer, typing.Generic, IRunnableb
    
Class variables
__________________

::

    var bands: Optional[FrozenSet[IBand]]
    var content: Tuple[IElement, ...]
    var name: Optional[str]
    var ports: Tuple[ITerminal, ...]

Methods
__________

::

    def with_content(self, content: Iterable[IElement]) -> ICell

::

    def with_patches(self, content: Iterable[IElement]) -> ICell
    
::

    def with_ports(self, ports: Sequence[Union[None, str, Hidden]]) -> ICell
    
Return a new cell with the given ports