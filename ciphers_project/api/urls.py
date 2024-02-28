from django.urls import path
from .views import greetings , encode


urlpatterns = [
    path('', greetings),
    path('caeser/<str:plaintext>/<int:shift>', encode),
]
