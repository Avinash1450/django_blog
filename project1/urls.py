"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from blog import views as blog_views
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', users_views.loggedin, name='login'),
    re_path(r'^\D+/loggedout/',users_views.loggedout, name='loggedout'),
    path('updateprofile/', users_views.updateprofile, name='updateprofile'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('profile/<str:name>', blog_views.userprofile, name="userprofile"),
    path('profile/', blog_views.profile, name='profile'),
    path('register/', users_views.register, name='register'),
    path('addpost/', blog_views.addpost, name='addpost'),
    path('deletepost/<str:postid>', blog_views.deletepost, name='deletepost'),
    path('updatepost/<int:postid>', blog_views.updatepost, name='updatepost')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)