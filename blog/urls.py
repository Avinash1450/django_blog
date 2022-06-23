from django.urls import path
from . import views

apps = 'blog'
urlpatterns = [
   path('', views.home, name='bloghome'),
   path('search/<str:search>', views.search, name='search'),
   path('searchbox/', views.search_box, name='search_box'),
   path('profile/<str:name>', views.userprofile, name="userprofile"),
   path('profile/', views.profile, name='profile'),
   path('addpost/', views.addpost, name='addpost'),
   path('deletepost/<str:postid>', views.deletepost, name='deletepost'),
   path('updatepost/<int:postid>', views.updatepost, name='updatepost'),
   path('users-list', views.users_list, name="users-list"),
   path('post/<str:postid>', views.post_with_id, name='post')
]


