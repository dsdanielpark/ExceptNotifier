# Copyright 2023 parkminwoo
from ExceptNotifier import beep


def ExceptBeepIpython(shell, etype, evalue, tb, tb_offset=1):
    """ExceptNotifier function for overriding custom execute in ipython for sounding system beep.

    :param shell: Excecuted shell 
    :type shell: _type_
    :param etype: Error type
    :type etype: _type_
    :param evalue: Error value
    :type evalue: _type_
    :param tb: TraceBack
    :type tb: _type_
    :param tb_offset: Offset of traceback, defaults to 1
    :type tb_offset: int, optional
    """
    beep()
    beep()
    beep()
