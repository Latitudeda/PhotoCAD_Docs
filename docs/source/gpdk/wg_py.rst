wg_py
============================================================

该脚本主要定义了多种波导类型以及宽度等相应的配置。

最终生成的csv::

    NAME,CONFIGURATION
    FWG.C.WIRE_TETM,"core_layout_width=0.64, cladding_layout_width=4.54, core_design_width=0.54, cladding_design_width=4.54, port_names=('op_0', 'op_1')"
    FWG.C.WIRE_TETM.BEND_CIRCULAR,radius_eff=10
    FWG.C.WIRE_TETM.BEND_EULER,"radius_min=3.27, l_max=5"
    FWG.C.WIRE,"core_layout_width=0.55, cladding_layout_width=4.45, core_design_width=0.45, cladding_design_width=4.45, port_names=('op_0', 'op_1')"
    FWG.C.WIRE.BEND_CIRCULAR,radius_eff=3.225
    FWG.C.WIRE.BEND_EULER,"radius_min=3.225, l_max=5"
    FWG.C.EXPANDED_TETM,"core_layout_width=1.7000000000000002, cladding_layout_width=5.6, core_design_width=1.6, cladding_design_width=5.6, port_names=('op_0', 'op_1')"
    FWG.C.EXPANDED_TETM.BEND_CIRCULAR,radius_eff=3.8
    FWG.C.EXPANDED_TETM.BEND_EULER,"radius_min=3.8, l_max=10"
    FWG.C.EXPANDED,"core_layout_width=0.9, cladding_layout_width=4.8, core_design_width=0.8, cladding_design_width=4.8, port_names=('op_0', 'op_1')"
    FWG.C.EXPANDED.BEND_CIRCULAR,radius_eff=3.4
    FWG.C.EXPANDED.BEND_EULER,"radius_min=3.4, l_max=10"
    FWG.O.WIRE_TETM,"core_layout_width=0.532, cladding_layout_width=3.632, core_design_width=0.43200000000000005, cladding_design_width=3.632, port_names=('op_0', 'op_1')"
    FWG.O.WIRE,"core_layout_width=0.4600000000000001, cladding_layout_width=3.5600000000000005, core_design_width=0.36000000000000004, cladding_design_width=3.5600000000000005, port_names=('op_0', 'op_1')"
    FWG.O.EXPANDED_TETM,"core_layout_width=1.3800000000000003, cladding_layout_width=4.4799999999999995, core_design_width=1.2800000000000002, cladding_design_width=4.4799999999999995, port_names=('op_0', 'op_1')"
    FWG.O.EXPANDED,"core_layout_width=0.7400000000000001, cladding_layout_width=3.84, core_design_width=0.6400000000000001, cladding_design_width=3.84, port_names=('op_0', 'op_1')"
    MWG.C.WIRE_TETM,"core_layout_width=1.3499999999999999, cladding_layout_width=11.2, core_design_width=1.2, cladding_design_width=11.2, port_names=('op_0', 'op_1')"
    MWG.C.WIRE_TETM.BEND_CIRCULAR,radius_eff=6.6
    MWG.C.WIRE_TETM.BEND_EULER,"radius_min=6.6, l_max=15"
    MWG.C.WIRE,"core_layout_width=1.15, cladding_layout_width=11.0, core_design_width=1, cladding_design_width=11.0, port_names=('op_0', 'op_1')"
    MWG.C.WIRE.BEND_CIRCULAR,radius_eff=6.5
    MWG.C.WIRE.BEND_EULER,"radius_min=6.5, l_max=15"
    MWG.C.EXPANDED_TETM,"core_layout_width=3.15, cladding_layout_width=13.0, core_design_width=3.0, cladding_design_width=13.0, port_names=('op_0', 'op_1')"
    MWG.C.EXPANDED_TETM.BEND_CIRCULAR,radius_eff=7.5
    MWG.C.EXPANDED_TETM.BEND_EULER,"radius_min=7.5, l_max=25"
    MWG.C.EXPANDED,"core_layout_width=1.65, cladding_layout_width=11.5, core_design_width=1.5, cladding_design_width=11.5, port_names=('op_0', 'op_1')"
    MWG.C.EXPANDED.BEND_CIRCULAR,radius_eff=6.75
    MWG.C.EXPANDED.BEND_EULER,"radius_min=6.75, l_max=25"
    MWG.O.WIRE_TETM,"core_layout_width=1.1099999999999999, cladding_layout_width=8.959999999999999, core_design_width=0.96, cladding_design_width=8.959999999999999, port_names=('op_0', 'op_1')"
    MWG.O.WIRE,"core_layout_width=0.9500000000000001, cladding_layout_width=8.8, core_design_width=0.8, cladding_design_width=8.8, port_names=('op_0', 'op_1')"
    MWG.O.EXPANDED_TETM,"core_layout_width=2.5500000000000003, cladding_layout_width=10.4, core_design_width=2.4000000000000004, cladding_design_width=10.4, port_names=('op_0', 'op_1')"
    MWG.O.EXPANDED,"core_layout_width=1.35, cladding_layout_width=9.200000000000001, core_design_width=1.2000000000000002, cladding_design_width=9.200000000000001, port_names=('op_0', 'op_1')"
    SLOT.C.WIRE,"core_layout_width=1.15, slot_layout_width=0.3, cladding_layout_width=11.0, core_design_width=1.0, slot_design_width=0.3, cladding_design_width=11.0, port_names=('op_0', 'op_1')"
    SLOT.O.WIRE,"core_layout_width=0.9500000000000001, slot_layout_width=0.24, cladding_layout_width=8.8, core_design_width=0.8, slot_design_width=0.24, cladding_design_width=8.8, port_names=('op_0', 'op_1')"
    SWG.C.WIRE_TETM,"core_layout_width=1.3499999999999999, cladding_layout_width=11.2, core_design_width=1.2, cladding_design_width=11.2, port_names=('op_0', 'op_1')"
    SWG.C.WIRE_TETM.BEND_CIRCULAR,radius_eff=6.6
    SWG.C.WIRE_TETM.BEND_EULER,"radius_min=6.6, l_max=15"
    SWG.C.WIRE,"core_layout_width=1.15, cladding_layout_width=11.0, core_design_width=1.0, cladding_design_width=11.0, port_names=('op_0', 'op_1')"
    SWG.C.WIRE.BEND_CIRCULAR,radius_eff=6.5
    SWG.C.WIRE.BEND_EULER,"radius_min=6.5, l_max=15"
    SWG.C.EXPANDED_TETM,"core_layout_width=3.15, cladding_layout_width=13.0, core_design_width=3.0, cladding_design_width=13.0, port_names=('op_0', 'op_1')"
    SWG.C.EXPANDED_TETM.BEND_CIRCULAR,radius_eff=7.5
    SWG.C.EXPANDED_TETM.BEND_EULER,"radius_min=7.5, l_max=25"
    SWG.C.EXPANDED,"core_layout_width=3.15, cladding_layout_width=13.0, core_design_width=3.0, cladding_design_width=13.0, port_names=('op_0', 'op_1')"
    SWG.C.EXPANDED.BEND_CIRCULAR,radius_eff=7.5
    SWG.C.EXPANDED.BEND_EULER,"radius_min=7.5, l_max=25"
    SWG.O.WIRE_TETM,"core_layout_width=1.1099999999999999, cladding_layout_width=8.959999999999999, core_design_width=0.96, cladding_design_width=8.959999999999999, port_names=('op_0', 'op_1')"
    SWG.O.WIRE,"core_layout_width=0.9500000000000001, cladding_layout_width=8.8, core_design_width=0.8, cladding_design_width=8.8, port_names=('op_0', 'op_1')"
    SWG.O.EXPANDED_TETM,"core_layout_width=2.5500000000000003, cladding_layout_width=10.4, core_design_width=2.4000000000000004, cladding_design_width=10.4, port_names=('op_0', 'op_1')"
    SWG.O.EXPANDED,"core_layout_width=1.35, cladding_layout_width=9.200000000000001, core_design_width=1.2000000000000002, cladding_design_width=9.200000000000001, port_names=('op_0', 'op_1')"
    SWGR.C.WIRE,"core_layout_width=1.15, cladding_layout_width=11.0, core_design_width=1.0, cladding_design_width=11.0, port_names=('op_0', 'op_1'), period=1.0, duty_cycle=0.5"
    SWGR.O.WIRE,"core_layout_width=0.9500000000000001, cladding_layout_width=8.8, core_design_width=0.8, cladding_design_width=8.8, port_names=('op_0', 'op_1'), period=1.0, duty_cycle=0.5"

通过csv文件我们可以查看各种类型波导的配置包括尺寸以及仿真信息。