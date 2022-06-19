import pytest
from users.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_model_after_user_creation(test_user):

	assert User.objects.all().count() == 1
	assert Profile.objects.all().count() == 1
	assert Profile.objects.all().exists() == True
	assert Profile.objects.first().user == test_user