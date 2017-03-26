from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from .models import User

# Create your views here.
def signin(rq):
    username = rq.POST['username']
    user = User.objects.get(username=username)
    if user.passwd == rq.POST['passwd']:
        rq.session['username'] = user.username
        return HttpResponseRedirect('/index.html')
    else:
        return HttpResponse(status=403)

def signup(rq):
    username = rq.POST['username']
    try:
        user = User.objects.get(username=username)
        return HttpResponse(status=403)
    except User.DoesNotExist as e:
        passwd = rq.POST['passwd']
        user = User(username=username,passwd=passwd)
        user.save()
        rq.session['username'] = user.username
        return HttpResponseRedirect('/index.html')



def logout(rq):
    del rq.session['username']
    return HttpResponseRedirect('/index.html')

