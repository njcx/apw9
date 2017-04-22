from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    #desc = models.TextField()
    #wechat = models.CharField(max_length=30, blank=True)
    #qq = models.IntegerField(blank=True, null=True)
    #imgabout = models.ImageField()

    def __unicode__(self):
        return self.username
class Aboutall(models.Model):
    publishtime = models.DateTimeField(auto_now=True)
    content = models.TextField()
class Site(models.Model):
    keywords = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

