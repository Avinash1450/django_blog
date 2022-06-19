import pytest
from blog.forms import Postform
from django.http import HttpRequest


@pytest.mark.django_db
def test_blogpost_empty_form():
	form = Postform()

	assert ("title" in [t for t in form.fields])
	assert ("sub_title" in [t for t in form.fields])
	assert ("content" in [t for t in form.fields])
	assert ("user" in [t for t in form.fields])
	assert ("blog_id" not in [t for t in form.fields])


@pytest.mark.django_db(True)
def test_postform_filled_form(test_user):

	data = {
		'title' : 'first',
		'sub_title' : 'first',
		'content' : 'first post',
		'user' : test_user.pk
	}

	request = HttpRequest()
	request.POST = data

	form = Postform(request.POST,instance=test_user)

	assert form.is_valid()




