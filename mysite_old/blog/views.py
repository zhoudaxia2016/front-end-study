from django.shortcuts import render
from .models import *
from markdown2 import markdown
from django.http import HttpResponse
from remark.models import *

# Create your views here.
def validate(rq):
    username = rq.session.get('username',False)
    islogin = False
    if username:
        islogin = True
    return islogin,username

def index(rq):
    posts = []
    posts.extend(Demo.objects.all())
    posts.extend(Blog.objects.all())
    posts = sorted(posts,key=lambda post: post.publish_time)

    islogin,username = validate(rq)

    rp = render(rq,'index.html',{'posts': posts,'islogin': islogin,'username': username})
    rp.set_cookie('page','0');
    return rp

def blogs(rq):
    posts = Blog.objects.all();
    posts = sorted(posts,key=lambda post: post.publish_time)

    islogin,username = validate(rq)

    rp = render(rq,'index.html',{'posts': posts,'islogin': islogin,'username': username})
    rp.set_cookie('page','1');
    return rp

def demos(rq):
    posts = Demo.objects.all();
    posts = sorted(posts,key=lambda post: post.publish_time)

    islogin,username = validate(rq)

    rp = render(rq,'index.html',{'posts': posts,'islogin': islogin,'username': username})
    rp.set_cookie('page','2');
    return rp

def detail(rq,id):
    islogin,username = validate(rq)
    try:
        post=Blog.objects.get(id=id)
        post.content = markdown(post.content)
        remarks = BlogRemark.objects.filter(blog_id=id)
        if islogin:
            rq.session['blog_id'] = id
        rp = render(rq,'blog.html',{'remarks':remarks,'blog': post,'islogin': islogin,'username': username})
        rp.set_cookie('page','999');
        return rp
    except Blog.DoesNotExist as err:
        try:
            post = Demo.objects.get(id=id)
            remarks = DemoRemark.objects.filter(demo_id=id)
            if islogin:
                 rq.session['demo_id'] = id
            rp = render(rq,'demo.html',{'demo': post,'remarks': remarks})
            rp.set_cookie('page','999');
            return rp
        except Demo.DoesNotExist as err:
            return HttpResponse(status=404)

def about(rq):
    islogin,username = validate(rq)
    rp = render(rq,'about.html',{'islogin': islogin,'username': username})
    rp.set_cookie('page','3');
    return rp
    
