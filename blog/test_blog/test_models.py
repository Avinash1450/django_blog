import pytest
from blog.models import Blogpost
from datetime import datetime
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_blogpost():
	user = User.objects.create(username='avinash',password='1qaz2wsz')
	blog = Blogpost.objects.create(blog_id = 1,
		user = user,
		title = 'siwan',
		sub_title = 'bihar',
		content = 'about siwan',
		date = datetime.now())

	assert Blogpost.objects.all().count() == 1
	assert blog.user.username == 'avinash'