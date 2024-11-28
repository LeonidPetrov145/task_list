from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True )
    time_update = models.DateTimeField(auto_now=True)
    status =  models.CharField(max_length=255)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    categories =  models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


