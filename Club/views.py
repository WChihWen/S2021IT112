from django.shortcuts import render, get_object_or_404
from .models import Resource, User, Meeting
from django.urls import reverse_lazy
from .forms import ResourceForm, MeetingForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def resources(request):
    return render(request, 'Club/resources.html', {'resource_list': Resource.objects.all()})
 
def meetings(request):
    return render(request, 'Club/meetings.html', {'meeting_list': Meeting.objects.all()})
 
def meetingdetails(request, id):
    return render(request, 'Club/meetingdetails.html', {'meeting_list': get_object_or_404(Meeting, pk=id)})

@login_required
def newResource(request):
    form = ResourceForm    
    if request.method == 'POST':
        form  = ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = ResourceForm
    else:
        form = ResourceForm        
    return render(request,'Club/newresource.html', {'form': form})

@login_required    
def newMeeting(request):
    form = MeetingForm
    if request.method == 'POST':
        form  = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = MeetingForm
    else:
        form = MeetingForm        
    return render(request,'Club/newmeeting.html', {'form': form})
     
def loginmessage(request):
    return render(request,'Club/loginmessage.html')     

def logoutmessage(request):
    return render(request, 'Club/logoutmessage.html')