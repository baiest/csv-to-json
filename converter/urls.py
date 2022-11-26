from django.contrib import admin
from django.urls import path
from .views import GetJson

urlpatterns = [
    path('converter/', GetJson.as_view()),
]