from django.contrib import admin
from django.urls import path

from core.views import (
    home,
    send_sheet_emails
)



urlpatterns = [
    path('', home),
    path('send/', send_sheet_emails),
    path('admin/', admin.site.urls),
]