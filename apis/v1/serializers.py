from rest_framework import serializers
from taskmgr.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title","text","done",'created_at']
        read_only_fields = ['created_at']