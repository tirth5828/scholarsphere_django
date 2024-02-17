"""
URL configuration for scholarsphere_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from scholarsphere_web import views as web_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', web_views.test, name='test'),
    path('home/<str:username>/', web_views.home, name='home'),
    path('profile/<str:username>/', web_views.profile, name='profile'),
    path('calender/<str:username>/', web_views.calender, name='calender'),
    path('subjects/<str:username>/', web_views.subjects, name='subjects'),
    path('deaf/<str:username>/', web_views.deaf, name='deaf'),
    path('feed/<str:username>/', web_views.feed, name='feed'),
]
