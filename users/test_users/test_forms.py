import pytest
from users.forms import RegistrationForm,ProfileForm,UpdateProfileForm
from django.http import HttpRequest

@pytest.mark.django_db
def test_registrationform_empty_form():

	form = RegistrationForm()

	assert ("username" in [t for t in form.fields])
	assert ("first_name" in [t for t in form.fields])
	assert ("last_name" in [t for t in form.fields])
	assert ("email" in [t for t in form.fields])
	assert ("password1" in [t for t in form.fields])
	assert ("password2" in [t for t in form.fields])


@pytest.mark.django_db
def test_registrationform_filled_form():

	data = {
	'username' : 'avi',
	'first_name' : 'avinash',
	'last_name' : 'yadav',
	'email' : 'a@y.com',
	'password1' : '1qaz1234',
	'password2' : '1qaz1234'
	}

	request = HttpRequest()
	request.POST = data

	form = RegistrationForm(request.POST)

	assert form.is_valid()


@pytest.mark.django_db
def test_profileform_empty_form():

	form = ProfileForm()

	assert ("age" in [t for t in form.fields])
	assert ("state" in [t for t in form.fields])
	assert ("about" in [t for t in form.fields])
	assert ("image" in [t for t in form.fields])


@pytest.mark.django_db
def test_profileform_filled_form(test_user):
	
	data = {
	'age' : '25',
	'about' : 'nothing',
	'state' : 'bihar',
	'image'  : 'a.jpg'
	}

	request = HttpRequest()
	request.POST = data 

	form = ProfileForm(request.POST)

	assert form.is_valid()


@pytest.mark.django_db
def test_updateprofileform_empty_form():

	form = UpdateProfileForm()

	assert ("first_name" in [t for t in form.fields])
	assert ("username" in [t for t in form.fields])
	assert ("last_name" in [t for t in form.fields])
	assert ("email" in [t for t in form.fields])
	
@pytest.mark.django_db
def test_updateprofileform_filled_form(test_user):

	data = {
	'username' : 'avi',
	'first_name' : 'avinash',
	'last_name' : 'yadav',
	'email' : 'a@y.com'
	}

	request = HttpRequest()
	request.POST = data

	form = UpdateProfileForm(request.POST)

	assert form.is_valid()