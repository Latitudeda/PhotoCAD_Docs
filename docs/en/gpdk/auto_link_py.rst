auto_link_py
============================================================

This function mainly defines the type of transition waveguide when connecting between multiple waveguide types::

    from >> to,  default link_type, default bend_factory
    port 1 >> port 2, default waveguide link type, default bend waveguide type

There are two default methods, and users can also define their own.

 ``LESS_TRANS``

------------------------
In the first linking method, the default waveguide link type goes with the end type of the waveguide we want to link together, and the bend used here is set to be an Euler bend to minimize waveguide loss according from the experiment.


::

        class LINKING_POLICY:
            @fpt.classconst
            @classmethod
            def LESS_TRANS(cls):
                return fpt.LinkingPolicy().updated(
                    [
                        (type(WG.FWG.C.WIRE) >> type(WG.FWG.C.WIRE), LinkPrefer(WG.FWG.C.WIRE), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                        (type(WG.MWG.C.WIRE) >> type(WG.MWG.C.WIRE), LinkPrefer(WG.MWG.C.WIRE), BendUsing(WG.MWG.C.WIRE.BEND_EULER)),
                        (type(WG.SWG.C.WIRE) >> type(WG.SWG.C.WIRE), LinkPrefer(WG.SWG.C.WIRE), BendUsing(WG.SWG.C.WIRE.BEND_EULER)),
                        #
                        (type(WG.FWG.C.WIRE) >> type(WG.MWG.C.WIRE), LinkPrefer(WG.MWG.C.WIRE), BendUsing(WG.MWG.C.WIRE.BEND_EULER)),
                        (type(WG.MWG.C.WIRE) >> type(WG.SWG.C.WIRE), LinkPrefer(WG.SWG.C.WIRE), BendUsing(WG.SWG.C.WIRE.BEND_EULER)),
                        (type(WG.FWG.C.WIRE) >> type(WG.SWG.C.WIRE), LinkPrefer(WG.SWG.C.WIRE), BendUsing(WG.SWG.C.WIRE.BEND_EULER)),
                        #
                        (type(WG.FWG.C.WIRE) >> type(WG.FWG.C.EXPANDED), LinkPrefer(WG.FWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                        (type(WG.MWG.C.WIRE) >> type(WG.MWG.C.EXPANDED), LinkPrefer(WG.MWG.C.EXPANDED), BendUsing(WG.MWG.C.WIRE.BEND_EULER)),
                        (type(WG.SWG.C.WIRE) >> type(WG.SWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.SWG.C.WIRE.BEND_EULER)),
                        #
                        (type(WG.FWG.C.WIRE) >> type(WG.MWG.C.EXPANDED), LinkPrefer(WG.MWG.C.EXPANDED), BendUsing(WG.MWG.C.EXPANDED.BEND_EULER)),
                        (type(WG.MWG.C.WIRE) >> type(WG.SWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.SWG.C.EXPANDED.BEND_EULER)),
                        (type(WG.FWG.C.WIRE) >> type(WG.SWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.SWG.C.EXPANDED.BEND_EULER)),
                        #
                        (type(WG.FWG.C.EXPANDED) >> type(WG.FWG.C.EXPANDED), LinkPrefer(WG.FWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                        (type(WG.MWG.C.EXPANDED) >> type(WG.MWG.C.EXPANDED), LinkPrefer(WG.MWG.C.EXPANDED), BendUsing(WG.MWG.C.WIRE.BEND_EULER)),
                        (type(WG.SWG.C.EXPANDED) >> type(WG.SWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.SWG.C.WIRE.BEND_EULER)),
                        #
                        (type(WG.FWG.C.EXPANDED) >> type(WG.MWG.C.EXPANDED), LinkPrefer(WG.MWG.C.EXPANDED), BendUsing(WG.MWG.C.EXPANDED.BEND_EULER)),
                        (type(WG.MWG.C.EXPANDED) >> type(WG.SWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.SWG.C.EXPANDED.BEND_EULER)),
                        (type(WG.FWG.C.EXPANDED) >> type(WG.SWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.SWG.C.EXPANDED.BEND_EULER)),
                        #
                    ]
                )


``MAX_SWG``
-----------------
The second link method designated ``SWG`` as the default waveguide link type no matter which type of the waveguide is going to be connected. On the other hand, the bend type is set to be ``FWG.C.WIRE.BEND_EULER`` for the whole scenario.

::

        @fpt.classconst
        @classmethod
        def MAX_SWG(cls):
            return fpt.LinkingPolicy().updated(
                [
                    (type(WG.FWG.C.WIRE) >> type(WG.FWG.C.WIRE), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    (type(WG.MWG.C.WIRE) >> type(WG.MWG.C.WIRE), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    (type(WG.SWG.C.WIRE) >> type(WG.SWG.C.WIRE), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    #
                    (type(WG.FWG.C.WIRE) >> type(WG.MWG.C.WIRE), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    (type(WG.MWG.C.WIRE) >> type(WG.SWG.C.WIRE), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    (type(WG.FWG.C.WIRE) >> type(WG.SWG.C.WIRE), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    #
                    (type(WG.FWG.C.EXPANDED) >> type(WG.FWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    (type(WG.MWG.C.EXPANDED) >> type(WG.MWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    (type(WG.SWG.C.EXPANDED) >> type(WG.SWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    #
                    (type(WG.FWG.C.EXPANDED) >> type(WG.MWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    (type(WG.MWG.C.EXPANDED) >> type(WG.SWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    (type(WG.FWG.C.EXPANDED) >> type(WG.SWG.C.EXPANDED), LinkPrefer(WG.SWG.C.EXPANDED), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    #
                ]
            )

Default rule set ::

    DEFAULT = LESS_TRANS
