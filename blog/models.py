from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class BlogsPost(models.Model):

    title = models.CharField(max_length=150)    # 博客标题
    # body = models.TextField()                   # 博客正文
    body = RichTextUploadingField()                      # 博客正文
    timestamp = models.DateTimeField()          # 创建时间

