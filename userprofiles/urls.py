from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth.views import *

urlpatterns = [
    path('register/', register_user, name='register-user'),
    path('reset_password/', reset_password, name='reset-password'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset_password_email/<str:email>/', send_password_reset_email, name='password-reset-email'),
    path('logout/', logout_user, name='logout-user')
]



