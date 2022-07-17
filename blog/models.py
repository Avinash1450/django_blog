from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Blogpost(models.Model):
	blog_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	sub_title = models.CharField(max_length=50)
	content = models.TextField(max_length=500)
	post_image = models.ImageField(upload_to='post_pics/', default='profile_pics/default.jpeg',max_length=500)
	likes = models.IntegerField(default=0)
	date = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['blog_id']


	def __str__(self):
		return self.title

	def save(self):
			print("called")
			super().save()
			
			basewidth = 700
			img = Image.open(self.post_image.path)
			wpercent = (basewidth/float(img.size[0]))
			hsize = int((float(img.size[1])*float(wpercent)))
			img = img.resize((basewidth,hsize), Image.ANTIALIAS)
			img.save(self.post_image.path)

	



class Preferences(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	blog = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
	value = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.user} {self.blog} {self.value}"

	class Meta:
		unique_together = ['user','blog','value']


	

