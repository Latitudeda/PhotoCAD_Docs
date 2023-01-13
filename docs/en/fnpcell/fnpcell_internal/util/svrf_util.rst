Module fnpcell.internal.util.svrf_util
========================================

Functions
------------

export_svrf_template
++++++++++++++++++++++

::
    
    def export_svrf_template(TECH: Any)

export svrf template.

Usage::
    
    fp.export_svrf_template(TECH)

generate_svrf
+++++++++++++++

::
    
    def generate_svrf(*, top_cell_name: str, gds_path: Union[str, os.PathLike], 
                        file: Union[str, os.PathLike, io.TextIOBase])

Generate svrf file for drc. :param top_cell_name top cell's name. 
:param gds_filename gds file path,both absolute and relative paths are OK. 
:param filename .svrf file saved path.

Usage::
    
    gds_file = Path(file).parent / "local" / Path(file).with_suffix(".gds").name 
    svrf_file = Path(file).parent / "local" / Path(file).with_suffix(".svrf").name 
    fp.generate_svrf(top_cell_name="svrf", gds_path=gds_file, file=svrf_file)