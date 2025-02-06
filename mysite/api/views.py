# Django and DRF imports
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Local application imports
from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# {"name": "John", "age": 35}

@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)

    # Check if the data is valid
    if serializer.is_valid():
        # Save the data
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
