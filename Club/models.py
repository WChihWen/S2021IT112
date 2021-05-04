from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingdate = models.DateField()
    meetingtime = models.TimeField()
    location = models.TextField()
    Agenda =  models.TextField()
    
    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'
    
class Minutes(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance = models.ForeignKey(User, on_delete=models.CASCADE)
    minutes = models.TextField()
    
    def __str__(self):
        return self.minutes
    
    class Meta:
        db_table='minutes'
    
class Resource(models.Model):
    resourcename = models.CharField(max_length=255)
    resourcetype = models.CharField(max_length=255)
    resourceurl = models.URLField(null=True, blank=True)
    entereddate = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'
        
    
class Event(models.Model):
    eventtitle = models.CharField(max_length=255)
    eventdate = models.DateField()
    eventtime = models.TimeField()
    location = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'