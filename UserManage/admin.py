from django.contrib import admin
from UserManage.models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password',  'email',)
    list_filter = ('username',)



admin.site.register(User, UserAdmin)
