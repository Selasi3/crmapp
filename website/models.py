from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Record(models.Model):

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female")
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email= models.EmailField(max_length=254, default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    location = models.CharField(max_length=50, default='')

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")







