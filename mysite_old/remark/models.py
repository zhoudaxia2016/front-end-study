from django.db import models

# Create your models here.
class Remark(models.Model):
    username = models.CharField(max_length=30)
    publish_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.content

class BlogRemark(Remark):
    blog_id = models.IntegerField()

class DemoRemark(Remark):
    demo_id = models.IntegerField()

