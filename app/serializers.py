from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Log
        fields = ['unix_ts', 'user_id', 'event_name']