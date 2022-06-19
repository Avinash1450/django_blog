import pytest
from django.test import Client
from model_bakery import baker
from blog.models import Blogpost
from django.contrib.auth.models import User
from datetime import datetime

@pytest.fixture(scope="session")
def client():
	return Client()

@pytest.fixture
def test_user():
	user = User.objects.create(username='avinash',password='1450')
	user.set_password('1450')
	user.save()
	return user

@pytest.fixture
def test_blog(test_user):
	user = test_user
	return Blogpost.objects.create(blog_id = 1,user=user,title='first',sub_title='first blog',content='first blog content')


