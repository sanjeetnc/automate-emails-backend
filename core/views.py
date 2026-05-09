from datetime import date

import pandas as pd

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .email_service import send_email


SHEET_ID = "14Y8r1qTXId9m2n36w_Zc2rTCUVJoqGdfBdLAkASQjSo"

URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"


# FRONTEND PAGE
def home(request):

    return render(request, "index.html")


# GOOGLE SHEETS EMAIL AUTOMATION
@api_view(["GET"])
def send_sheet_emails(request):

    df = pd.read_csv(URL)

    df["Date"] = pd.to_datetime(
        df["Date"],
        format="%d-%b-%y"
    )

    df["reminder_date"] = pd.to_datetime(
        df["reminder_date"],
        format="%d-%b-%y"
    )

    present = date.today()

    email_counter = 0

    sent_emails = []

    for _, row in df.iterrows():

        if (
            present >= row["reminder_date"].date()
            and row["mailstatus"] == "no"
        ):

            send_email(
                receiver_email=row["email"],
                name=row["name"],
                subject="Daily Internship Report",
                date=row["Date"].date(),
                morning=row["morning"],
                prelunch=row["prelunch"],
                postlunch=row["postlunch"],
                reminder_date=row["reminder_date"].date().strftime("%d-%b-%y")
            )

            email_counter += 1

            sent_emails.append(row["email"])

    return Response({
        "total_emails_sent": email_counter,
        "emails": sent_emails
    })