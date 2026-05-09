from django.urls import path
from .views import home, send_sheet_emails

urlpatterns = [
    path('', home),
    path('send/', send_sheet_emails),
]