from django.db import models
from login.models import User
from blog.models import Blog

# Create your models here.
class Comment(models.Model):
    content = models.TextField();
    published_time = models.DateTimeField()
    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)

    def __str__(self):
        return self.user.username + '的评论'
