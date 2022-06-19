from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from users.models import Profile

class RegistrationForm(UserCreationForm):
	email = forms.CharField(max_length=30 )
	class Meta:
		model=User
		fields = ['username','first_name','last_name','email','password1','password2']

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['age','about','state','image']


class UpdateProfileForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']




