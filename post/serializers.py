from rest_framework import serializers
from .models import Author, Post


# Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model.
    Converts Author model instances to/from JSON.
    """
    class Meta:
        model = Author
        fields = ['id', 'fullname', 'description', 'thumbnail', 'timestamp']
        read_only_fields = ['id', 'timestamp']  # Auto-generated fields


# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post model.
    - When reading (GET): Returns full author details (nested serializer)
    - When writing (POST/PUT): Accepts author_id to link to an author
    """
    author = AuthorSerializer(read_only=True)  # Nested serializer for GET requests
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True  # Only used for POST/PUT requests
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'description', 'timestamp', 'last_updated', 'author', 'author_id']
        read_only_fields = ['id', 'timestamp', 'last_updated']  # Auto-generated fields
