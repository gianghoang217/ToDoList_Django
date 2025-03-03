# todo_api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Assign the current user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)