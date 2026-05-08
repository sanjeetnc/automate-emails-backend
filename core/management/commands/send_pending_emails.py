from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import EmailRecord
from core.email_service import send_email


class Command(BaseCommand):

    help = "Send pending emails automatically"

    def handle(self, *args, **kwargs):

        today = timezone.now().date()

        pending_emails = EmailRecord.objects.filter(
            status="pending",
            reminder_date__lte=today
        )

        if not pending_emails.exists():

            self.stdout.write(
                self.style.WARNING("No pending emails found")
            )

            return

        for email_record in pending_emails:

            try:
                send_email(email_record)

                email_record.status = "sent"

                email_record.sent_at = timezone.now()

                email_record.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Email sent to {email_record.receiver_email}"
                    )
                )

            except Exception as e:

                email_record.status = "failed"

                email_record.save()

                self.stdout.write(
                    self.style.ERROR(
                        f"Failed sending to {email_record.receiver_email}: {str(e)}"
                    )
                )