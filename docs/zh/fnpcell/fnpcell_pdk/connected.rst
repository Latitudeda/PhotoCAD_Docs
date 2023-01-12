Module fnpcell.pdk.connected
==============================

Functions
----------

Connected
+++++++++++

::
    
    def Connected(*, name: str = 'Connected', joints: Iterable[Union[None, Tuple[IOwnedTerminal, IOwnedTerminal], Iterable[ForwardRef('_J')]]], 
                    ports: Sequence[ITerminal], transform: Affine2D = Affine2D.identity()) -> ICellRef

This is connected function, return cell reference.

This function is used to connect one port in the CellRef to the port in the another CellRef.

Args

joints

    in form

    [ cell1["op_0"] <= cell2["op_0"], cell1["op_1"] <= cell2["op_1"], ]

Usage::
    
    device_connected = fp.Connected(joints=[cell1["op_0"] <= cell2["op_0"],],ports=[])