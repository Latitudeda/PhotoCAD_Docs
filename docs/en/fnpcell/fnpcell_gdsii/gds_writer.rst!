Module fnpcell.gdsii.gds_writer
==================================

Classes
--------

GDSWriter
+++++++++++

::
    
    class GDSWriter(*, file: Union[str, os.PathLike, io.IOBase], name: str = 'library', 
                    layer_mapper: Optional[Callable[[Tuple[int, int]], Optional[Tuple[int, int]]]] = None, 
                    cell_naming_table: Optional[Dict[ICell, str]] = None, db_unit: float, user_unit: float, 
                    auto_flatten: bool = True)

An IProcessor processes hierarchical targets in a deep first manner We use processors to plot, export_gds …

Ancestors
__________

    IProcessor

Instance variables
______________________

::
    
    var gds: GDSOutputWriter

Returns the GDSOutputWriter object, which is a file object for writing to the gds file.

Methods
________

::
    
    def close(self)

Close the open GDSOutputWriter object so that it can no longer be written to.

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
    
    def get_cell_name(self, cell: ICell) -> str

Returns the name of the specified cell, or generates a new name if the cell has no name. 
If a cell has the same name as another cell, add an incrementing hexadecimal suffix to 
the original name to distinguish it. For example wg, wg_x1, wg_x2, wg_x3, wg_x4 and so on. 
All cell names are unique to distinguish the reference structure in gds.

::
    
    def get_generated_cell_name(self, cell: ICell) -> str

Generate a new name for the specified cell, all cell names are unique to distinguish 
the reference structure in gds.

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