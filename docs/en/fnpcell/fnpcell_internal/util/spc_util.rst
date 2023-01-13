Module fnpcell.internal.util.spc_util
=========================================

Functions
------------

export_spc
+++++++++++++

::
    
    def export_spc(content: Union[ICell, ICellRef, ILibrary], *, 
                    file: Union[str, os.PathLike, io.TextIOBase] = Ellipsis, 
                    components: Union[None, module, Iterable[Callable[..., ICellRef]]] = None, 
                    subcircuit_naming_table: Optional[Dict[ICell, str]] = None)

Export spice file .spc. :param content Cell Library and CellRef can be used as a content. 
:param file spice file, both absolute and relative paths are OK. 
:param components pdk's components,if the cell is in components,it's name in .spc file without _x1,_x2.

if components=None .spc like this .subckt RingFilter op_0 op_1 op_2 op_3 ep_0 ep_1 .ends

.subckt RingFilter_x1 op_0 op_1 op_2 op_3 ep_0 ep_1 .ends RingFilter is different from RingFilter_x1 in in 
internal structure

if components=gpdk.components.all .spc like this,there is no RingFilter_x1 any more. 
.subckt RingFilter op_0 op_1 op_2 op_3 ep_0 ep_1 .ends

Usage::

    from fnpcell import all as fp 
    import gpdk.components.all 
    
    spc_file = Path(file).parent / "local" / Path(file).with_suffix(".spc").name 
    fp.export_spc(library, file=spc_file, components=gpdk.components.all)
