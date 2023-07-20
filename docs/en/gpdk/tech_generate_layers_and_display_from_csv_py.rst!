.. _generate layers and display from csv file.py :


generate layers and display from csv file.py
============================================================

This function enables to convert the ``layers.csv`` file (:doc:`layers_csv`) into the script files ``layers.py`` and ``display.py`` that gpdk needs to use.

::

    from pathlib import Path

    from fnpcell import all as fp

    # csv file format
    #   PROCESS_DESCRIPTION, PURPOSE_DESCRIPTION are optional
    #   FILL_COLOR,FILL_PATTERN,STROKE_COLOR must appear together or not
    #
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

The generated ``layers.py`` and ``display.py`` will be stored under the folder ``generated``, users have to copy and paste it under ``gpdk`` > ``technology`` for further use. ``layers.lyp`` file allows layout tools e.g. Klayout to recognize the layer information when displaying gds file to the layout tool.


