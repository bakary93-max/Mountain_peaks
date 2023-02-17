from django.contrib import admin
from django.urls import path
from .views import PeakList, PeakDetail

urlpatterns = [
    path('peaks/', PeakList.as_view()),
    path('peaks/<str:name>', PeakDetail.as_view())
]