from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    """
    Description: Task manager
    """
    WORK_TYPES = (
    ('Road', 'Road'),
    ('Buiding', 'Building'),
    ('Maintenence', 'Maintenence'),
    ('Cleaning', 'Cleaning'),
    )
    name = models.CharField(max_length=1000)
    created = models.DateField(auto_now=True)
    completed = models.IntegerField(default=0)
    worktype = models.CharField(max_length=200,choices=WORK_TYPES,default="Building")
    lat = models.CharField(max_length=100)
    longt = models.CharField(max_length=100)
    def __unicode__(self):
    	return self.name

class UserDetails(models.Model):
    user = models.ForeignKey(User)
    contact = models.CharField(max_length=100)

class Road(models.Model):
    name = models.CharField(max_length=100)
    start_lat = models.CharField(max_length=20)
    start_long = models.CharField(max_length=20)
    middle_lat = models.CharField(max_length=20)
    middle_long = models.CharField(max_length=20)
    end_lat = models.CharField(max_length=20)
    end_long = models.CharField(max_length=20)
    path = models.TextField(max_length=400000)
    status = models.CharField(max_length=100)
    remarks = models.TextField(max_length=400,default="None")