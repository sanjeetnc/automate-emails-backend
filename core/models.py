from django.db import models


class EmailRecord(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("sent", "Sent"),
        ("failed", "Failed"),
    ]

    name = models.CharField(max_length=200)

    receiver_email = models.EmailField()

    subject = models.CharField(max_length=255)

    morning_task = models.TextField()

    prelunch_task = models.TextField()

    postlunch_task = models.TextField()

    report_date = models.DateField()

    reminder_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"