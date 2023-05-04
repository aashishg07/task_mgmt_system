from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source = 'user.username', read_only = True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'completed', 'created_by']

