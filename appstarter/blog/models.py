from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default = datetime.now)
    postText = models.TextField(default=None, blank=True, null=True)

class Comment(models.Model):
    blog_id =  models.ForeignKey(
        Blog,
        on_delete=models.CASCADE
    )
    visitor_name = models.CharField(max_length=200, default=None, blank=True, null=True)
    commentText = models.TextField(default=None, blank=True, null=True)
