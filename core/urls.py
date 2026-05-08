from django.urls import path
from django.http import HttpResponse

from .views import send_email

urlpatterns = [
    path('send/', send_email),
]

def home(request):
    return HttpResponse("Frontend Working 🚀")





