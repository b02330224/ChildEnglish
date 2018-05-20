from django.shortcuts import render
from django.http import HttpResponse
from story.models import Story
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers

# Create your views here.

def detail(request, s_id):
    username = request.session['username']
    story = Story.objects.get(id=s_id)
    story.num_views= story.num_views+1
    story.save()
    return render(request, "story_detail.html", {'story': story, 'username':username})

def top5(request):
    username = request.session['username']
    story = Story.objects.all().order_by('-num_views')[0:5]
    data_s = serializers.serialize("json", story)
    return HttpResponse(data_s)

def list(request):
    username = request.session['username']
    storys= Story.objects.all()
    paginator = Paginator(storys, 10)  # Show 25 contacts per page

    page_num = request.GET.get('page')
    try:
        items = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)

    print("storys", storys)

    print("items", items)
    print(items.start_index(),'---',items.end_index())
    start = items.start_index()-1
    end = items.end_index()-1
    return render(request, "story_list.html",{'storys': storys[start:end+1], 'items':items, 'username':username})