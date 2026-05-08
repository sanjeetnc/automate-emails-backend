from django.utils import timezone

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import EmailRecord
from .serializers import EmailRecordSerializer

from .email_service import send_email


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def send_email(request):

    if request.method == "POST":

        data = json.loads(request.body)

        email = data.get("email")

        return JsonResponse({
            "message": f"Email sent to {email}"
        })

    return JsonResponse({
        "error": "Invalid request"
    })

@api_view(["GET"])
def home(request):

    return Response({
        "message": "Automate Emails Backend Running"
    })


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


@api_view(["GET"])
def get_all_emails(request):

    emails = EmailRecord.objects.all().order_by("-created_at")

    serializer = EmailRecordSerializer(emails, many=True)

    return Response(serializer.data)

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