from django.forms import ModelForm
from task2.models import user_info

class user_form(ModelForm):
	class Meta:
		model = user_info
		fields = ['name','email','phone_number','gender']

