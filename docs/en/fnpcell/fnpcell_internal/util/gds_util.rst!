Module fnpcell.internal.util.gds_util
=======================================

Functions
------------

export_gds
+++++++++++++

::
    
    def export_gds(content: Union[ICell, ICellRef, ILibrary], *, 
                    file: Union[str, os.PathLike, io.IOBase] = Ellipsis, 
                    layer_mapper: Optional[Callable[[Tuple[int, int]], 
                    Optional[Tuple[int, int]]]] = None, cell_naming_table: Optional[Dict[ICell, str]] = None, 
                    db_unit: Optional[float] = None, user_unit: Optional[float] = None, auto_flatten: bool = True)

Export gds file .gds.

Args
_____

content
    Cell Library and CellRef can be used as a content.

file
    gds file path, both absolute and relative paths are OK.

Usage::
    
    from fnpcell import all as fp

    gds_file = Path(__file__).parent / "local" / Path(__file__).with_suffix(".gds").name
    fp.export_gds(library, file=gds_file)

import_from_gds
+++++++++++++++++

::
    
    def import_from_gds(*, file: Union[str, os.PathLike, io.IOBase], 
                        cell_name: Optional[str] = None, 
                        layer_mapper: Optional[Callable[[Tuple[int, int]], Optional[ILayer]]] = None, 
                        ports: Optional[Iterable[ITerminal]] = None, 
                        user_unit: Union[None, float, Literal['db']] = None)

Import device form gds.

Args
_______

file
    gds file

cell_name
    name of cell to be imported, default to the only(raises if multiple) top cell if absent

layer_mapper
    a callable take a tuple (layer, datatype) as parameter and returns ILayer or None, layer is filtered out if None is returned

Returns An ICell that imported

import_from_json
++++++++++++++++++

::
    
    def import_from_json(*, name: Optional[str] = None, json_path: Union[str, os.PathLike], 
                            library_path: Union[str, os.PathLike, None] = None, 
                            default_layers: Optional[Mapping[str, Any]] = None)

Import device form json file. Args: name: device's name. json_path: json file path. 
json file like this::
    
    {
        "library_path": "cell.gds",
        "cell_name": "cell",
        "layers": {
            "*": "_ERROR_",
            "0/0": "FWG_COR",
        },
        "ports": [
            {
                "name": "op_0",
                "position": [
                    0,
                    0
                ],
                "orientation": {
                    "degrees": 180
                },
                "waveguide_type": {
                    "override": "FWG.C.WIRE",
                    "values": {
                        "core_layout_width": 0.5
                    }
                }
            }
        ]
    }

library_path: gds file path, if specified, take precedence. 
default_layers: default mappling for layers, same structure 
as layers in json, json take precedence

Returns

An instance of the imported cell Usage::
    
    instance = fp.import_from_json(json_path=Path(__file__).with_name("cell.json"))