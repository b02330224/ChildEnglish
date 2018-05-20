from django.db import models
from django.utils import timezone
from video.models import Video
import uuid
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    gender = models.CharField(
        max_length=6,
        verbose_name=u"性别",
        choices=GENDER_CHOICES,
        default="female")
    # 地址
    address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, default="")
    nickname = models.CharField(max_length=10, unique=True)
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