from django import forms
from django.contrib.auth.models import User
from .models import Blogpost


class Postform(forms.ModelForm):

	class Meta:
		model = Blogpost
		fields = ['blog_id','title','sub_title','content','post_image','user']


		
			



		