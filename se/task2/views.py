from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import user_form
from django.views.generic.detail import DetailView
from . import models
from django.urls import reverse
# Create your views here.
def home(request):
	if request.method == 'POST':
		form = user_form(request.POST)
		if form.is_valid():
			u = form.cleaned_data.get('email')
			form.save()
			mail = request.POST.get('email')
			match = models.user_info.objects.get(email=mail)
			return HttpResponseRedirect(reverse('post-view',args=(match.id,)))
	else:
		form = user_form(request.POST)
	return render(request,'info.html',{'form':form})

class info_view(DetailView):
	model = models.user_info
	template_name = 'post_view.html'
	context_object_name = 'post'

def search(request):
	if request.method == 'POST':
		try:
			mail = request.POST.get('email')
			match = models.user_info.objects.get(email=mail)
			#print(match)
			#print(match.id)
			return HttpResponseRedirect(reverse('post-view',args=(match.id,)))
		except:
			return render(request,'not_found.html')
	return render(request,'search.html')