from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from .models import Profile

@receiver(post_save,sender=Profile)
def alterimage(sender,created,instance,**kwargs):
	if not created:
		img = Image.open(instance.image)
		size = (100,100)
		img = img.resize(size)
		img.save(instance.image.path)
