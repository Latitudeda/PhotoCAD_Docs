fnpcell.gdsii.gds_importer
===========================

Classes
---------

GDSImporter
++++++++++++

::
    
    class GDSImporter(input: io.IOBase, user_unit: Union[None, float, Literal['db']] = None)

Instance variables
____________________

::
    
    var cell_names
    var unit_ratio: float
    var user_unit: float

Methods
_________

::
    
    def import_cell(self, cell_name: Optional[str], layer_mapper: Callable[[Tuple[int, int]], 
                    Optional[ILayer]], ports: Optional[Iterable[ITerminal]] = None)

::
    
    def top_cells(self, layer_mapper: Callable[[Tuple[int, int]], Optional[ILayer]])