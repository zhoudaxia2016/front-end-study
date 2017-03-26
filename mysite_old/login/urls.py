from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^signin/?$',views.signin,name='signin'),
    url(r'^signup/?$',views.signup,name='signup'),
    url(r'^logout/?$',views.logout,name='logout'),
]

