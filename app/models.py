from django.db import models
# import os

class Config(models.Model):
  
    api_key = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200,choices = [("email","Email"),("phone_number_sms","Phone")])



class Info(models.Model):
    name = models.CharField( max_length=30)  # Field name made lowercase.
    email = models.EmailField(max_length=254) # field name for email in lowercase
    def __str__(self):
            return self.name


class Customized_Info(models.Model):
    c_name = models.CharField( max_length=30)  # Field name made lowercase.m
    logo = models.ImageField(upload_to = 'pics') # field name for email in lowercase
    bg_img =  models.ImageField(upload_to = 'pics')  # Field name made lowercase.m
    url = models.URLField(max_length=231)# field name for email in lowercase
    c_url = models.URLField(max_length=231) # Field name made lowercase.models
    desc = models.CharField( max_length=400,default='') 
    def __str__(self):
        return self.c_name
