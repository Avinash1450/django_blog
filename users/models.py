from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.CharField(max_length=2,default="age")
	about = models.CharField(max_length=50, default="about me")
	state = models.CharField(max_length=20,default="state")
	image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f"{self.user} Profile"

	@receiver(post_save, sender=User)
	def create_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def Save_profile(sender, instance, created, **kwargs):
		instance.profile.save()

	def imgprocess(self):
		img = Image.open(self.image)
		img = img.resize(50,50)
		img.save()



