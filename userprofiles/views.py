from .serializers import UserRegisterSerializer,PasswordResetSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings


@api_view(['GET'])
def send_password_reset_email(request, email):
    try:
        user = User.objects.get(email=email)
        # print(user.username)
        subject = 'LoginSystem - Reset Forgotten Password'
        message = 'Hello '+user.username+'\n\nPlease click below to reset your password for LoginSystem\n\nhttps://auth.geeksforgeeks.org/resetPassword.php?c=bh9n7quy&e=msireeshar141504%40gmail.com.\n\nIf you did not ask to reset your password, please ignore this message.\n\nThank you,\nLogin System.'


        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [user.email],
        #     fail_silently=False,
        # )
        content = {'success': 'Email sent'}
        return Response(content, status=status.HTTP_200_OK)

    except:
        content = {'NotFound': 'user not found with the given email'}
        # content = dict(notfound='user not found with the given email')
        return Response(content, status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def reset_password(request):
    user = request.user
    print(user)
    print(request.data)
    serializer = PasswordResetSerializer(instance=user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response({'message:"Password updated successfully..'})

