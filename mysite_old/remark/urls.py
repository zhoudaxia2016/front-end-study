from django.conf.urls import url 
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^blog/?$', views.blogRemark,name='blogRemark'),
    url(r'^demo/?$', views.demoRemark,name='demoRemark'),
]
