from django.db import models

# Create your models here.
class Event(models.Model):
    publish_time = models.DateTimeField(auto_now_add=False)
    url = models.CharField(max_length=30,null=True,blank=True)
    description = models.TextField(blank=False)
    ismajor = models.BooleanField()


    def __str__(self):
        return self.description[0:10]
