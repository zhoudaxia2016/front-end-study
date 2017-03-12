from django.shortcuts import render
from .models import *
from comment.models import Comment

def validate(rq,rp):
    if rq.session.get('is_login',False):
        print(rq.session.get('is_login'))
        rp.set_cookie('islogin','true')
    else:
        rp.set_cookie('islogin','false')

# Create your views here.
def index(rq):
    blog = Blog.objects.order_by('-published_time')[0]
    blog.view_num += 1
    blog.save()
    Comments = Comment.objects.filter(blog=blog).order_by('-published_time')
    rp = render(rq,'index.html',{'Blog': blog,'Comments': Comments})
    validate(rq,rp)
    return rp 

def blogs(rq):
    Blogs = Blog.objects.all()
    return render(rq,'all.html',{'Blogs': Blogs})

def cooperation(rq):
    msg = Msg.objects.get(title='cooperation')
    msg.view_num += 1
    msg.save()
    return render(rq,'cooperation.html',{'msg': msg})

def about(rq):
    msg = Msg.objects.get(title='about')
    msg.view_num += 1
    msg.save()
    return render(rq,'about.html',{'msg': msg})

def blog(rq,id):
    blog = Blog.objects.get(id=id)
    blog.view_num += 1
    blog.save()
    Comments = Comment.objects.filter(blog=blog).order_by('-published_time')
    return render(rq,'blog.html',{'Blog': blog,'Comments': Comments})

def login(rq):
    return render(rq,'login.html')
