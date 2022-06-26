from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Blogpost,Preferences

@receiver(post_save,sender=Preferences)
def onlike_counter(created,instance,sender,**kwargs):
	blog = Blogpost.objects.get(blog_id=instance.blog.blog_id)
	blog.likes = blog.preferences_set.all().count()
	blog.save()


@receiver(post_delete,sender=Preferences)
def ondelete_counter(instance,sender,**kwargs):
	blog = Blogpost.objects.get(blog_id=instance.blog.blog_id)
	blog.likes = blog.preferences_set.all().count()
	blog.save()

