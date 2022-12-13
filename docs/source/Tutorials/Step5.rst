步骤1： 搭建链路基础模块
=====

前言
------------

更多信息参考 引用文档_

这里是其他内容


To use PhotoCAD, first install it using pip:

.. ccc::

    console
   (.venv) $ pip install fnpcell
   (.venv) $ pip install gpdk

.. note::

   This project is under active development.
   llhz

Exporting a GDSII file
----------------------

To export a gds file,
you can use the ``fp.export_gds()`` function:


The ``file`` parameter should be either string or ``pathlib.Path`` or some other file-like object.


For example:

>>> from fnpcell import all as fp
>>> ...
>>> fp.export_gds(library, file="gds_file_name.gds")
