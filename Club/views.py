from django.shortcuts import render, get_object_or_404
from .models import Resource, User, Meeting
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def resources(request):
    return render(request, 'Club/resources.html', {'resource_list': Resource.objects.all()})
 
def meetings(request):
    return render(request, 'Club/meetings.html', {'meeting_list': Meeting.objects.all()})
 
def meetingdetails(request, id):
    return render(request, 'Club/meetingdetails.html', {'meeting_list': get_object_or_404(Meeting, pk=id)})
     
     