from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import json
from .models import CustomUser




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['name'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = ['/api/token',
              '/api/token/refresh']
    return Response(routes)

@api_view(['POST'])
def signup(request):
    print(request.body)
    print(json.loads(request.body))
    serializer = UserSerializer(data=json.loads(request.body))
    if serializer.is_valid():
        serializer.save()
        print(json.loads(request.body)["username"])
        user = CustomUser.objects.get(username=json.loads(request.body)["username"])
        user.set_password((request.data['password']))
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def login(request):
    user = get_object_or_404(CustomUser, username=request.data['username'])
    print(request.data['password'])
    print(user.id)
    # if not user.check_password(request.data['password']):
    #     return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({"token":token.key, 'user': serializer.data})
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
