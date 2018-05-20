from django.db import models

# Create your models here.


class Story(models.Model):
    name = models.CharField(max_length=255)
    store_path = models.CharField(default='', max_length=255)
    url_path=models.CharField(default='', max_length=255)
    num_views = models.IntegerField(default=0)
    description = models.TextField(default='', blank=True)
    image = models.CharField(max_length=255, default='')
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s' % self.name
