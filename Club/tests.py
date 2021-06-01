from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, Minutes, Resource, Event
import datetime
from .forms import ResourceForm, MeetingForm


class MeetingTest(TestCase):
    def setUp(self):
        self.mtdate = datetime.date(2021,6,2)
        self.mttime = datetime.time(12, 30, 00, 240000)
        self.myMeeting = Meeting(meetingtitle = 'Optional IT112 week 10', meetingdate  = self.mtdate, meetingtime = self.mttime, location ='Zoom', Agenda = 'Q&A')
        
    def test_string(self):
        self.assertEqual(str(self.myMeeting), 'Optional IT112 week 10')
        
    def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')
       
class MinuteTest(TestCase):
    def setUp(self):
        self.mt = Meeting(meetingtitle = 'Optional IT112 week 10')
        self.user = User(username = 'user01')
        self.myMinutes = Minutes(meeting = self.mt, attendance = self.user, minutes = "Spending 25 minutes.")
        
    def test_string(self):
        self.assertEqual(str(self.myMinutes), 'Spending 25 minutes.')
        
    def test_table(self):
       self.assertEqual(str(Minutes._meta.db_table), 'minutes')
    
class ResourceTest(TestCase):
    def setUp(self):
        self.user = User(username = 'user01')
        self.endate = datetime.date(2021,6,2)
        self.url = 'https://www.w3schools.com/python/'
        self.dcript = 'Python can be used on a server to create web applications.'
        self.myresource = Resource(resourcename = 'Python Tutorial', resourcetype = 'Tutorial', resourceurl = self.url, 
                                   entereddate = self.endate, user = self.user, description = self.dcript)
                
    def test_string(self):
        self.assertEqual(str(self.myresource), 'Python Tutorial')
        
    def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.ettile = 'Taking COVID Vaccine (2nd)'
        self.etdate = datetime.date(2021,6,4)
        self.ettime = datetime.time(10, 00, 00, 240000)
        self.user = User(username = 'user01')
        self.location = 'Ash Way Park & Ride DRIVE THROUGH - COVID Vaccine Site'
        self.dcript ='This is second appointment for vaccination.'
        self.myEvent = Event(eventtitle = self.ettile, eventdate = self.etdate, eventtime= self.ettime, 
                             location = self.location, description = self.dcript, user = self.user)
        
    def test_string(self):
        self.assertEqual(str(self.myEvent), 'Taking COVID Vaccine (2nd)')
        
    def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'event')
       
    
# form test
class NewResourceForm(TestCase):
    def test_ResourceForm(self):
        data = {
            'resourcename': 'Python Tutorial', 
            'resourcetype': 'Tutorial', 
            'resourceurl': 'https://www.w3schools.com/python/', 
            'entereddate': datetime.date(2021,6,1), 
            'user': 'yaman', 
            'description': 'Python can be used on a server to create web applications.'           
        }
        form = ResourceForm(data)
        self.assertTrue(form.is_valid)
        
    # def test_resurcename_empty(self):
    #     data = {
    #         'resourcename': '', 
    #         'resourcetype': 'Tutorial', 
    #         'resourceurl': 'https://www.w3schools.com/python/', 
    #         'entereddate': datetime.date(2021,6,1), 
    #         'user': 'yaman', 
    #         'description': 'Python can be used on a server to create web applications.'           
    #     }
    #     form = ResourceForm(data)
    #     self.assertFalse(form.is_valid)
        
class NewMeetingForm(TestCase):
    def test_ResourceForm(self):
        data = {
            'meetingtitle': 'Optional IT112 week 10', 
            'meetingdate': datetime.date(2021,6,2), 
            'meetingtime': datetime.time(12, 30, 00, 240000), 
            'location': 'Zoom', 
            'Agenda': 'Q&A'     
        }
        form = MeetingForm(data)
        self.assertTrue(form.is_valid)