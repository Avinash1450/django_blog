from django.urls import path
from . import views

apps = 'blog'
urlpatterns = [
   path('', views.homep, name='bloghome'),
   path('search/<str:search>', views.search, name='search')
]


