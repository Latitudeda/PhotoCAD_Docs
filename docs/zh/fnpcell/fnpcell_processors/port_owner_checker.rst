Module fnpcell.processors.port_owner_checker
==============================================

Classes
---------

PortOwnerChecker
++++++++++++++++++

::
    
    class PortOwnerChecker(port_refs: Tuple[IOwnedTerminal, ...])

An IProcessor processes hierarchical targets in a deep first manner We use processors to plot, export_gds …

Ancestors
_____________

::
    
    IProcessor

Methods
_________

::
    
    def enter(self, target: IRunnable) -> bool

**Inherited from:** IProcessor.enter

Called before processing a target. Return True to continue processing child content. 
False to stop here and run exit for the target

::
    
    def exit(self, target: IRunnable) -> None

**Inherited from:** IProcessor.exit

Called after processing a target.