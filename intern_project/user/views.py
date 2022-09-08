from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


@api_view(['POST'])
def register_user(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    User.objects.create()
