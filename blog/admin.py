from django.contrib import admin
from .models import Blogpost,Preferences
# Register your models here.

admin.site.register(Blogpost)
admin.site.register(Preferences)