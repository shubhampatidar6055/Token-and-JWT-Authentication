from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Token Authentication
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


    # JWT Authentication
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]