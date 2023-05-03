from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=255)
    user_instance = models.ForeignKey(User, on_delete=models.CASCADE)

class Work(models.Model):
    LINK_TYPES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    )
    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=LINK_TYPES)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField(Work)

