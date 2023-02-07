AutoTransitioned
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the case that the device ports need to connect to different types of waveguides, the ``AutoTransitioned`` method can be used to implement the transition of the component ports, and the specific schematic of this function is given in ``gpdk`` > ``routing`` > ``auto_transitioned`` > ``auto_transitioned.py``, and the core usage is as follows ::

        if __name__ == "__main__":
            from gpdk.util.path import local_output_file

            gds_file = local_output_file(__file__).with_suffix(".gds")
            library = fp.Library()

            TECH = get_technology()
            # =============================================================
            # fmt: off
            from gpdk.components.mmi.mmi import Mmi

            library += AutoTransitioned(device=Mmi(waveguide_type=TECH.WG.FWG.C.WIRE), waveguide_types={"*": TECH.WG.SWG.C.WIRE})

            # fmt: on
            # =============================================================
            fp.export_gds(library, file=gds_file)
            # fp.plot(library)

Here, different waveguide types of component ports are connected by using the ``AutoTransitioned`` class, where the parameter ``device`` is used to receive the components whose ports need to be automatically converted; ``waveguide_types`` receives the waveguide types of the converted ports, where ``*: TECH.WG.SWG.C.WIRE`` is a key-value pair and ``*`` refers to all undefined ports. Finally we can get the following device after port auto-transition.

 .. image:: ../images/autotransition.png