from django.urls import path

from .views import questions

urlpatterns = [
    path("v1/questions/", questions, name="questions"),
]
