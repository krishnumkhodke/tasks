from django.urls import path,include
from . import views

urlpatterns = [
	path('',views.sign_up,name='task3-sign_up'),
	path('/user/login/',views.login_,name='log-in'),
	path('/user/logout/',views.logout,name='log-out'),
]