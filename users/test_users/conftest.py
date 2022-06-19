import pytest
from django.test import Client
from django.contrib.auth.models import User


@pytest.fixture
def test_user():
	user = User.objects.create(username='avinash')
	user.set_password('1450')
	user.save()
	return user
