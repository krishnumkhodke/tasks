from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	context = {}
	if request.method == 'POST':
		a = request.POST['number1']
		b = request.POST['number2']
		if(a==''or b==''):
			context = {'message':'enter numbers'}
			return render(request,'home.html',context)
		a = int(a)
		b = int(b)
		l = []
		for i in range(a,b+1):
			l.append(i)

		if(a>b):
			context = {'message':'invalid range of numbers'}
		else:
			context = {'nums':l}


	return render(request,'home.html',context)
