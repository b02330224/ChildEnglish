from django.contrib import admin
from video.models import *

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ('filename', 'e_name', 'store_path', 'num_views', 'description',)
    list_filter = ('filename',)



admin.site.register(Video, VideoAdmin)


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'nums',)
    list_filter = ('name',)


admin.site.register(Episode, EpisodeAdmin)