from rest_framework import generics
from .models import Author, Post
from .serializers import AuthorSerializer, PostSerializer
from profiles.permissions import IsAdminOrReadOnly


# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    """
    GET: List all authors (public access)
    POST: Create a new author (admin only)
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admin can create, everyone can read


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single author (public access)
    PUT/PATCH: Update an author (admin only)
    DELETE: Delete an author (admin only)
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admin can modify, everyone can read


# Post Views
class PostListCreateView(generics.ListCreateAPIView):
    """
    GET: List all posts (public access)
    POST: Create a new post (admin only)
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admin can create, everyone can read


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single post by slug (public access)
    PUT/PATCH: Update a post (admin only)
    DELETE: Delete a post (admin only)
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'  # Use slug instead of pk for URL lookup
    permission_classes = [IsAdminOrReadOnly]  # Admin can modify, everyone can read
