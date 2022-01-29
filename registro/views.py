
from rest_framework import permissions


from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes =[permissions.AllowAny]
    serializer_class = RegisterSerializer
