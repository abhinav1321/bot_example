from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



# Create your models here.
class SiteUrl(models.Model):
    url_address = models.CharField(max_length=30, primary_key=True)
    page_name = models.CharField(max_length=20, default='')
    status = models.CharField(max_length=3, default='')
    last_update = models.DateTimeField(default=datetime.now())
    time_till_change = models.IntegerField(default=0)

    def __str__(self):
        return self.page_name



'''
Still Not Implememted

class SiteUrl(models.Model):
    project_name = models.ForeignKey('Project', on_delete=models.CASCADE)
    url_address = models.CharField(max_length=30, primary_key=True)
    page_name = models.CharField(max_length=20, default='')
    status = models.CharField(max_length=3, default='')
    last_update = models.DateTimeField(default=datetime.now())
    time_till_change = models.IntegerField(default=0)
    

    def __str__(self):
        return self.page_name


class Project(models.Model):
    project_name = models.CharField(max_length=30, default=None)
    project_description = models.CharField(max_length=200, default=None)
    
    def __str__(self):
    return self.project_name

class User(AbstractUser):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    
'''
