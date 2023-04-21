# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo

from ExceptNotifier.utils.kakao_token import get_authorize_code, save_token

from ExceptNotifier.base.kakao_sender import send_kakao_msg
from ExceptNotifier.base.mail_sender import send_gmail_msg
from ExceptNotifier.base.slack_sender import send_slack_msg
from ExceptNotifier.base.telegram_sender import send_telegram_msg
from ExceptNotifier.base.chime_sender import send_chime_msg
from ExceptNotifier.base.discord_sender import send_discord_msg
from ExceptNotifier.base.line_sender import send_line_msg
from ExceptNotifier.base.teams_sender import send_teams_msg
from ExceptNotifier.base.whatsapp_sender import send_whatsapp_msg
from ExceptNotifier.base.sms_sender import send_sms_msg
from ExceptNotifier.base.beep_sender import beep
from ExceptNotifier.base.openai_receiver import receive_openai_advice
from ExceptNotifier.base.openai_receiver import get_resp_openai_advice
from ExceptNotifier.base.wechat_sender import send_wechat_msg
from ExceptNotifier.base.desktop_sender import send_desktop_msg

from ExceptNotifier.python.mail_notifier import SuccessMail, ExceptMail, SendMail
from ExceptNotifier.python.slack_notifier import SuccessSlack, ExceptSlack, SendSlack
from ExceptNotifier.python.telegram_notifier import (
    SuccessTelegram,
    ExceptTelegram,
    SendTelegram,
)
from ExceptNotifier.python.chime_notifier import SuccessChime, ExceptChime, SendChime
from ExceptNotifier.python.discord_notifier import (
    SuccessDiscord,
    ExceptDiscord,
    SendDiscord,
)
from ExceptNotifier.python.kakao_notifier import SuccessKakao, ExceptKakao, SendKakao
from ExceptNotifier.python.line_notifier import SuccessLine, ExceptLine, SendLine
from ExceptNotifier.python.teams_notifier import SuccessTeams, ExceptTeams, SendTeams
from ExceptNotifier.python.sms_notifier import SuccessSMS, ExceptSMS, SendSMS
from ExceptNotifier.python.beep_notifier import SuccessBeep, ExceptBeep, SendBeep
from ExceptNotifier.python.wechat_notifier import (
    SuccessWechat,
    ExceptWechat,
    SendWechat,
)
from ExceptNotifier.python.desktop_notifier import (
    SuccessDesktop,
    ExceptDesktop,
    SendDesktop,
)

from ExceptNotifier.ipython.telegram_notifier_ipython import ExceptTelegramIpython
from ExceptNotifier.ipython.chime_notifier_ipython import ExceptChimeIpython
from ExceptNotifier.ipython.discord_notifier_ipython import ExceptDiscordIpython
from ExceptNotifier.ipython.kakao_notifier_ipython import ExceptKakaoIpython
from ExceptNotifier.ipython.line_notifier_ipython import ExceptLineIpython
from ExceptNotifier.ipython.mail_notifier_ipython import ExceptMailIpython
from ExceptNotifier.ipython.slack_notifier_ipython import ExceptSlackIpython
from ExceptNotifier.ipython.sms_notifier_ipython import ExceptSMSIpython
from ExceptNotifier.ipython.teams_notifier_ipython import ExceptTeamsIpython
from ExceptNotifier.ipython.wechat_notifier_ipython import ExceptWechatIpython
from ExceptNotifier.ipython.beep_notifier_ipython import ExceptBeepIpython
from ExceptNotifier.ipython.desktop_notifier_ipython import ExceptDesktopIpython


__all__ = [
    "ExceptBeepIpython",
    "ExceptDesktopIpython" "get_resp_openai_advice" "SuccessMail",
    "ExceptMail",
    "SendMail",
    "SuccessSlack",
    "ExceptSlack",
    "SendSlack",
    "SuccessTelegram",
    "ExceptTelegram",
    "SendTelegram",
    "get_authorize_code",
    "save_token",
    "send_kakao_msg",
    "send_gmail",
    "send_slack_msg",
    "send_telegram_msg",
    "SuccessChime",
    "ExceptChime",
    "SendChime",
    "SuccessDiscord",
    "ExceptDiscord",
    "SendDiscord",
    "SuccessKakao",
    "ExceptKakao",
    "SendKakao",
    "SuccessLine",
    "ExceptLine",
    "SendLine",
    "SuccessTeams",
    "ExceptTeams",
    "SendTeams",
    "send_chime_msg",
    "send_discord_msg",
    "send_line_msg",
    "send_teams_msg",
    "send_whatsapp_msg",
    "SuccessSMS",
    "ExceptSMS",
    "SendSMS",
    "send_sms_msg",
    "SuccessBeep",
    "ExceptBeep",
    "SendBeep",
    "receive_openai_advice",
    "beep",
    "send_gmail_msg",
    "SuccessWechat",
    "ExceptWechat",
    "SendWechat",
    "send_wechat_msg",
    "send_desktop_msg",
    "SuccessDesktop",
    "ExceptDesktop",
    "SendDesktop",
    "ExceptTelegramIpython",
    "ExceptTelegramIpython",
    "ExceptChimeIpython",
    "ExceptDiscordIpython",
    "ExceptKakaoIpython",
    "ExceptLineIpython",
    "ExceptMailIpython",
    "ExceptSlackIpython",
    "ExceptSMSIpython",
    "ExceptTeamsIpython",
    "ExceptWechatIpython",
]

__version__ = "0.2.0"
__author__ = "daniel park <parkminwoo1991@gmail.com>"
