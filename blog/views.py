from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Blogpost
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import user_logged_in


# Create your views here.
def homep(request):
	blogs = Blogpost.objects.all().order_by('-date')
	print(blogs.count())
	context = {
		'blogs' : blogs
	}
	return render(request, 'blog/home.html',context)

def profile(request):
	user=request.user 
	posts = user.blogpost_set.all() 
	context = {
		'posts' : posts
	}
	return render(request, 'blog/profilepage.html', context)


def userprofile(request,name):
	user = User.objects.get(username=name)
	posts = user.blogpost_set.all()
	context = {
		'user' : user,
		'posts' : posts
	}
	return render(request, 'blog/userprofile.html', context)


@user_logged_in
def addpost(request):
	form = Postform()
	if request.method == 'POST':
		form = Postform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('profile')
		else:
			messages.warning(request,"Post is not validated")
	context = {
		'title'  : 'Add Post'
	}
	return render(request, 'users/login.html', context)

@login_required
def updatepost(request,postid):
	form = Postform(instance=Blogpost.objects.get(blog_id=postid))
	if request.method == 'POST':
		form = Postform(request.POST, instance=Blogpost.objects.get(blog_id=postid))
		if form.is_valid():
			form.save()
			return redirect('profile')
		else:
			messages.warning(request,"Post is not updated")
	context = {
		'form' : form,
		'title' : 'Update Post',
		'postid' : postid
	}
	return render(request, 'users/login.html',context)


@login_required
def deletepost(request,postid):
	post = Blogpost.objects.get(blog_id=postid)
	post.delete()
	messages.warning(request,f"{post.title} has been deleted")
	return redirect('profile')


#this is the pagination