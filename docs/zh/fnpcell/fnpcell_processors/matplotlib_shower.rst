Module fnpcell.processors.matplotlib_shower
=============================================

Classes
--------

MatplotlibShower
+++++++++++++++++++

::
    
    class MatplotlibShower(*, title: str = 'show', max_cell_depth: int = 9223372036854775807, 
                            show_immediately: bool = True)

An IProcessor processes hierarchical targets in a deep first manner We use processors to plot, export_gds …

Ancestors
___________

::
    
    IProcessor

Methods
___________

::
    
    def enter(self, target: IRunnable) -> bool

**Inherited from:** IProcessor.enter

Called before processing a target. Return True to continue processing child content. 
False to stop here and run exit for the target

::
    
    def exit(self, target: IRunnable) -> None

**Inherited from:** IProcessor.exit

Called after processing a target.

::
    
    def pop_ctm(self)

::
    
    def push_ctm(self)

::
    
    def show(self, title: Optional[str] = None) -> None

::
    
    def toplevel(self)