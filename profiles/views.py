from os import path
from django import views
from django.shortcuts import render

urlpatterns=[
    path('upload/',views.image_upload_view)
]
