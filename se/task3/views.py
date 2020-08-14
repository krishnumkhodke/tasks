from django.shortcuts import render
from .models import visiters
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def sign_up(request):
	#message = ' '
	if request.method == 'POST':
		username = request.POST.get('username')
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		ph_no = request.POST.get('ph_no')
		email = request.POST.get('email')
		pass1 = request.POST.get('pass1')
		pass2 = request.POST.get('pass2')

		if(pass1==pass2):
			try:
				ch1 =  User.objects.get(username=request.POST.get('username'))
				return render(request,'sign.html',{'messag':"ERROR : username already taken"})
			except:
				user = User.objects.create_user(username=username,password=pass1)
				#up is short for user profile
				up = visiters(user=user,ph_no=ph_no)
				up.save()
				return render(request,'sign.html',{'messag':"User Created"})
		else:
			return render(request,'sign.html',{'messag':"password dont match"})
	else:
	
		return render(request,'sign.html',{'messag':' '})


def login_(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			print(user)
			return render(request,'hope.html',{'message':username})
		else:
			return render(request,'login.html',{'message':'Invalid Credentials'})
	return render(request,'login.html',{'message':' '})

def logout(request):
	auth.logout(request)
	#return render(request,'sign.html',{'messag':'successfuly logged out'})
	return HttpResponseRedirect(reverse('task3-sign_up'))