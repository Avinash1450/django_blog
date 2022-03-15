from django.urls import path
from . import views

apps = 'blog'
urlpatterns = [
   path('', views.homep, name='bloghome')
]


