Module fnpcell.internal.plogic_util
====================================

Functions
-----------

export_layout_json
+++++++++++++++++++++

::
    
    def export_layout_json(content: Union[ICell, ICellRef, ILibrary], *, 
                            file: Union[str, os.PathLike, io.TextIOBase])

Output a json format file containing all layout information of the device.

export_lyp_json
+++++++++++++++++

::
    
    def export_lyp_json(TECH: Any, *, file: Union[str, os.PathLike], 
                        name_format: str = '{layer_name} {layer_no}.{datatype_no}')

Export lyp file .lyp

Usage

::
    
    lyp_file = Path(file).with_name("gpdk.lyp")
    fp.export_lyp(TECH, file=lyp_file, name_format="{layer_name} {layer_no}.{datatype_no}")

export_pls
+++++++++++

::
    
    def export_pls(content: Union[ICell, ICellRef, ILibrary], *, 
                    file: Union[str, os.PathLike, io.TextIOBase], 
                    components: Union[None, module, Iterable[Callable[..., ICellRef]]] = None, 
                    instance_naming_table: Optional[Dict[ICellRef, str]] = None)

Export pls file .pls.

Args

content
    Cell Library and CellRef can be used as a content.

file
    pls file or IOBase object, if it is a pls file, both absolute and relative paths are OK.

components
    pdk's components,if the cell is in components,it's name in .pls file without _x1,_x2.

instance_naming_table
    Store the name of the instance of each Cell and output it to the pls file.

Usage

::
    
    from fnpcell import all as fp 
    import gpdk.components.all 
    pls_file = Path(file).parent / "local" / Path(file).with_suffix(".pls").name 
    fp.export_pls(library, file=pls_file, components=gpdk.components.all, instance_naming_table=instance_naming_table)

gds2json
+++++++++++

::
    
    def gds2json(gds_file: Union[str, os.PathLike, io.TextIOBase], 
                    json_file: Union[str, os.PathLike, io.TextIOBase])

Import a device from a gds file and output a json format file containing all layout information for this device.

Classes
---------

JSONEncoderExt
+++++++++++++++++

::
    
    class JSONEncoderExt(instance_naming_table: Mapping[ICellRef, str])

Class variables
___________________

::
    
    var instance_naming_table: Mapping[ICellRef, str]

LayoutWriter
+++++++++++++

::
    
    class LayoutWriter(*, name: str = 'library', layer_mapper: Optional[Callable[[Tuple[int, int]], 
                        Optional[Tuple[int, int]]]] = None, cell_naming_table: Optional[Dict[ICell, str]] = None, 
                        instance_naming_table: Optional[Dict[ICellRef, str]] = None, 
                        db_unit: float, user_unit: float)

An IProcessor processes hierarchical targets in a deep first manner We use processors to plot, export_gds …

Ancestors
__________

::
    
    IProcessor

Instance variables
____________________

::
    
    var result

Methods
__________

::
    
    def enter(self, target: IRunnable) -> bool

**Inherited from:** IProcessor.enter

Called before processing a target. Return True to continue processing child content. False to stop here 
and run exit for the target.

::
    
    def exit(self, target: IRunnable) -> None

**Inherited from:** IProcessor.exit

Called after processing a target.

::
    
    def get_cell_name(self, cell: ICell) -> str

Returns the name of the specified cell, or generates a new name if the cell has no name. 
If a cell has the same name as another cell, add an incrementing hexadecimal suffix to 
the original name to distinguish it. For example wg, wg_x1, wg_x2, wg_x3, wg_x4 and so on. 
All cell names are unique to distinguish the reference structure in the layout section of the json file.

::
    
    def get_generated_name(self, cell: ICell) -> str

Generate a new name for the specified cell, all cell names are unique to distinguish the 
reference structure in the layout section of the json file.

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

NetlistWriter
++++++++++++++

::
    
    class NetlistWriter(*, name: str = 'library', components: Optional[Iterable[Any]] = None, 
                        subcircuit_naming_table: Optional[Dict[ICell, str]] = None, 
                        instance_naming_table: Optional[Dict[ICellRef, str]] = None)

An IProcessor processes hierarchical targets in a deep first manner We use processors to plot, export_gds …

Ancestors
___________

::
    
    IProcessor

Instance variables
_____________________

::
    
    var instance_naming_table
    var result

Methods
__________

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

Generate a new name for the specified subcircuit. All subcircuit names are 
unique to distinguish them in the netlist section of the json file.

::
    
    def get_instance_name(self, instance: ICellRef) -> str

Returns the name of the specified instance, or generates a new name if the instance has no name. 
All instance names are unique to distinguish them in the netlist section of the json file.

::
    
    def get_subcircuit_name(self, cell: ICell, pcell_class: Optional[type]) -> str

Returns the name of the specified subcircuit. If the subcircuit is in the pdk's components, 
the subcircuit's existing name is returned. If the subcircuit does not have a name, a new 
name is generated. If a subcircuit has the same name as another subcircuit, add an incrementing 
hexadecimal suffix to the original name to distinguish it. For example, LinkBetween, LinkBetween_x1, 
LinkBetween_x2, LinkBetween_x3 and so on. All subcircuit names are unique to distinguish them in the 
netlist section of the json file.

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

All subcircuits in the spice format netlist are represented in json format. 
The content described in the netlist is consistent with the physical design 
in the layout. The device modules in the layout correspond to the subcircuits 
in the netlist. The device ports in the layout correspond to the subcircuit 
ports (or line nodes) in the netlist.