from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate

def navigator(request):
	return render(request,'navigate.html')