import argparse
import subprocess

from ExceptionNotifier import (chime_sender,
                        desktop_sender,
                        dingtalk_sender,
                        discord_sender,
                        email_sender,
                        matrix_sender,
                        rocketchat_sender,
                        slack_sender,
                        sms_sender,
                        teams_sender,
                        telegram_sender,
                        wechat_sender,)

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
    email_parser.set_defaults(sender_func=email_sender)