layers_csv
====================

layers.csv文件是用户可编辑修改层级信息的文件。

文件内容格式如下::

    LAYER,DATATYPE,NAME,DESCRIPTION,PROCESS,PROCESS_DESCRIPTION,PURPOSE,PURPOSE_DESCRIPTION,FILL_COLOR,FILL_PATTERN,STROKE_COLOR
    1,1,FWG_COR,"Full Etch waveguide core",FWG,"Full etch",COR,"Waveguide core",BLUE,DIAGONAL,BLUE
    1,2,FWG_CLD,"Full Etch waveguide cladding",FWG,"Full etch",CLD,"Waveguide cladding",BLUE,BACK_DIAGONAL,BLUE
    1,4,FWG_TRE,"Full Etch waveguide trench",FWG,"Full etch",TRE,"Waveguide trench"
    1,5,FWG_HOL,"Full Etch waveguide hole lattice",FWG,"Full etch",HOL,"Waveguide hole lattice"
    2,1,SWG_COR,"Shallow Etch waveguide core",SWG,"Shallow etch",COR,"Waveguide core"
    2,2,SWG_CLD,"Shallow Etch waveguide cladding",SWG,"Shallow etch",CLD,"Waveguide cladding"
    2,4,SWG_TRE,"Shallow Etch waveguide trench",SWG,"Shallow etch",TRE,"Waveguide trench"
    2,5,SWG_HOL,"Shallow Etch waveguide hole lattice",SWG,"Shallow etch",HOL,"Waveguide hole lattice"
    3,1,MWG_COR,"Medium Etch waveguide core",MWG,"Medium etch",COR,"Waveguide core"
    3,2,MWG_CLD,"Medium Etch waveguide cladding",MWG,"Medium etch",CLD,"Waveguide cladding"
    3,4,MWG_TRE,"Medium Etch waveguide trench",MWG,"Medium etch",TRE,"Waveguide trench"
    3,5,MWG_HOL,"Medium Etch waveguide hole lattice",MWG,"Medium etch",HOL,"Waveguide hole lattice"
    20,3,NP_DRW,"NP, for MOD slab, Ge etc.",NP,"NP, for MOD slab, Ge etc.",DRW,"Drawing"
    21,3,PP_DRW,"PP, for MOD slab, Ge etc.",PP,"PP, for MOD slab, Ge etc.",DRW,"Drawing"
    23,3,N_DRW,"N type light doping",N,"N type light doping",DRW,"Drawing"
    24,3,P_DRW,"P type light doping",P,"P type light doping",DRW,"Drawing"
    25,3,N2_DRW,"N2 type light doping 2",N2,"N type light doping 2",DRW,"Drawing"
    26,3,P2_DRW,"P2 type light doping 2",P2,"P type light doping 2",DRW,"Drawing"
    27,3,NPP_DRW,"N++ implement",NPP,"N++ implant",DRW,"Drawing"
    28,3,PPP_DRW,"P++ implement",PPP,"P++ implant",DRW,"Drawing"
    29,3,GE_DRW,"Germanium epitaxy",GE,"Ge epitaxy",DRW,"Drawing"
    30,3,SIL_DRW,"Silicide area",SIL,"Silicide area",DRW,"Drawing"
    31,3,TIN_DRW,"TiN heater",TIN,"TiN Metal heater",DRW,"Drawing"
    32,3,CONT_DRW,"Contact",CONT,"Contact",DRW,"Drawing"
    33,3,M1_DRW,"Metal 1",M1,"Metal 1",DRW,"Drawing"
    34,3,VIA1_DRW,"Via 1 on M1",VIA1,"VIA1 on M1 ",DRW,"Drawing"
    35,3,M2_DRW,"Metal 2",M2,"Metal 2",DRW,"Drawing"
    36,3,VIA2_DRW,"Via 2 on M2",VIA2,"VIA2 on M2 ",DRW,"Drawing"
    43,3,MT_DRW,"Metal Top",MT,"Metal Top",DRW,"Drawing"
    50,11,PASS_EC,"Passivation, open EC",PASS,"Passivation open window",EC,""
    50,12,PASS_GC,"Passivation, open GC",PASS,"Passivation open window",GC,""
    50,13,PASS_MT,"Passivation, open MT",PASS,"Passivation open window",MT,""
    51,3,TH_ISO_DRW,"Thermal isolation",TH_ISO,"Thermal isolation",DRW,"Drawing"
    52,3,DT_DRW,"Deep Trench for edge coupler",DT,"Deep Trench for edge coupler",DRW,"Drawing"
    55,3,LABEL_DRW,"Label to print on FWG",LABEL,"Label to print on FWG",DRW,"Drawing"
    56,30,TEXT_NOTE,"Text layer, not to print on wafer",TEXT,"Text, not to print on wafer",NOTE,"Note"
    60,21,IOPORT_OREC,"Optical port, for testing",IOPORT,"Port, for testing",OREC,"Optical"
    60,22,IOPORT_EREC,"Electrical port, for testing",IOPORT,"Port, for testing",EREC,"Electrical"
    70,30,PINREC_NOTE,"Pin rectangle, for LVS, DRC",PINREC,"Pin rectangle, for LVS, DRC",NOTE,"Note"
    70,31,PINREC_FWG,"Pin rectangle, for LVS, DRC",PINREC,"Pin rectangle, for LVS, DRC",FWG,"Full etch"
    70,32,PINREC_SWG,"Pin rectangle, for LVS, DRC",PINREC,"Pin rectangle, for LVS, DRC",SWG,"Shallow etch"
    70,33,PINREC_MWG,"Pin rectangle, for LVS, DRC",PINREC,"Pin rectangle, for LVS, DRC",MWG,"Medium etch"
    70,41,PINREC_TEXT,"Pin rectangle, for LVS, DRC",PINREC,"Pin rectangle, for LVS, DRC",TEXT,"Text"
    71,30,FIBREC_NOTE,"Fiber rectangle, for LVS, DRC",FIBREC,"Fiber rectangle, for LVSS, DRC",NOTE,"Note"
    72,30,FIBTGT_NOTE,"Fiber Target for LVS",FIBTGT,"Fiber Target for LVS",NOTE,"Note"
    80,30,DEVREC_NOTE,"Device rectangle, for LVS, DRC",DEVREC,"Device rectangle, for LVS, DRC",NOTE,"Note"
    90,30,PAYLOAD_NOTE,"Design area",PAYLOAD,"Design area",NOTE,"Note"
    81,3,M1KO_DRW,"Tilling keep-out for M1",M1KO,"Tilling keep-out for M1",DRW,"Drawing"
    82,3,MTKO_DRW,"Tilling keep-out for MT",MTKO,"Tilling keep-out for MT",DRW,"Drawing"
    83,3,SIKO_DRW,"Tiliing keep-out for Silicon",SIKO,"Tiliing keep-out for Silicon",DRW,"Drawing"
    91,35,FLYLINE_MARK,"Flyline for insufficient space in AutoLink",FLYLINE,"Fly line",MARK,"Mark"
    92,35,ERROR_MARK,"Error mark",ERROR,"Error",MARK,"Mark"

数据从前至后分别表示，数据间以英文制表符“,”间隔，具体可查看csv文件的格式标准。

- 层
- 数据类型
- 层名
- 描述
- 工艺
- 工艺描述
- 目的
- 目的描述
- 填充颜色
- 填充图形
- 描边颜色