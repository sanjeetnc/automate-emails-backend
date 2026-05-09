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

receiver_email = "njsa3803@gmail.com"

def send_email(
    receiver_email,
    name,
    subject,
    date,
    morning,
    prelunch,
    postlunch,
    reminder_date
):

    msg = EmailMessage()

    msg["From"] = formataddr(
        ("Intern Sanjit NC", sender_email)
    )

    msg["To"] = receiver_email

    msg["Subject"] = subject

    msg["BCC"] = sender_email

    msg.set_content(
        f"""

Hello {name},

I hope you're doing well.

The tasks completed on {date} are:

Morning (09:00 AM - 11:15 AM):
{morning}

Pre-lunch (11:30 AM - 02:00 PM):
{prelunch}

Post-lunch (02:30 PM - 04:00 PM):
{postlunch}

Reminder Date:
{reminder_date}

Best regards,
Thank you sir,
Intern Sanjit NC

"""
    )

    print("EMAIL_SERVER:", EMAIL_SERVER)

    print("PORT:", PORT)

    with smtplib.SMTP(
        EMAIL_SERVER,
        PORT
    ) as server:

        server.starttls()

        server.login(
            sender_email,
            password_email
        )

        server.send_message(msg)

        print(
            f"Email sent to {receiver_email}"
        )