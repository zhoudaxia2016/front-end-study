from django.db import models

# Create your models here.
class Blog(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=50)
    published_time = models.DateTimeField('Date publish')
    comment_count = models.IntegerField(default=0)
    view_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Msg(models.Model):
    title = models.CharField(max_length=50)
    comment_count = models.IntegerField(default=0)
    view_num = models.IntegerField(default=0)
