auto_link_py
============================================================

该脚本主要定义了多种波导类型之间连接时过渡波导的类型::

    from >> to,  default link_type, default bend_factory
    端口1 >> 端口2,默认连接类型,默认弯曲波导

默认方法有两种，用户也可以自行定义::

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

设置的默认规则为::

    DEFAULT = LESS_TRANS