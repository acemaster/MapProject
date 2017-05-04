from rest_framework import serializers
from manager.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'created', 'completed', 'worktype','lat', 'longt')