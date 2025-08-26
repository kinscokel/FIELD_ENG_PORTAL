from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'created_by', 'created_at', 'updated_at']