from django.urls import path
from .views import send_sheet_emails

from .views import (
    home,
    send_email_api,
    get_all_emails,
    get_single_email,
    delete_email
)

urlpatterns = [

    path('', home),

    path('send/', send_email_api),
    
    path('send-sheet/', send_sheet_emails),

    path('emails/', get_all_emails),

    path('emails/<int:id>/', get_single_email),

    path('delete/<int:id>/', delete_email),
]