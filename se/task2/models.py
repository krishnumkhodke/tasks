from django.db import models

class user_info(models.Model):
	gender_choices = [
		('M','male'),
		('F','female'),
		('O','other'),
	]
	name = models.CharField(max_length=254)
	email = models.EmailField(unique=True)
	phone_number = models.CharField(max_length=12)
	gender = models.CharField(choices=gender_choices,max_length=254)

	def __str__(self):
		return self.name
