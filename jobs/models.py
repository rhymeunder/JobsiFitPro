    #from __future__ import unicode_literals
    
from django.db import models
from django.conf import settings
     # Create your models here.  models are tables
     

         
class seeker(models.Model):
         user = models.OneToOneField(settings.AUTH_USER_MODEL) #user object
         
     
         first_name = models.CharField(max_length = 30)
         last_name = models.CharField(max_length = 30)
         seeker_id = models.IntegerField(blank=True, null=True)
         #message = models.OneToOneField(message)
         last_resume_date = models.DateField()
         resume = models.FilePathField()   
         video = models.FilePathField()
        
         
         
         def get_seeker_fname (self):
             return self.first_name + " " + self.last_name
         
         
            
class employer(models.Model):
       #  user = models.OneToOneField(settings.AUTH_USER_MODEL) #user object
         
     
         first_name = models.CharField(max_length = 30)
         last_name = models.CharField(max_length = 30)
         employer_id = models.IntegerField(blank=True, null=True)
       #  message = models.OneToOneField(message)

     #    starred = models.ManyToMany(seeker)
     #    selected = models.ManyToMany(seeker)  
         
         
         def get_employer_fullname (self):
             return self.first_name + " " + self.last_name
         
        
class message(models.Model):
         messages = models.CharField(max_length = 30)
         
         def get_message (self):
             return self.messages
class jobs(models.Model):
    
         seekerornot =models.BooleanField()
         
         