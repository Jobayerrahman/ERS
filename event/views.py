from django.shortcuts import render
from .models import Event

def home(request):
    return render(request, 'Frontend/index.html');

def event_view(request):
    events_information  = Event.objects.all()
    return render(request, 'events/list.html', {'events_information':events_information});
