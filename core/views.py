from django.utils import timezone
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import EmailRecord
from .serializers import EmailRecordSerializer

import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .email_service import send_email


SHEET_ID = "14Y8r1qTXId9m2n36w_Zc2rTCUVJoqGdfBdLAkASQjSo"

URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"


# FRONTEND PAGE
def home(request):

    return render(request, "index.html")


# SEND EMAIL API
@api_view(["POST"])
def send_email_api(request):

    serializer = EmailRecordSerializer(data=request.data)

    if serializer.is_valid():

        email_record = serializer.save()

        try:

            send_email(email_record)

            email_record.status = "sent"

            email_record.sent_at = timezone.now()

            email_record.save()

            return Response({
                "message": "Email Sent Successfully"
            })

        except Exception as e:

            email_record.status = "failed"

            email_record.save()

            return Response({
                "error": str(e)
            }, status=500)

    return Response(serializer.errors, status=400)


# GET ALL EMAILS
@api_view(["GET"])
def get_all_emails(request):

    emails = EmailRecord.objects.all().order_by("-created_at")

    serializer = EmailRecordSerializer(
        emails,
        many=True
    )

    return Response(serializer.data)


# GET SINGLE EMAIL
@api_view(["GET"])
def get_single_email(request, id):

    try:

        email = EmailRecord.objects.get(id=id)

        serializer = EmailRecordSerializer(email)

        return Response(serializer.data)

    except EmailRecord.DoesNotExist:

        return Response({
            "error": "Email not found"
        }, status=404)


# DELETE EMAIL
@api_view(["DELETE"])
def delete_email(request, id):

    try:

        email = EmailRecord.objects.get(id=id)

        email.delete()

        return Response({
            "message": "Email deleted successfully"
        })

    except EmailRecord.DoesNotExist:

        return Response({
            "error": "Email not found"
        }, status=404)
        
        
        from datetime import date


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
                reminder_date=row["reminder_date"].date()
            )

            email_counter += 1

            sent_emails.append(row["email"])

    return Response({
        "total_emails_sent": email_counter,
        "emails": sent_emails
    })