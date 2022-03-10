
from rest_framework import permissions

from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User
from .serializers import RegisterSerializer, RegisterSerializerNew
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes =[permissions.AllowAny]
    serializer_class = RegisterSerializer

class RegisterViewNew(generics.CreateAPIView):
   queryset = User.objects.all()
   permission_classes = (AllowAny,)
   serializer_class = RegisterSerializerNew

