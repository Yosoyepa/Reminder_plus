from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH
# Create your models here.
# Notes Clases.
class Notes(models.Model):
    STATUS = (
        ("new", "NEWEST"),
        ("old", "OLDEST"),
        ("title", "TITLE"),
    )
    heading = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS, default="old")
    def __str__(self):
        return self.heading

#Task List Clases.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank= True)
    complete = models.BooleanField(default=False)
    create = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['Complete']