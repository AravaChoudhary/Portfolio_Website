from django.db import models
from django.utils import timezone

# Create your models here.

# Interests Model
class cp(models.Model):
    NIKA_TYPE_CHOICES = [
        ('SW','SWIMMING'),
        ('CR', 'CRICKET'),
        ('PT', 'URDU POETRY'),
        ('MV', 'MOVIES'),
    ]

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='nikas/')
    date_added = models.DateTimeField(default=timezone.now)

    type = models.CharField(max_length=2,choices = NIKA_TYPE_CHOICES,default='PT')
    
    description = models.TextField(default='')

    def __str__(self):
        return self.name
    

#Projects Model
class Projects(models.Model):
    PROJECTS = [
        ('TA','Tweet App'),
        ('FRA','Food Recipe App'),
        ('MSD','Spam Email Detection'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='nikas/')
    date_added = models.DateTimeField(default=timezone.now)
    live_url = models.URLField(max_length=200, blank=True, null=True)
    github_url = models.URLField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=3, choices = PROJECTS,default='FRA')
    description = models.TextField(default='')

    def __str__(self) -> str:
        return self.name



class Visitor(models.Model):
    ip_address = models.CharField(max_length=45)
    user_agent = models.TextField()
    path = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
         return f"{self.ip_address} - {self.path} at {self.timestamp}"
    