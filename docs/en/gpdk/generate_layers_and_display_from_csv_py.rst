generate_layers_and_display_from_csv_py.rst
============================================================

该脚本可以实现将layers.csv文件（:doc:`layers_csv`）转换成GPDK需要用到的脚本文件layers.py以及display.py。

代码如下::

    from pathlib import Path

    from fnpcell import all as fp

    # csv file format
    #   PROCESS_DESCRIPTION, PURPOSE_DESCRIPTION are optional
    #   FILL_COLOR,FILL_PATTERN,STROKE_COLOR must appear together or not
    #
    # LAYER,XTYPE,NAME,DESCRIPTION,PROCESS,PROCESS_DESCRIPTION, PURPOSE,PURPOSE_DESCRIPTION,FILL_COLOR,FILL_PATTERN,STROKE_COLOR
    # 1,1,FWG_COR,"Full Etch waveguide core","FWG", "Full etch","COR","Waveguide core",BLUE,DIAGONAL,BLUE
    #
    if __name__ == "__main__":
        folder = Path(__file__).parent
        generated_folder = folder / "generated"
        csv_file = folder / "layers.csv"
        layer_file = generated_folder / "layers.py"
        display_file = generated_folder / "display.py"
        lyp_file = generated_folder / "layers.lyp"

        fp.util.generate_layers_from_csv(csv_file=csv_file, layer_file=layer_file, overwrite=True)
        fp.util.generate_display_from_csv(csv_file=csv_file, display_file=display_file, overwrite=True)
        fp.util.generate_lyp_from_csv(csv_file=csv_file, lyp_file=lyp_file, overwrite=True)

用户只需要了解用途即可。