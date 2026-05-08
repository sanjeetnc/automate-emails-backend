from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Frontend Working 🚀")

urlpatterns = [
    path('', home),
]




