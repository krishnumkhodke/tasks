from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='task2-home'),
    path('/search/',views.search,name='search'),
    path('/<int:pk>/view/',views.info_view.as_view(),name='post-view')
]
