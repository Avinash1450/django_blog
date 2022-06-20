from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			pass1 = form.cleaned_data.get('password1')
			form.save()
			user = authenticate(username=username, password=pass1)
			login(request,user)
			messages.success(request, f"you are succesfully registered {username.upper()}")
			return redirect("profile")
		else:
			for msg in form.errors:
				messages.error(request,form.errors.get(msg))
	form = RegistrationForm()
	return render(request,'users/registration.html',{ 'form' : form })



def loggedin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user =  authenticate(username=username,password=password)
		if user:
			login(request,user)
			request.session.set_expiry(0)
			return redirect('profile')
		else:
			messages.error(request, f"please enter correct username or password")
	context = { 'title' : 'Login' }
	return render(request,'users/login.html',context)


def loggedout(request):
	logout(request)
	return redirect('bloghome')

@login_required
def updateprofile(request):
	form = ProfileForm(instance=request.user.profile)
	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('profile')
		else:
			messages.error(request,f"please fill data correctly")
	context = {
		'form' : form
	}
	return render(request, 'users/update.html', context)


	