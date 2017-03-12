from django.shortcuts import render
from .models import *
from login.models import User
from blog.models import Blog
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def comment(rq):
    if rq.session.get('is_login',False):
        user_id = rq.session.get('user_id') 
        user = User.objects.get(pk=user_id)
        now =  datetime.datetime.now()
        blog_id = rq.POST['blogId']
        blog = Blog.objects.get(pk=blog_id)
        content = rq.POST['comment']
        comment = Comment(blog=blog,user=user,published_time=now,content=content)
        comment.save()
        return HttpResponseRedirect(reverse('blog:blog',args=[blog_id]))
    else:
        return HttpResponse('You need to sign in to comment the blogs')
