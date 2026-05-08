from django.urls import path

from .views import send_email

urlpatterns = [
    path('send/', send_email),
]

from .views import (
    home,
    send_email_api,
    get_all_emails,
    get_single_email,
    delete_email
)

urlpatterns = [
    path("", home),

    path("send-email/", send_email_api),

    path("emails/", get_all_emails),

    path("emails/<int:id>/", get_single_email),

    path("emails/delete/<int:id>/", delete_email),
]