from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from video.models import Video, Episode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from UserManage.models import *
import hashlib
import json
from datetime import datetime


# Create your views here.

def login_required(func):
    """要求登录的装饰器"""
    def _deco(request, *args, **kwargs):
        if not request.session.get('username'):
            return redirect('/login/')
        return func(request, *args, **kwargs)
    return _deco

@login_required
def list(request, username=None):
    videos= Video.objects.all()
    paginator = Paginator(videos, 3)  # Show 25 contacts per page

    page_num = request.GET.get('page')
    try:
        items = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)

    print("videos", videos)

    print("items", items)
    print(items.start_index(),'---',items.end_index())
    start = items.start_index()-1
    end = items.end_index()-1
    return render(request, "index.html",{'videos': videos[start:end+1], 'items':items, "username":username})

def detail(request, path):

    video= Video.objects.get(store_path = path+".mp4")
    num = video.num_views+1
    video.num_views = num
    video.save()
    videoList = Video.objects.filter(e_name=video.e_name)
    print("video", video)
    username = request.session.get("username")
    comment = Comment.objects.filter( video__filename=video.filename)
    print("comment", comment)
    return render(request, "detail.html",{'video': video,"videoList":videoList, "comment":comment, "username":username})


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
            #if md5_crypt(password) == user.password:
            if password == user.password:
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



def md5_crypt(string):
    return hashlib.new("md5", string).hexdigest()

def logout(request):
    """注销登录调用"""
    if request.session.get('username'):
        del request.session['username']
        del request.session['admin']
    return redirect('/login/')

def register(request):
    if request.method == "POST":
        print("-------------------register handle--------")
        username =  request.POST.get("username")
        passwd =  request.POST.get("password")
        email = request.POST.get("email")
        nickname = request.POST.get("nickname")
        sex = request.POST.get("sex")
        if sex == "false":
            sex ="False"
        elif sex =="true":
            sex = "True"
        city = request.POST.get("city")
        error_info = dict()

        if User.objects.filter(username= username):
            error_info['error'] = "用户名已经注册了"
        elif   User.objects.filter(nickname=nickname):
            error_info['error'] = "昵称已被使用"
        elif User.objects.filter(email=email):
            error_info['error'] = "邮箱已被注册"
        else:
            User.objects.create(username=username, password=passwd, nickname=nickname, email=email, sex=sex, city=city)
            return  redirect("/login/")

        return render_to_response("register.html",  error_info)
    else:
        return render_to_response("register.html")


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H-%M-%S")
        return json.JSONEncoder.default(self, obj)


json_1 = {'num': 1112, 'date': datetime.now()}

def pl(request):
    comment = request.POST.get('comment')
    username = request.session.get("username", None)
    video_id = request.POST.get('video_id')
    print(" video_id", video_id)
    user = User.objects.get(username=username)
    video = Video.objects.get(id=video_id)
    obj = Comment.objects.create(content=comment,user=user, video=video)
    print(type(obj.time))
    result={"status":"ok","nickname":user.nickname,"content":comment,"time":obj.time}
    return HttpResponse(json.dumps(result, cls=DateEncoder))