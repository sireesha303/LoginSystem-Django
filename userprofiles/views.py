from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

