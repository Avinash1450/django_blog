import pytest
from django.urls import reverse,resolve
from blog.views import *

def test_bloghome():
	url = reverse('bloghome')
	assert resolve(url).func == home

def test_search():
	url = reverse('search', args="l")
	assert resolve(url).func == search

def test_search_box():
	url = reverse('search_box')
	assert resolve(url).func == search_box

def test_userprofile():
	url = reverse('userprofile', args='u')
	assert resolve(url).func == userprofile 

def test_profile():
	url = reverse('profile')
	assert resolve(url).func == profile 

def test_addpost():
	url = reverse('addpost')
	assert resolve(url).func == addpost 

def test_deletepost():
	url = reverse('deletepost', args='d')
	assert resolve(url).func == deletepost  

def test_updatepost():
	url = reverse('updatepost', args='1')
	assert resolve(url).func == updatepost

