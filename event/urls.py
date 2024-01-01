from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('event-list',views.event_view, name="event_list"),
]