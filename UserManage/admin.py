from django.contrib import admin
from UserManage.models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password',  'email',)
    list_filter = ('username',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'content', 'time')
    list_filter = ('content',)


admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
