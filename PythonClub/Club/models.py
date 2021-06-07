from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meeting_tittle=models.CharField(max_length=255)
    meeting_date=models.DateField(null=True)
    meeting_time=models.TimeField(null=True)
    location=models.TextField(null=True, blank=True)
    Agenda=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.meeting_tittle  
    
    class Meta: 
        db_table='meeting'
class MeetingMinute(models.Model):
    #meeting_id=models.CharField(max_length=255)
    meeting_id=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User, blank=True)
    #dateentered=models.DateField()
    #price=models.DecimalField(max_digits=6, decimal_places=2)       
    #productur1=models.URLField()
    #description=models.TextField()
    minutestext=models.TextField(null=True, blank=True)
    #def __str__(self):
      #  return self.attendance
    class Meta:
        db_table='meetingminute'
   
        

class Resource(models.Model):
    resource_name=models.CharField(max_length=255, null= True)
    resource_type=models.CharField(max_length=255, null= True)
    URL=models.URLField(null=True)
    date_entered=models.DateField()
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField(null=True, blank=True)
    #product=models.ForeignKey(MeetingMinute, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.resource_name

    class Meta:
        db_table='resource'

class Event(models.Model):
    event_title=models.CharField(max_length=255)
    location=models.TextField(null=True, blank=True)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    description=models.TextField(null=True, blank=True)
    user_id=models.CharField(max_length=255, null = True)

    def __str__(self):
        return self.event_title
    
    class Meta: 
        db_table='event'
    