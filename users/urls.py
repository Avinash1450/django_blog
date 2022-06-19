from django.urls import path,re_path
from . import views


urlpatterns = [
 	path('login/', views.loggedin, name='login'),
    re_path(r'^\D+/loggedout/', views.loggedout, name='loggedout'),
	path('updateprofile/', views.updateprofile, name='updateprofile'),
	path('register/', views.register, name='register'),
	]
