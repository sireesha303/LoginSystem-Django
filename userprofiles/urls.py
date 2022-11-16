from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user, name="register-user"),
]
