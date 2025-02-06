# Django and DRF imports
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Local application imports
from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def get_user(request):
    serializer = UserSerializer({'name': 'John', 'age': 35}) # {'name': 'John', 'age': 25}
    return Response(serializer.data)