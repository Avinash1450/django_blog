from django.urls import path
from . import views

apps = 'blog'
urlpatterns = [
   path('?page=1', views.homep, name='bloghome')
]


