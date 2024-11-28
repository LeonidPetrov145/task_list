# projects/views.py

# projects/serializers.py

from rest_framework import serializers

from task.models import Task
from task.serializers import TaskSerializer
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


