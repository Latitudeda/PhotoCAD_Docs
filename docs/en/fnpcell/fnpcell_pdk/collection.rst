Module fnpcell.pdk.collection
==============================

Classes
---------

ElementSet
++++++++++++

::
    
    class ElementSet(content: Optional[Dict[Union[str, IElement], IElement]] = None)

A element container, element can be add to it.

Usage::
    
    elems = fp.ElementSet() elems += element

Ancestors
____________

::
    
    fnpcell.pdk.collection._ContentCollection, typing.Generic

Methods
________

::
    
    def new(self, content: Dict[Union[str, IElement], IElement])

Create a element container.

::
    
    def validate(self, value: Any)

Determine value whether a element.

InstanceSet
++++++++++++

::
    
    class InstanceSet(content: Optional[Dict[Union[str, ICell, ICellRef, ICellArray], 
                        Union[ICell, ICellRef, ICellArray]]] = None)

An instance container, instance can be added to it.

Usage::
    
    # create the instance set
    insts = fp.InstanceSet()

    # add an anonymous instance
    insts += instance1

    # add an instance with a key
    insts += instance2, "key"

    # get instance back with the registered key, raises LookupError if "key" not found
    assert insts["key"] is instance2

    # get instance back with the key, returns instance1 as the default
    assert insts.get("badkey", instance1) is instance1

    # get first inserted instance, raises LookupError if empty
    assert insts.first() is instance1

    # get last inserted instance, raises LookupError if empty
    assert insts.last() is instance2

Ancestors
____________

fnpcell.pdk.collection._ContentCollection, typing.Generic

Methods
___________

::
    
    def new(self, content: Dict[Union[str, ICell, ICellRef, ICellArray], Union[ICell, ICellRef, ICellArray]])

Create a instance container.

::
    
    def validate(self, value: Any)

Determine value whether a cell reference.

PortSet
++++++++

::
    
    class PortSet(content: Optional[Dict[Union[str, ITerminal], ITerminal]] = None)

A port container, port can be add to it.

When create a new device(CellRef) this is must.

Usage::
    
    ports = fp.PortSet()
    port_0 = fp.Port(name="op_0", ...)
    ports += port_0  # using port.name as key
    assert ports["op_0"] is port_0

    port_1 = fp.Port(name="op_1", ...)
    ports += port_1, "opt_1"  # assign a key
    assert ports["opt_1"] is port_1

Ancestors
_____________

fnpcell.pdk.collection._ContentCollection, typing.Generic

Methods
________

::
    
    def new(self, content: Dict[Union[str, ITerminal], ITerminal])

Create a port container.

::
    
    def validate(self, value: Any)

Determine value whether a port.