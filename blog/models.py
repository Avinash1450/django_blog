from django.db import models
from django.contrib.auth.models import User

class Blogpost(models.Model):
	blog_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	sub_title = models.CharField(max_length=50)
	content = models.TextField(max_length=500)
	date = models.DateTimeField(auto_now_add = True)

	class Meta:
		ordering = ['date']

	def __str__(self):
		return self.title
