from django.contrib import admin
from story.models import *

# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'url_path', 'store_path', 'num_views', 'description', 'created_on')
    list_filter = ('name',)



admin.site.register(Story, StoryAdmin)

