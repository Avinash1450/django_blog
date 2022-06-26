from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Blogpost,Preferences
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import user_logged_in
from django.core.paginator import Paginator
from datetime import date,timedelta
from django.contrib.auth import login

# Create your views here.
def home(request):
	page_number = request.GET.get('page')
	if page_number is None:
		page_number = 1
	blogs = Blogpost.objects.all().order_by('-date')
	paginator = Paginator(blogs, 3)
	page_obj = paginator.get_page(page_number)
	if request.user.username:
		liked_blogs = request.user.preferences_set.all()
		liked_blogs = [b.blog for b in liked_blogs]
	else:
		liked_blogs = ''
	context = {
		'page_obj' : page_obj,
		'liked_blogs' : liked_blogs
	}
	print(liked_blogs)
	return render(request, 'blog/home.html',context)

@login_required
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
			try:
				filter_date = date.today() - timedelta(days=3)
				blog = Blogpost.objects.filter(date__gte = filter_date)
				if blog.exists() is False:
					raise ValueError ("no such posts")
			except:
				messages.error(request,'NO POSTS IN LAST FEW DAYS')
				return redirect('bloghome')
		elif search == "last week":
			try:
				exclude_date = date.today() - timedelta(days=7)
				blog = Blogpost.objects.filter(date__gt = exclude_date)
				if blog.exists() is False:
					raise ValueError ("no such posts")
			except:
				messages.error(request,"NO POSTS IN LAST WEEK")
				return redirect('bloghome')
		else:
			try:
				t = date.today()
				last_month_first_day = date(t.year,t.month-1,1)
				last_month_last_day = date(t.year,t.month,1) - timedelta(days=1)
				blog = Blogpost.objects.filter(date__range=(last_month_first_day, last_month_last_day))
				if blog.exists() is False:
					raise ValueError ("no such posts")
			except:
				messages.error(request,"NO POSTS IN LAST MONTH")
				return redirect('bloghome')
		paginator = Paginator(blog, 2)
		page_obj = paginator.get_page(page_number)
	context = {
		'page_obj' : page_obj
	}
	return render(request, 'blog/home.html',context)


def search_box(request):
	page_number = request.GET.get('page')
	if page_number is None:
		page_number = 1
	if request.GET.get('title'):
		word = request.GET.get('title')
		try:
			blog = Blogpost.objects.filter(title__icontains = word).all()
			if blog.exists() is False:
				raise ValueError('no such posts')
			paginator = Paginator(blog,5)
		except:
			messages.error(request,f'NO POSTS EXISTS FOR KEYWORD {word}')
			return redirect('bloghome')	
		page_obj = paginator.get_page(page_number)
		context = { 'page_obj' : page_obj }
		return render(request, 'blog/home.html', context)
	else:
		return redirect('bloghome')


def users_list(request):
	user_list = User.objects.all()
	post_list = [ [t.username, t.blogpost_set.all().count()] for t in user_list ]
	context = { 'post_list' : post_list }
	return render(request, 'blog/user_list.html', context)


def post_with_id(request,postid):
	post = Blogpost.objects.get(blog_id=postid)
	if request.user.username:
		liked_blogs = request.user.preferences_set.all()
		liked_blogs = [b.blog for b in liked_blogs]
	else:
		liked_blogs = ''
	context = {
		'post' : post,
		'liked_blogs' : liked_blogs
	}
	return render(request, 'blog/user_list.html',context)

@login_required(login_url='/user/login/')
def like_post(request,postid):
	blog = Blogpost.objects.get(blog_id=postid)
	p = Preferences(user=request.user,blog=blog,value=1)
	p.save()
	return redirect('bloghome')

@login_required(login_url='/user/login/')
def unlike_post(request,postid):
	user = request.user
	p = Preferences.objects.filter(user=user).get(blog__blog_id=postid)
	p.delete()
	return redirect('bloghome')



