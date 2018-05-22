from django.shortcuts import  render,redirect,render_to_response,HttpResponse
# 基于类实现需要继承的view
from django.views.generic.base import View
from UserManage.forms import UpdatePwdForm
from UserManage.models import User
from utils.tools import *
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from UserManage.forms import UserInfoForm
# Create your views here.


def login_required(func):
    """要求登录的装饰器"""
    def _deco(request, *args, **kwargs):
        if not request.session.get('username'):
            return HttpResponse(json.dumps({"error":"没有登录"}))
        return func(request, *args, **kwargs)
    return _deco

def login(request):
    """登录界面"""
    # if request.session.get('username'):
    #     return redirect('/')
    if request.method == 'GET':
        return render_to_response('login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user:
            user = user[0]
            if md5_crypt(password) == user.password:
                request.session['username'] = username
                if user.is_admin:
                    request.session['admin'] = 1
                elif user.is_superuser:
                    request.session['admin'] = 2
                else:
                    request.session['admin'] = 0
                return redirect('/index/%s/' % username)
            else:
                error = '密码错误，请重新输入。'
        else:
            error = '用户不存在。'
    return render_to_response('login.html', {'error': error})



def logout(request):
    """注销登录调用"""
    if request.session.get('username'):
        del request.session['username']
        del request.session['admin']
    return redirect('/index/')

def register(request):
    if request.method == "POST":
        print("-------------------register handle--------")
        username =  request.POST.get("username")
        passwd =  request.POST.get("password")
        email = request.POST.get("email")
        nickname = request.POST.get("nickname")
        gender = request.POST.get("sex")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")

        city = request.POST.get("city")
        error_info = dict()

        if User.objects.filter(username= username):
            error_info['error'] = "用户名已经注册了"
        elif   User.objects.filter(nickname=nickname):
            error_info['error'] = "昵称已被使用"
        elif User.objects.filter(email=email):
            error_info['error'] = "邮箱已被注册"
        else:
            User.objects.create(username=username, password=md5_crypt(passwd), nickname=nickname, email=email, gender=gender, city=city)
            return  redirect("/login/")

        return render_to_response("register.html", error_info )
    else:
        return render_to_response("register.html")



class UpdatePwdView(View):

    def get(self, request):
       return render(   request, "password_reset.html")

    def post(self, request):
        modiypwd_form = UpdatePwdForm(request.POST)
        if modiypwd_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            #active_code = request.POST.get("active_code", "")
            #print("active_code=%s" % active_code)
            email = request.POST.get("email", "")
            # 如果两次密码不相等，返回错误信息
            if pwd1 != pwd2:
                return render(
                    request, "password_reset.html", { "msg": "密码不一致"})

            user = User.objects.get(username=request.session['username'])
            # 加密成密文
            user.password = md5_crypt(pwd2)
            # save保存到数据库
            user.save()
            return redirect("/login/")
        # 验证失败说明密码位数不够。
        else:

            return render(
                request, "password_reset.html", {  "modiypwd_form": modiypwd_form})



class UserInfoView(View):


    def get(self, request):
        user = User.objects.get(username=request.session['username'])
        return render(request, "user_info.html", {'user':user  })

    def post(self, request):
        # 不像用户咨询是一个新的。需要指明instance。不然无法修改，而是新增用户
        user = User.objects.get(username=request.session['username'])
        user_info_form = UserInfoForm(request.POST, instance=user)

        if user_info_form.is_valid():
            user_info_form.save()
            return render_to_response("user_info.html",  {'user':user,'status':"修改成功"})
        else:
            render_to_response("user_info.html", {'user': user, 'status':user_info_form.errors})
