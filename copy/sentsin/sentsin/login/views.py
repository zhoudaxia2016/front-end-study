from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import User
from django.core.urlresolvers import reverse

# Create your views here.
def login(rq):
    return render(rq,'login.html')

def logout(rq):
  try:
      del rq.session['is_login']
      del rq.session['user_id']
  except KeyError:
      pass
  return HttpResponseRedirect(reverse('blog:index'))

def validate(rq):
    user = get_object_or_404(User,username=rq.POST['username'])
    if user.password == rq.POST['password']:
        rq.session['is_login'] = True
        rq.session['user_id'] = user.id
        rp = HttpResponseRedirect(reverse('blog:index'))
        rp.set_cookie('username',user.username)
        rp.set_cookie('islogin','true')
        return rp;
    else:
        return HttpResponse('Your user dose not exist or your username and password did not match!')

def signin(rq):
    return render(rq,'signin.html')

def submit(rq):
    username = rq.POST['username']
    password = rq.POST['password']
    try: 
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        new_user = User(username=username,password=password)
        new_user.save()
        rq.session['is_login'] = True
        rq.session['user_id'] = new_user.id
        rp = HttpResponseRedirect(reverse('blog:index'))
        rp.set_cookie('username',username)
        rp.set_cookie('islogin','true')
        return rp
    else:
        return HttpResponse('用户名已经存在')
