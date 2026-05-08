import os
import smtplib

from email.message import EmailMessage
from email.utils import formataddr

from dotenv import load_dotenv


load_dotenv()

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


def send_email(record):

    msg = EmailMessage()

    msg["From"] = formataddr(("Automate Emails", sender_email))

    msg["To"] = record.receiver_email

    msg["Subject"] = record.subject

    msg.set_content(
        f"""
Hello {record.name} sir,

daily report.

Date: {record.report_date}

Morning Tasks (09:00 AM - 11:15 AM):
{record.morning_task}

Pre Lunch Tasks (11:30 AM - 02:00 PM):
{record.prelunch_task}

Post Lunch Tasks (02:00 PM - 05:00 PM):
{record.postlunch_task}

Reminder Date :
{record.reminder_date}

Thank you.
"""
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()

        server.login(sender_email, password_email)

        server.send_message(msg)