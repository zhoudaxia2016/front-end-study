from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^index\.html/?$',views.index,name='index'),
    url(r'^all\.html/?$',views.blogs,name='all'),
    url(r'^cooperation\.html/?$',views.cooperation,name='cooperation'),
    url(r'^about\.html/?$',views.about,name='about'),
    url(r'^blog/(?P<id>[0-9]+)/?$',views.blog,name='blog'),
]
