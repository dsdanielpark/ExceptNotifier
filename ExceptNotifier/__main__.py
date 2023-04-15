import argparse
import subprocess

from ExceptNotifier import (
                        chime_notifier,
                        desktop_notifier,
                        dingtalk_notifier,
                        discord_notifier,
                        mail_notifier,

                        sms_notifier,
                        teams_notifier,
                        telegram_notifier,
                        wechat_notifier,
                        slack_notifier,
                        discord_notifier,
                        kakao_notifier,
                        line_notifier
                        )

def main():
    parser = argparse.ArgumentParser(
        description="ExceptCatch: Use Python's try-except statement to receive notifications more flexibly.")
    parser.add_argument("--verbose", required=False, action="store_true",
                        help="Show All Commands")
    subparsers = parser.add_subparsers()
    
    # Email
    email_parser = subparsers.add_parser(
        name="email", description="Send an email before and after function " +
        "execution, with start and end status (sucessfully or crashed).")
    email_parser.add_argument(
        "--gmail_receiver", type=str, required=True,
        help="The email addresses to notify")
    email_parser.add_argument(
        "--gmail_sender", type=str, required=False,
        help="The email adress to send the messages." +
        "(default: use the same address as the first email in `gmail_receiver`)")
    email_parser.set_defaults(sender_func=mail_notifier)