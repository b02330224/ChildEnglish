from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from video.models import Video, Episode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from UserManage.models import *
from utils.tools import *
import json
from datetime import datetime
from django.core import serializers
from UserManage.views import login_required


# Create your views here.



def list(request, username=None):
    username = request.session.get('username', None)
    videos= Video.objects.all()
    paginator = Paginator(videos, 5)  # Show 25 contacts per page

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

    video= Video.objects.get(store_path = path+".flv")
    num = video.num_views+1
    video.num_views = num
    video.save()
    videoList = Video.objects.filter(e_name=video.e_name)
    print("video", video)
    username = request.session.get("username", None)
    comment = Comment.objects.filter( video__filename=video.filename)
    print("comment", comment)
    return render(request, "detail.html",{'video': video,"videoList":videoList, "comment":comment, "username":username})

def episode(request, slug):
    episode = Episode.objects.get(slug=slug)
    videos = episode.videos.all()
    print("videos",videos)
    username = request.session.get("username", None)
    return render(request, "list.html", {'videos': videos,  "username": username})

def top5(request):
    username = request.session.get('username', None)
    videos = Video.objects.all().order_by('-num_views')[0:5]
    data_v = serializers.serialize("json", videos)
    return HttpResponse(data_v)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H-%M-%S")
        return json.JSONEncoder.default(self, obj)


json_1 = {'num': 1112, 'date': datetime.now()}

@login_required
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