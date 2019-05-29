from django.test import TestCase

# Create your tests here.
from .models import Meeting, Minute, Resource, event
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import meetingForm
import datetime


class MeetingTest(TestCase):
    def test_string(self):
        meet=Meeting(meettitle='monthly meeting')
        self.assertEqual(str(meet), meet.meettitle)
    
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MinuteTest(TestCase):
    def setUp(self):
        self.meet=Meeting(meettitle='yearly')
        self.min=Minute(minuteid=self.meet, minutetext='python')
        
    
    #def test_string(self): 
        #self.assertEqual(str(self.min), self.min.minuteid)
    
    
    def test_table(self):
        self.assertEqual(str(Minute._meta.db_table), 'minutes')
    
    
    
class ResourceTest(TestCase):
    def test_string(self):
        res=Resource(resourcename='python')
        self.assertEqual(str(res), res.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class eventsTest():
    def test_string(self):
        even=event(eventtitle='monthly meeting')
        self.assertEqual(str(even), even.eventtitle)
    
    def test_table(self):
        self.assertEqual(str(event._meta.db_table), 'event')

class indexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetmeetingTest(TestCase):
    def setUp(self):
        self.meet=Meeting.objects.create(meettitle='monthly', meetdate='2019-05-05',meettime='3:00',meetlocation='seattle', meetagenda='django')

    def test_meet_detail_success(self):
        response=self.client.get(reverse('meetdetails',args=(self.meet.id,)))
        self.assertEqual(response.status_code,200)


class meetingformtest(TestCase):
    def test_meetingform(self):
        data={
            'meettitle' :'meet1',
            'meetdate': datetime.date(2019,5,26),
            'meettime': datetime.datetime.now(),
            'meetlocation':'seattle',
            'meetagenda':'new trainning'



        }
        form =meetingForm(data=data)
        self.assertTrue(form.is_valid)


        





    



    
