from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Blogpost
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import user_logged_in
from django.core.paginator import Paginator
from datetime import date,timedelta


# Create your views here.
def homep(request):


	page_number = request.GET.get('page')
	if page_number is None:
		page_number = 1

	if request.method == "POST":
		title = request.POST.get("title")
		blogs = Blogpost.objects.filter(title__icontains=title).all()

	else:
		blogs = Blogpost.objects.all().order_by('-date')
	
	paginator = Paginator(blogs, 3)
	page_obj = paginator.get_page(page_number)
	context = {
		'page_obj' : page_obj
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


def search(request,search):
	page_number = request.GET.get('page')
	if page_number is None:
		page_number = 1
	
	if search == "most recent":
		filter_date = date.today() - timedelta(days=7) 
		blog = Blogpost.objects.filter(date__gte = filter_date)
		print(blog)
	elif search == "last week":
		exclude_date = date.today() - timedelta(days=7)
		blog = Blogpost.objects.filter(date__gte = exclude_date)
		print(blog)
	else:
		t = date.today()
		last_month_first_day = date(t.year,t.month-1,1)
		last_month_last_day = date(t.year,t.month,1) - timedelta(days=1)
		blog = Blogpost.objects.filter(date__gte = last_month_last_day).exclude(date__gte = last_month_last_day)
		print(blog)
	paginator = Paginator(blog, 2)
	page_obj = paginator.get_page(page_number)
	context = {
		'page_obj' : page_obj
	}
	return render(request, 'blog/home.html',context)
