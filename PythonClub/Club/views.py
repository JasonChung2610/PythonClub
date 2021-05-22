from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinute, Resource, Event
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def resources(request):
    resource_list= Resource.objects.all()   
    return render(request, 'Club/resources.html', {'resource_list': resource_list} )

def meetings(request):
    meeting_list= Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meeting_list': meeting_list})

def details(request, id):
    meeting_detail = get_object_or_404(Meeting, pk=id) 
    return render(request, 'Club/details.html', {'meeting_detail': meeting_detail})
    
