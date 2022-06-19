import pytest
from django.urls import reverse,resolve
from users.views import *

def test_loggedin():
	url = reverse('login')

	assert resolve(url).func == loggedin

def test_loggedout():
	url = reverse('loggedout')

	assert resolve(url).func == loggedout

def test_register():
	url = reverse('register')

	assert resolve(url).func == register

def test_updateprofile():
	url = reverse('updateprofile')

	assert resolve(url).func == updateprofile
