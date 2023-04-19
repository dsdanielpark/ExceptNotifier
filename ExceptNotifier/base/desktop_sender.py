
# coding=utf-8
# Copyright 2023 parkminwoo Authors.

import time
from plyer import notification


def send_desktop_msg(title_msg: str, body_msg: str, DISP_TIME=5) -> None:
    """Send notification to your desktop

    :param title_msg: Notificatrion Title
    :type title_msg: str
    :param body_msg: _description_
    :type body_msg: str
    :param DISP_TIME: _description_, defaults to 5
    :type DISP_TIME: int, optional
    """
    notification.notify(
            title = title_msg,
            message=body_msg ,
            timeout=DISP_TIME)
    