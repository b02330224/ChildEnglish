from django.db import models
from django.utils import timezone
from video.models import Video
import uuid
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    sex = models.BooleanField()
    city = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50, unique=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.username


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='user')
    video =models.ForeignKey(Video)
    content = models.CharField(max_length=100)
    time = models.DateTimeField('发表时间', default=timezone.now)