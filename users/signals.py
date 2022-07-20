from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from .models import Profile

@receiver(post_save,sender=Profile)
def alterimage(sender,created,instance,**kwargs):
	if created:
		basewidth = 200
		img = Image.open(instance.image.path)
		wpercent = (basewidth/float(img.size[0]))
		hsize = int(float(img.size[1])*float(wpercent))
		img = img.resize((basewidth,hsize),Image.ANTIALIAS)
		img.save(instance.image.path)
