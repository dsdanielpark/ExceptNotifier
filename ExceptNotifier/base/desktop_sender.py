# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
from plyer import notification


def send_desktop_msg(title_msg: str, body_msg: str, DISP_TIME=5) -> None:
    """Sending notification to desktop

    :param title_msg: Title of message
    :type title_msg: str
    :param body_msg: Body of message
    :type body_msg: str
    :param DISP_TIME: Time duration, defaults to 5
    :type DISP_TIME: int, optional
    """
    notification.notify(title=title_msg[:20], message=body_msg[:200], timeout=DISP_TIME)
