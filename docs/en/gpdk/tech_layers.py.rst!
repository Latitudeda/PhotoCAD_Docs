.. _layers.py :

layers.py
===================

``layers.py`` was generated from :ref:`generate layers and display from csv file.py`. The layer information will be stored in this file and will be ready for further call. However, users are able to adjust the information of the layers manually for some specific reasons (sometimes the rules of the layer or the datatype is forbidden or restricted when inserting to the csv file and generate automatically to ``layers.py``)

The file content format is as follows:

::

    from fnpcell.pdk.technology.all import Layer, LayerEnum, Process, ProcessEnum, Purpose, PurposeEnum


    class PROCESS(ProcessEnum):
        FWG = Process(1, "Full etch")
        SWG = Process(2, "Shallow etch")
        MWG = Process(3, "Medium etch")
        NP = Process(20, "NP, for MOD slab, Ge etc.")
        ...


    class PURPOSE(PurposeEnum):
        COR = Purpose(1, "Waveguide core")
        CLD = Purpose(2, "Waveguide cladding")
        DRW = Purpose(3, "Drawing")
        ...


    class LAYER(LayerEnum):
        FWG_COR = Layer(PROCESS.FWG, PURPOSE.COR, "Full Etch waveguide core")
        FWG_CLD = Layer(PROCESS.FWG, PURPOSE.CLD, "Full Etch waveguide cladding")
        FWG_TRE = Layer(PROCESS.FWG, PURPOSE.TRE, "Full Etch waveguide trench")
        FWG_HOL = Layer(PROCESS.FWG, PURPOSE.HOL, "Full Etch waveguide hole lattice")
        SWG_COR = Layer(PROCESS.SWG, PURPOSE.COR, "Shallow Etch waveguide core")
        SWG_CLD = Layer(PROCESS.SWG, PURPOSE.CLD, "Shallow Etch waveguide cladding")
        SWG_TRE = Layer(PROCESS.SWG, PURPOSE.TRE, "Shallow Etch waveguide trench")
        SWG_HOL = Layer(PROCESS.SWG, PURPOSE.HOL, "Shallow Etch waveguide hole lattice")
        MWG_COR = Layer(PROCESS.MWG, PURPOSE.COR, "Medium Etch waveguide core")
        MWG_CLD = Layer(PROCESS.MWG, PURPOSE.CLD, "Medium Etch waveguide cladding")
        MWG_TRE = Layer(PROCESS.MWG, PURPOSE.TRE, "Medium Etch waveguide trench")
        MWG_HOL = Layer(PROCESS.MWG, PURPOSE.HOL, "Medium Etch waveguide hole lattice")
        ...


    if __name__ == "__main__":
        from pathlib import Path
        from fnpcell import all as fp
        from gpdk.technology import get_technology

        TECH = get_technology()
        folder = Path(__file__).parent
        generated_folder = folder / "generated"
        csv_file = generated_folder / "layers.csv"
        # ================================

        fp.util.generate_csv_from_layers(csv_file=csv_file, layers=TECH.LAYER, display=TECH.DISPLAY, overwrite=True)
