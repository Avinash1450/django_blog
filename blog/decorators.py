from django.contrib import messages
from django.shortcuts import redirect

def user_logged_in(func):
	def wrap(request, *args, **kwargs):
		if request.user.username:
			return func(request, *args, **kwargs)
		else:
			messages.warning(request,"please log in to add a post")
			return redirect('login')
	return wrap