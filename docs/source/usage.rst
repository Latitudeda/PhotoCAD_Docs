Usage
=====

.. _installation:

Installation
------------

To use PhotoCAD, first install it using pip:

.. code-block:: console

   (.venv) $ pip install fnpcell
   (.venv) $ pip install gpdk

Creating recipes
----------------

To export a gds file,
you can use the ``fp.export_gds()`` function:


The ``file`` parameter should be either string or ``pathlib.Path`` or some other file-like object.


For example:

>>> from fnpcell import all as fp
>>> ...
>>> fp.export_gds(library, file="example_01.gds")
