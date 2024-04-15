PhotoCAD Hands-on
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
   **重要说明：用户手册中的脚本布局不可能与 Python 脚本的格式完全一致，手册中的代码段落仅供参考。实际代码格式请参阅软件包中的 Python 源代码。**

本部分适用于已安装 PyCharm (Python 3.8) 并熟悉如何使用 PyCharm 的用户。有关 **PhotoCAD** 的详细文档，请从 ``教程`` 部分开始。

1. 获取 **PhotoCAD** 安装包后，解压缩并找到 "Installation Instructions.pdf" 文件，按照 "Installation Instructions.pdf" 中的详细说明进行操作。

2. 按照安装说明成功安装 **PhotoCAD** 后，您可以继续以下操作，快速体验 **PhotoCAD**.

3. 初识元件脚本:

   在 PyCharm 的当前项目中，找到 ``External Libraries`` > ``site-packages`` > ``gpdk`` > ``components`` > ``bend`` > ``bend_bezier.py`` 文件并双击，就会打开贝塞尔型弯曲波导的 python 源代码（如下图所示）：
   
   .. image:: ../images/quickstart1.png
   
   
4. 运行脚本并查看布局:

   在运行 ``bend_bezier.py`` 后，会在 ``gpdk`` > ``components`` > ``bend`` 下生成一个 ``local`` 文件夹, 并在 ``local`` 文件夹下生成 ``bend_bezier.gds`` 文件（目前 bend 文件夹下已经有一个 local 文件夹，运行脚本后不会创建新的 local 文件夹，默认情况下，新生成的文件会替换本地文件夹中的同名文件）。请注意，运行该脚本文件有两种常见方式。

   4.1 方式一：单击代码编辑区的右键，然后单击 ``Run bend_bezier`` ，如图中红色箭头所示。
   
   .. image:: ../images/quickstart2.png
   
   4.2 方式二：如下图所示，首先确保第一个红色箭头显示 ``Current File`` 或者 ``bend_bezier`` ，再点击第二个箭头。

   .. image:: ../images/quickstart3.png
   
   4.3 运行成功后，可以看到如下所示的信息。
   
   .. image:: ../images/quickstart4.png
   
   4.4 使用 KLayout 等布局工具打开 GDS 文件以查看版图。在左侧箭头所示的列表中，您可以看到两个布局单元： ``BendBezier`` 和 ``BendBezier_q``，当前显示的是 ``BendBezier_q``.
   
   .. image:: ../images/quickstart5.png

5. 使用 ``class`` 创建相应的器件 (instance).

   在 PyCharm 中查看 ``bend_bezier.py`` 的源代码，源代码通过 ``library +=`` 创建了两个 ``class BendBezier()`` 实例::
   
      library += BendBezier()
      library += BendBezier(name="q", start=(0, 0), controls=[(30, 30)], end=(60, 0), waveguide_type=TECH.WG.FWG.C.WIRE), transform=fp.translate(0,40))
      
   其中，第一个器件使用默认参数生成；第二个器件使用以下参数生成::
   
      name="q"                       定义器件的特定名称 q;
      start=(0, 0)                   定义贝塞尔曲线的起点为 (0,0);
      controls=[(30, 30)]            定义贝塞尔曲线经过的控制点为 (30,30);
      end=(60, 0)                    定义贝塞尔曲线的终点为 (60,0);
      waveguide_type=WG.FWG.C.WIRE   定义曲线生成弯曲波导所使用的波导类型;
      transform=fp.translate(0, 40)) 定义布局单元相对于原点的位置;
      
   有关该设备参数的详细说明，请参阅图中 python 脚本的描述：

   .. image:: ../images/quickstart6.png
   
6. 尝试修改 bend_bezier.py 源代码中生成的实例数量和参数，并观察其布局形状的变化。



