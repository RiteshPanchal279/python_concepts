from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
   path('registration/',views.registration ,name='register'),
   path('insertuser/', views.insertuser, name='insertuser'),
]