from django.db import models
from django.utils import timezone

# Create your models here.
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
    

class Visitor(models.Model):
    ip_address = models.CharField(max_length=45)
    user_agent = models.TextField()
    path = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"{self.ip_address} - {self.path} at {self.timestamp}"
    