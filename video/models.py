from django.db import models

# Create your models here.

class Episode(models.Model):
    slug= models.CharField(max_length=50, default="")
    name = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)
    nums =  models.IntegerField(default=0)

    def __str__(self):
        return '%s' % self.name


class Video(models.Model):
    filename = models.CharField(max_length=255)
    e_name = models.ForeignKey(Episode, verbose_name='Video', related_name="videos")
    store_path = models.CharField(default='', max_length=255)
    url_path=models.CharField(default='', max_length=255)
    #is_img = models.BooleanField(default=False)
    num_views = models.IntegerField(default=0)
    description = models.TextField(default='', blank=True)
    image_path = models.CharField(max_length=255, default='/static/img/gogo2.png')
    #is_active = models.BooleanField(default=False)

    #created_on = models.DateTimeField(auto_now_add=True)
    #created_by = models.ForeignKey(AUTH_USER_MODEL)

    def __str__(self):
        return '%s' % self.filename

