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
from django.conf.urls import url
from UserManage.views import UpdatePwdView,UserInfoView
from UserManage import views


urlpatterns = [

    #url(r'update/$', views.update),
    url('updatepwd/', UpdatePwdView.as_view(), name="updatepwd"),
    url('userinfo/', UserInfoView.as_view(), name="userinfo"),
    # 专用于发送验证码的
    #url('sendemail_code/', SendEmailCodeView.as_view(),  name="sendemail_code"),

]
