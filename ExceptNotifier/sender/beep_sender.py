# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
from os import system
import platform


def beep(sec=1, freq=1000) -> None:
    """Make beep sound

    :param sec: Beep duration, defaults to 1
    :type sec: int, optional
    :param freq: Beep fequency, defaults to 1000
    :type freq: int, optional
    """

    sys = platform.system()

    if sys == "Windows":
        import winsound

        winsound.Beep(int(1000 * sec), freq)
    else:
        system("play -nq -t alsa synth {} sine {}".format(sec, freq))
