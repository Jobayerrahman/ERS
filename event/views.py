from .models import Event
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'frontend/index.html')

@login_required(login_url='login')
def event_view(request):
    events_information  = Event.objects.all()
    return render(request, 'events/list.html', {'events_information':events_information})
