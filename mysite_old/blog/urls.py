from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^index\.html/?$',views.index,name='index'),
    url(r'^blogs/?$',views.blogs,name='blogs'),
    url(r'^demos/?$',views.demos,name='demos'),
    url(r'^detail/(\d+)/?$',views.detail,name='detail'),
    url(r'^about/?$',views.about,name='about'),
    url(r'^$',views.index,name='index'),
]
