from django.conf.urls import url, include
from . import views

app_name = 'event'

urlpatterns = [
    url(r'^$',views.event,name='event'),
]


