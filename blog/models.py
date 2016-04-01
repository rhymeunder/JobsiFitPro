from __future__ import unicode_literals

from django.db import models
#makes table in database
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
# Create your models here.

    def __unicode__(self):
        return self.title
