import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")





def send_email(receiver_email,name, subject,date, morning ,prelunch,postlunch, reminder_date):

    msg = EmailMessage()
    msg["From"] = formataddr(("Intern Sanjit NC", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg["BCC"] = sender_email

    msg.set_content(
        f"""
        Hello {name},
        I hope you're doing well. I wanted to share the following information with you:
        The tasks which I have completed today {date} are as follows:

        Date: {date}
        Tasks and Time:
        Time (09:00 AM - 11:15 AM): {morning} (Morning)
        Time (11:30 AM - 02:00 PM): {prelunch} (Pre-lunch)
        Time (02:30 PM - 04:00 PM): {postlunch} (Post-lunch)
        Reminder Date: {reminder_date}

        Best regards,
        Thank you sir,
        Intern Sanjit NC
        """
    )
    print("EMAIL_SERVER:", EMAIL_SERVER)
    print("PORT:", PORT)

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        
        
if __name__ == "__main__":
    send_email(
        subject="Daily Report",
        name="Sanjit NC",
        receiver_email="vikashc030207@gmail.com",
        date="2023-10-01",
        time="10:00 AM",
        tasks="Completed the email automation script."
    )
