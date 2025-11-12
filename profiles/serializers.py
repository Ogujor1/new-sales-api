from rest_framework import serializers
from .models import Feature, Project, About


# Feature Serializer
class FeatureSerializer(serializers.ModelSerializer):
    """
    Serializer for Feature model.
    Converts Feature model instances to/from JSON.
    """
    class Meta:
        model = Feature
        fields = ['id', 'name', 'title', 'url', 'timestamp']
        read_only_fields = ['id', 'timestamp']  # Auto-generated fields


# Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Project model.
    Converts Project model instances to/from JSON.
    """
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'timestamp', 'thumbnail']
        read_only_fields = ['id', 'timestamp']  # Auto-generated fields


# About Serializer
class AboutSerializer(serializers.ModelSerializer):
    """
    Serializer for About model.
    Converts About model instances to/from JSON.
    """
    class Meta:
        model = About
        fields = ['id', 'title', 'description', 'mission', 'timestamp', 'thumbnail']
        read_only_fields = ['id', 'timestamp']  # Auto-generated fields
