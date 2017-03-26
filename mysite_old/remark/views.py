from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from .models import *

# Create your views here.
def blogRemark(rq):
    if rq.method == 'POST':
        [isvalid,username,blog_id,content] = validate(rq,'blog_id')
        if isvalid:
            blog_remark = BlogRemark(username=username,blog_id=blog_id,content=content)
            blog_remark.save()
            return redirect(reverse('blog:detail', args=(blog_id,)))
        else:
            return HttpResponse(status=403)
    else:
        return HttpResponse(status=403)
    
def demoRemark(rq):
    if rq.method == 'POST':
        [isvalid,username,demo_id,content] = validate(rq,'demo_id')
        if isvalid:
            demo_remark = DemoRemark(username=username,demo_id=demo_id,content=content)
            demo_remark.save()
            return redirect(reverse('blog:detail', args=(demo_id,)))
        else:
            return HttpResponse(status=403)
    else:
        return HttpResponse(status=403)

def validate(rq,t):
    username = rq.session.get('username',False)
    post_id = rq.session.get(t,False)
    content = rq.POST.get('content',False)
    if username and post_id and content:
        if len(content) <= 140:
            return [True,username,post_id,content]
        else:
            return [False,None,None,None]
    else:
        return [False,None,None,None]
