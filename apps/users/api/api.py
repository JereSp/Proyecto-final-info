from posixpath import dirname
from django.http import response
from apps.users.models import User,UserManager
from apps.users.api.serializers import UserSerializer,LoginSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from cryptography.fernet import Fernet
from rest_framework.response import Response
from rest_framework import status
import environ
from pathlib import Path
import os 

env = environ.Env()
environ.Env.read_env(env_file='.env')

class UserAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def LoginAPIView(request):
    if request.method == 'POST':
        fernet = Fernet(env.bytes('SECRET_KEY'))
        user = User.objects.get(username = request.data['username'])
        bytes_password = bytes(request.data['password'],encoding='utf-8')
        dec_password = fernet.decrypt(bytes_password).decode()
        if user.password == dec_password:
            return Response('',status=status.HTTP_200_OK)
        else:
            return Response('',status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response('',status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def RegisterAPIView (request):
    if request.method == 'POST':
        data = request.data
        try:
            user = User.objects.get(username=request.data["username"])
            if (user.username == data['username']):
                return Response(f'Usuario {user.username} ya existe en la base de datos...' ,status=status.HTTP_409_CONFLICT)
        except:
            new_user = User(
                username=data['username'],
                email=data['email'],
                name=data['name'],
                last_name=data['last_name'],
                is_staff = False,
                is_superuser = False,
            )
            new_user.set_password(data['password']),#Contraseña desencriptada
            new_user.save(using=UserManager().db)

            return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

