import pytest
from django.urls import reverse
from blog.views import home,profile,userprofile,addpost,deletepost,updatepost,search,search_box
from model_bakery import baker
from blog.models import Blogpost
from django.contrib.auth.models import User
from datetime import datetime,date,timedelta
from django.contrib.auth import login
import json

@pytest.mark.django_db
def test_home_GET(client):
	url = reverse('bloghome')
	response = client.get(url)
	assert response.status_code == 200
	assert ('blog/home.html' in [t.name for t in response.templates])

@pytest.mark.django_db
def test_profile(client,test_user):
	user = test_user
	Blogpost.objects.bulk_create([
		Blogpost(blog_id = 1,user=user,title='first',sub_title='first blog',content='first blog content',date=datetime.now()),
		Blogpost(blog_id = 2,user=user,title='second',sub_title='second blog',content='second blog content',date=datetime.now())
		])
	url = reverse('profile')
	client.login(username=user.username,password='1450')
	response = client.get(url)
	assert response.status_code == 200
	assert user.blogpost_set.all().count() == 2


@pytest.mark.django_db
def test_userprofile(client,test_user):
	url = reverse('userprofile',args=['avinash'])
	response = client.get(url)

	assert response.status_code == 200
	assert ('blog/userprofile.html' in [t.name for t in response.templates])


@pytest.mark.django_db
def test_addpost_GET_when_not_login(client):
	url = reverse('addpost')
	response = client.get(url)

	assert response.status_code == 302


@pytest.mark.django_db
def test_addpost_GET_when_user_loggedin(client,test_user):
	url = reverse('addpost')
	client.login(username='avinash',password='1450')
	response = client.get(url)

	assert response.status_code == 200
	assert ('users/login.html' in [t.name for t in response.templates])

@pytest.mark.django_db
def test_addpost_POST_right_data(client,test_user):
	payload = {
			"blog_id" : 1,
			"user" : 1,
			"title" : "first",
			"sub_title" : "first blog",
			"content" : "first blog content"
	}
	url = reverse('addpost')
	client.login(username='avinash',password='1450')
	response = client.post(url,payload)
	
	assert response.status_code == 302
	assert response.url == '/blog/profile/'
	assert Blogpost.objects.all().count() == 1


@pytest.mark.django_db
def test_addpost_POST_wrong_data(client,test_user):
	payload = {
			"user" : "avinash",
			"title" : "first",
	}
	url = reverse('addpost')
	client.login(username='avinash',password='1450')
	response = client.post(url,payload)

	assert response.status_code == 200
	assert ('users/login.html' in [t.name for t in response.templates])


@pytest.mark.django_db
def test_updatepost_GET(client,test_user,test_blog):
	url = reverse('updatepost', args=[1])
	client.login(username='avinash',password='1450')
	response = client.get(url)

	assert response.status_code == 200
	assert ('users/login.html' in [t.name for t in response.templates])


@pytest.mark.django_db
def test_updatepost_POST_right_data(client,test_user,test_blog):
	url = reverse('updatepost',args=[1])
	client.login(username='avinash',password='1450')
	payload = {
		"blog_id" : 1,
		"user" : 1,
		"title" : "third",
		"sub_title" : "third post",
		"content"  : "third blogpost"
	}
	response = client.post(url,payload)

	assert response.status_code == 302
	assert response.url == '/blog/profile/'
	assert Blogpost.objects.first().title == 'third'


@pytest.mark.django_db
def test_updatepost_POST_wrong_data(client,test_user,test_blog):
	url = reverse('updatepost', args=[1])
	client.login(username='avinash',password='1450')
	payload = {}
	response = client.post(url,payload)

	assert response.status_code == 200


@pytest.mark.django_db
def test_delete(client,test_user,test_blog):
	user = User.objects.create(username='shivam',password='1450')
	user.set_password('1450')
	user.save()
	client.login(username='shivam',password='1450')
	Blogpost.objects.create(blog_id=2,user=user,title='k',sub_title='ker',content='kerala')
	url = reverse('deletepost', args=[1])
	response = client.get(url)

	assert response.status_code == 302
	assert Blogpost.objects.all().count() == 1
	assert response.url == '/blog/profile/'


@pytest.mark.django_db
def test_search_for_most_recent_available(client,test_user,test_blog):
	url = reverse('search', args=['most recent'])
	response = client.get(url)

	assert response.status_code == 200
	assert ('blog/home.html' in [t.name for t in response.templates])


@pytest.mark.django_db
def test_search_for_most_recent_not_available(client):
	url = reverse('search', args=['most recent'])
	response = client.get(url)

	assert response.status_code == 302
	assert response.url == '/blog/'

@pytest.mark.django_db
def test_search_for_last_week_available(client,test_user):
	client.login(username='avinash',password='1450')
	Blogpost.objects.create(blog_id=1,user=test_user,title='week',sub_title='last week',content='last week filteration',date=date.today()-timedelta(days=3)) #blogpost with date three dqays earlier
	url = reverse('search',args=['last week'])
	response = client.get(url)

	assert response.status_code == 200

@pytest.mark.django_db
def test_search_for_last_week_not_available(client):
	url = reverse('search',args=['last week'])
	response = client.get(url)

	assert response.status_code == 302
	assert response.url == '/blog/'


@pytest.mark.django_db
def test_search_box_no_keyword(client):
	url = reverse('search_box')
	response = client.get(url)

	assert response.status_code == 302
	assert response.url == '/blog/'

@pytest.mark.django_db
def test_search_box_with_right_keyword(client,test_blog):
	url = reverse('search_box')
	response = client.get(url, { 'title' : 'first'})

	assert response.status_code == 200
	assert ('blog/home.html' in [t.name for t in response.templates])


@pytest.mark.django_db
def test_search_box_with_wrong_keyword(client,test_blog):
	url = reverse('search_box')
	response = client.get(url, { 'title' : 'last'})

	assert response.status_code == 302
	assert response.url == '/blog/'

	


































































