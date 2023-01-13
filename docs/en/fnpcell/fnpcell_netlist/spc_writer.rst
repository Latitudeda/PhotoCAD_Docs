Module fnpcell.netlist.spc_writer
=====================================

Classes
------------

SPCWriter
++++++++++++

::
    
    class SPCWriter(*, file: Union[str, os.PathLike, io.TextIOBase], 
                    name: str = 'library', components: Optional[Iterable[Any]] = None, 
                    subcircuit_naming_table: Optional[Dict[ICell, str]] = None)

An IProcessor processes hierarchical targets in a deep first manner We use processors to plot, export_gds …

Ancestors
__________

::
    
    IProcessor

Instance variables
_____________________

::
    
    var out

Returns the TextIOBase object, which is a file object for writing to the spice file.

Methods
__________

::
    
    def close(self)

Close the open TextIOBase object so that it can no longer be written to.

::
    
    def enter(self, target: IRunnable) -> bool

**Inherited from:** IProcessor.enter

Called before processing a target. Return True to continue processing child content. 
False to stop here and run exit for the target.

::
    
    def exit(self, target: IRunnable) -> None

**Inherited from:** IProcessor.exit

Called after processing a target.

::
    
    def get_generated_instance_name(self, instance: ICellRef) -> str

Generate a new name for the instance by incrementing the instance id. 
The instance id is incremented from 1001, and "U" should be added before the id. 
For example, U1001, U1002, U1003, U1004 and so on.

::
    
    def get_generated_subcircuit_name(self, cell: ICell) -> str

Generate a new name for the specified subcircuit. 
All subcircuit names are unique to distinguish them within the spice file.

::
    
    def get_instance_name(self, instance: ICellRef) -> str

Returns the name of the specified instance, or generates a new name if the instance has no name. 
All instance names are unique to distinguish them within the spice file.

::
    
    def get_subcircuit_name(self, cell: ICell, pcell_class: Optional[Type[PCell]]) -> str

Returns the name of the specified subcircuit. If the subcircuit is in the pdk's components, 
the subcircuit's existing name is returned. If the subcircuit does not have a name, a new 
name is generated. If a subcircuit has the same name as another subcircuit, add an incrementing 
hexadecimal suffix to the original name to distinguish it. For example, LinkBetween, LinkBetween_x1, 
LinkBetween_x2, LinkBetween_x3 and so on. All subcircuit names are unique to distinguish them within the spice file.

::
    
    def pop_ctm(self) -> Affine2D

Delete the saved transformation corresponding to the stack data.

::
    
    def push_ctm(self) -> None

Save the transformation of the corresponding stack data.

::
    
    def toplevel(self) -> bool

Determine whether it is currently in the position of the top-level stack data. 
If the number of stack data is 1, it means yes. This is the second function of 
the _transform_stack, which records the location of the stack data.

::
    
    def write_subcircuit(self, cell: ICell, pcell_class: Optional[Type[PCell]])

Write subcircuits to spice format netlist according to spice syntax. 
he content described in the netlist is consistent with the physical 
design in the layout. The device modules in the layout correspond to 
the subcircuits in the netlist, and the device ports in the layout 
correspond to the subcircuit ports (or line nodes) in the netlist.