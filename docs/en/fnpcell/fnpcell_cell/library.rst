Module fnpcell.cell.library
===============================

Functions
----------

new_library
+++++++++++++

::

    def new_library(*cells: Union[None, ICell, ICellRef]) -> Library
        
Create a library

Classes
---------

Library
+++++++++++

::

    class Library(content: Tuple[ICell, ...])

Library is for defining Library.
Library only stores cells, cell reference will be flattened to cell

Usage::

    from fnpcell import all as fp
    from gpdk.components.bend.bend_euler import BendEuler


    if __name__ == "__main__":
        from pathlib import Path

        gds_file = Path(__file__).parent / "local" / Path(__file__).with_suffix(".gds").name
        library = fp.Library()

        # =======================================================================
        # fmt: off

        library += BendEuler()

        # fmt: on
        # =============================================================
        fp.export_gds(library, file=gds_file)
        # fp.plot(library)

Ancestors
___________

::

    ILibrary, IUpdatable, IRunnableContainer, typing.Generic, IRunnable

Class variables
_________________

::

    var content : Tuple[ICell, ...]