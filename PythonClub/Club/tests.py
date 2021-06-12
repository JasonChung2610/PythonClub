from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinute, Resource, Event
import datetime
from .forms import MeetingForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.name=Meeting(meeting_tittle='First Meeting')
        self.Meeting=Meeting(meeting_tittle=self.name,  location="Seattle Theather", Agenda="333")
    def test_typestring(self):
        self.assertEqual(str(self.name), 'First Meeting')
    
    def test_tablename(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinuteTest(TestCase):
    def setUp(self):
        #self.user=User.objects.create(username='jason')
        self.id=Meeting(meeting_tittle='First Meeting')
        self.user=User(username='jason')
        self.meetingminute=MeetingMinute(meeting_id=self.id, minutestext="hehe")

    def test_stringforfun(self):
        self.assertEqual(str(self.meetingminute), 'MeetingMinute object (None)')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinute._meta.db_table), 'meetingminute')

class ResourceTest(TestCase):
    def setUp(self):
        self.resource=Resource(resource_name='Harrier',resource_type='Low Rank Dog Breed', URL='https://www.akc.org/dog-breeds/harrier/', description="Average cost from a breeder: $300" )

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

    def test_typestring(self):
        self.assertEqual(str(self.resource), 'Harrier')

class EventTest(TestCase):
    def setUp(self):
        self.event=Event(event_title='1',location='', description="" )

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

    def test_typestring(self):
        self.assertEqual(str(self.event), '1')
    

class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='Gwen', password='@Soxsox123')
        self.resource=Resource.objects.create(resource_name='Afghan Hound',resource_type='High Rank Dog Breed', user_id=self.test_user, date_entered=datetime.date(2021,5,15), URL='https://www.akc.org/dog-breeds/afghan-hound/', description="Afghan Hound – $7,000")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('resources'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/newmeeting/')