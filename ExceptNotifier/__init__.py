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
from ExceptNotifier.pycore.mail_notifier import SuccessMail, ExceptMail, SendMail
from ExceptNotifier.pycore.slack_notifier import SuccessSlack, ExceptSlack, SendSlack
from ExceptNotifier.pycore.telegram_notifier import (
    SuccessTelegram,
    ExceptTelegram,
    SendTelegram,
)
from ExceptNotifier.pycore.chime_notifier import SuccessChime, ExceptChime, SendChime
from ExceptNotifier.pycore.discord_notifier import (
    SuccessDiscord,
    ExceptDiscord,
    SendDiscord,
)
from ExceptNotifier.pycore.kakao_notifier import SuccessKakao, ExceptKakao, SendKakao
from ExceptNotifier.pycore.line_notifier import SuccessLine, ExceptLine, SendLine
from ExceptNotifier.pycore.teams_notifier import SuccessTeams, ExceptTeams, SendTeams
from ExceptNotifier.pycore.sms_notifier import SuccessSMS, ExceptSMS, SendSMS
from ExceptNotifier.pycore.beep_notifier import SuccessBeep, ExceptBeep, SendBeep
from ExceptNotifier.pycore.wechat_notifier import (
    SuccessWechat,
    ExceptWechat,
    SendWechat,
)
from ExceptNotifier.pycore.desktop_notifier import (
    SuccessDesktop,
    ExceptDesktop,
    SendDesktop,
)
from ExceptNotifier.ipycore.telegram_notifier_ipython import ExceptTelegramIpython
from ExceptNotifier.ipycore.chime_notifier_ipython import ExceptChimeIpython
from ExceptNotifier.ipycore.discord_notifier_ipython import ExceptDiscordIpython
from ExceptNotifier.ipycore.kakao_notifier_ipython import ExceptKakaoIpython
from ExceptNotifier.ipycore.line_notifier_ipython import ExceptLineIpython
from ExceptNotifier.ipycore.mail_notifier_ipython import ExceptMailIpython
from ExceptNotifier.ipycore.slack_notifier_ipython import ExceptSlackIpython
from ExceptNotifier.ipycore.sms_notifier_ipython import ExceptSMSIpython
from ExceptNotifier.ipycore.teams_notifier_ipython import ExceptTeamsIpython
from ExceptNotifier.ipycore.wechat_notifier_ipython import ExceptWechatIpython
from ExceptNotifier.ipycore.beep_notifier_ipython import ExceptBeepIpython
from ExceptNotifier.ipycore.desktop_notifier_ipython import ExceptDesktopIpython

from ExceptNotifier.base.bard_receiver import receive_bard_advice


__all__ = [
    "receive_bard_advice",
    "ExceptBeepIpython",
    "ExceptDesktopIpython",
    "get_resp_openai_advice",
    "SuccessMail",
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

__version__ = "0.2.11"
__author__ = "daniel park <parkminwoo1991@gmail.com>"
