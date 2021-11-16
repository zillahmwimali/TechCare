
from django.db import models
import datetime

# Create your models here.
 
class Event(models.Model):
   title = models.CharField(max_length=200)
   organizer=models.CharField(max_length=200,blank=True,null=True)
   description = models.TextField()
   start_time = models.DateTimeField()
   end_time = models.DateTimeField()