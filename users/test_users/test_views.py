import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from users.forms import *

@pytest.mark.django_db
def test_register_GET(client):
	url = reverse('register')
	response = client.get(url)

	assert response.status_code == 200
	assert ('users/registration.html' in [t.name for t in response.templates])


@pytest.mark.django_db
def test_register_POST_right_data(client):
	payload = {
		'username' : 'avi',
		'email' : 'avinash@yadav.com',
		'password1' : '1qaz2wsz',
		'password2' : '1qaz2wsz'
	}
	url = reverse('register')
	response = client.post(url,payload)

	assert response.status_code == 302
	assert response.url == '/blog/profile/'


@pytest.mark.django_db
def test_register_POST_wrong_data(client):
	url = reverse('register')
	response = client.post(url,{})

	assert response.status_code == 200
	assert ('users/registration.html' in [t.name for t in response.templates])


@pytest.mark.django_db
def test_loggedin_GET(client):
	url = reverse('login')
	response = client.get(url)

	assert response.status_code == 200
	assert response.context['user'],AnonymousUser
	assert ('users/login.html' in [t.name for t in response.templates])


@pytest.mark.django_db
def test_loggedin_POST_right_credentials(client,test_user):
	credentials = {
		'username' : 'avinash',
		'password' : '1450'
	}
	url = reverse('login')
	response = client.post(url,credentials)

	assert response.status_code == 302
	assert response.url == '/blog/profile/'



@pytest.mark.django_db
def test_loggedin_POST_wrong_credentials(client,test_user):
	credentials = {
		'username' : 'abc',
		'password2' : '1234'
	}
	url = reverse('login')
	response = client.post(url,credentials)

	assert response.status_code == 200
	assert response.context['title'] == 'Login'


@pytest.mark.django_db
def test_loggedout(client,test_user):
	url = reverse('loggedout')

	response = client.get(url)

	assert response.status_code == 302
	assert response.url == '/blog/'


@pytest.mark.django_db
def test_updateprofile_GET_user_not_loggedin(client):
	url = reverse('updateprofile')
	response = client.get(url)

	assert response.status_code == 302
	assert response.url == '/login/?next=/user/updateprofile/'


@pytest.mark.django_db
def test_updateprofile_GET_user_loggedin(client,test_user):
	url = reverse('updateprofile')
	client.login(username='avinash',password='1450')
	response = client.get(url)

	assert response.status_code == 200
	assert ('users/update.html' in [t.name for t in response.templates])


@pytest.mark.django_db
def test_updateprofile_POST_right_credentials(client,test_user):
	credentials = {
		"first_name" : "abc",
		"last_name" : "def",
		"age" : 22,
		"about" : "anything",
		"state" : "Bihar",
		"image" : "1.jpg"
	}
	client.login(username='avinash',password='1450')
	url = reverse('updateprofile')
	response = client.post(url,credentials)

	assert response.status_code == 302
	assert response.url == '/blog/profile/'


@pytest.mark.django_db
def test_updateprofile_POST_wrong_credentials(client,test_user):
	url = reverse('updateprofile')
	client.login(username='avinash',password='1450')
	response = client.post(url,{})

	assert response.status_code == 200
	assert ('users/update.html' in [t.name for t in response.templates])










