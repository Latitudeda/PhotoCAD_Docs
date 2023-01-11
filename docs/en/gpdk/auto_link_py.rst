auto_link_py
============================================================

This function mainly defines the type of transition waveguide when connecting between multiple waveguide types::

    from >> to,  default link_type, default bend_factory
    port 1 >> port 2, default waveguide link type, default bend waveguide type

There are two default methods, and users can also define their own::

    class LINKING_POLICY:
        @fpt.classconst
        @classmethod
        def LESS_TRANS(cls):
            return fpt.LinkingPolicy().updated(
                [
                    #
                    # from >> to,  default link_type, default bend_factory
                    #
                    # (WG.FWG.C.WIRE >> WG.FWG.C.WIRE, LinkPrefer(WG.FWG.C.WIRE), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    #
                    # general rules for waveguides (including non-standard waveguides)
                    #
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

        @fpt.classconst
        @classmethod
        def MAX_SWG(cls):
            return fpt.LinkingPolicy().updated(
                [
                    #
                    # from >> to,  default link_type, default bend_factory
                    #
                    # (WG.FWG.C.WIRE >> WG.FWG.C.WIRE, LinkPrefer(WG.FWG.C.WIRE), BendUsing(WG.FWG.C.WIRE.BEND_EULER)),
                    #
                    # general rules for waveguides (including non-standard waveguides)
                    #
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
