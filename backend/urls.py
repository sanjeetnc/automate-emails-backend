from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from core.views import send_email

def home(request):
    return HttpResponse("""
    <h1>Frontend Working 🚀</h1>

    <button onclick="sendMail()">
        Send Email
    </button>

    <script>

    async function sendMail() {

        const response = await fetch('/send/');

        const data = await response.json();

        alert(data.message);
    }

    </script>
    """)

urlpatterns = [
    path('', home),
    path('send/', send_email),
    path('admin/', admin.site.urls),
]