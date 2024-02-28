步骤5： MMI级联
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本案例利用步骤2(:doc:`Step2`)中的多模干涉仪结构实现多层级联结构，并实现版图绘制。

导入步骤2(:doc:`Step2`)创建的多模干涉仪结构::

    from step.step2.mmi1x2 import MMI1x2

定义级联MMI类，方便后面直接调用::

    @dataclass(eq=False)
    class MMITree(fp.PCell):
        def build(self):
            insts, elems, ports = super().build()
            TECH = get_technology()

            x_spacing = 50
            end_y_spacing = 50
            order = 2
            mmi = MMI1x2()
            num_per_col = []
            v_spacing = []

            for i in range(order):
                num_per_col.append(2**i)
                v_spacing.append(end_y_spacing*(2**(order - i - 1)))

            for i in range(order):
                for j in range(num_per_col[i]):
                    x = i * x_spacing
                    y = (-(num_per_col[i] - 1) * v_spacing[i]/2) + j * v_spacing[i]
                    mmi = mmi["op_0"].repositioned(at=(x,y)).owner
                    insts += mmi, f"{i},{j}"

            mmi_tree = cast(Mapping[str, fp.ICellRef], insts)
            for i in range(order):
                for j in range(num_per_col[i]):
                    if i < order-1:
                        link1 = fp.LinkBetween(start=mmi_tree[f"{i},{j}"]["op_1"],
                                               end=mmi_tree[f"{i+1},{2*j}"]["op_0"],
                                               bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR)
                        insts += link1
                        link2 = fp.LinkBetween(start=mmi_tree[f"{i},{j}"]["op_2"],
                                               end=mmi_tree[f"{i+1},{2*j+1}"]["op_0"],
                                               bend_factory=TECH.WG.FWG.C.WIRE.BEND_CIRCULAR)
                        insts += link2

            ports += mmi_tree["0,0"]["op_0"].with_name("op_0")
            for i in range(num_per_col[-1]):
                ports += mmi_tree[f"{order - 1},{i}"]["op_1"].with_name(f"op_{2*i+1}")
                ports += mmi_tree[f"{order - 1},{i}"]["op_2"].with_name(f"op_{2*i+2}")

            # fmt: on
            return insts, elems, ports

需要说明的是::

    order = 2

这个参数表示的是级联的层级，本案例中我们取的是4。

调用类，并通过布尔运算实现版图设计::

    library += MMITree()
    device = MMITree()
    cor = device.polygon_set(layer=TECH.LAYER.FWG_COR)
    cld = device.polygon_set(layer=TECH.LAYER.FWG_CLD)
    tre = fp.el.PolygonSet.boolean_sub(cld, cor, layer=TECH.LAYER.FWG_TRE)
    library += fp.Device(content=[tre.translated(300, 0)], ports=[])
    fp.export_gds(library, file=gds_file)
    fp.plot(library)
    
MMI级联结构图例展示

.. image:: ../images/MMI_tree.png

其中左侧为包含所有图层信息的版图，局部放大如下

.. image:: ../images/MMI_initial.png

右侧为经过布尔运算的得到的，局部图为

.. image:: ../images/MMI_boolean.png
