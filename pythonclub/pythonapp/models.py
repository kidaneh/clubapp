from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meettitle=models.CharField(max_length=255)
    meetdate=models.DateField()
    meettime=models.TimeField()
    meetlocation=models.CharField(max_length=255)
    meetagenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meettitle

    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class Minute(models.Model):
    minuteid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    minuteattendance=models.ManyToManyField(User)
    minutetext=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.minutesid
    
    class Meta:
        db_table='minutes'
        verbose_name_plural='minutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.TextField(null=True, blank=True)
    resourceURL=models.URLField(null=True, blank=True)
    resourcedateentered=models.DateField()
    resourceuserid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'

class event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField
    eventdescription=models.TextField(null=True, blank=True)
    eventuserid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return  self.eventtitle
    
    class Meta:
        db_table='event'
        verbose_name="events"







    

