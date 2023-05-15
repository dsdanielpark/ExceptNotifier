# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import platform
from os import environ
from os import system
from ExceptNotifier import beep


class ExceptBeep(BaseException):
    """Override excepthook to send error message to beep.

    :param etype: Error Type
    :type etype: _type_
    :param value: Error Value
    :type value: _type_
    :param tb: Traceback Information
    :type tb: _type_
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
        if environ.get("BEEP_TIME") is not None:
            beep(environ["BEEP_TIME"])
            beep(environ["BEEP_TIME"])
            beep(environ["BEEP_TIME"])
        else:
            beep()
            beep()
            beep()

    @staticmethod
    def beep(sec=1, freq=1000) -> None:
        """Make beep sound

        :param sec: beep duration, defaults to 1
        :type sec: int, optional
        :param freq: beep fequency, defaults to 1000
        :type freq: int, optional
        """

        sys = platform.system()

        if sys == "Windows":
            import winsound

            winsound.Beep(int(1000 * sec), freq)
        else:
            system("play -nq -t alsa synth {} sine {}".format(sec, freq))


class SuccessBeep:
    """Success beep
    """

    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        if environ.get("BEEP_TIME") is not None:
            beep(environ["BEEP_TIME"])
            beep(environ["BEEP_TIME"])
        else:
            beep()
            beep()


class SendBeep:
    """Send beep
    """

    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        if environ.get("BEEP_TIME") is not None:
            beep(environ["BEEP_TIME"])
        else:
            beep()


# if __name__ == "__main__":
#     environ['BEEP_TIME'] = 1
#     sys.excepthook = ExceptBeep.__call__
#     try:
#         print(1 / 20)
#         SuccessBeep().__call__()  # 1 success beep-beep
#     except ExceptBeep as e:  # 2 except beep-beep
#         sys.exit()
#     SendBeep().__call__()  # 3 customized beep-beep
