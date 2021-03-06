"""BabyEnglish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from video import  urls, views
from UserManage import views as UserViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^video/', include('video.urls')),
    url(r'^story/', include('story.urls')),
    url(r'^users/', include('UserManage.urls',namespace="users")),
    url(r'^login/',UserViews.login),
    url(r'^logout/',UserViews.logout, name='logout'),
    url(r'^register/',UserViews.register, name='register'),
    url(r'^index/$', views.list, name='index'),
    url(r'^$', views.list),
    url(r'^index/(?P<username>\w+)/$',views.list, name='index_user'),
    url(r'^pl/$', views.pl),
]
