from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50,default="first name")
	last_name = models.CharField(max_length=50, default="last name")
	age = models.IntegerField(default=0)
	about = models.CharField(max_length=50, default="about me")
	state = models.CharField(max_length=20,default="state")
	image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics',max_length=500)

	def __str__(self):
		return f"{self.user} Profile"

	@receiver(post_save, sender=User)
	def create_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_profile(sender, instance, created, **kwargs):
		instance.profile.save()







