from django.shortcuts import render
from .models import Event

# Create your views here.
def event(rq):
    events = Event.objects.all()
    rp = render(rq,'event/event.html',{'events': events})
    rp.set_cookie('page','3');
    return rp
