from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('resources/', views.resources, name="resources"),
    path('meetings/', views.meetings, name="meetings"),
    path('meetingdetails/<int:id>', views.meetingdetails, name="meetingdetails"),
    path('newResource/', views.newResource, name='newResource'), 
    path('newMeeting/', views.newMeeting, name='newMeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]