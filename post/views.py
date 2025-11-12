from rest_framework import generics
from .models import Author, Post
from .serializers import AuthorSerializer, PostSerializer


# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    """
    GET: List all authors
    POST: Create a new author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single author
    PUT/PATCH: Update an author
    DELETE: Delete an author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Post Views
class PostListCreateView(generics.ListCreateAPIView):
    """
    GET: List all posts
    POST: Create a new post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single post by slug
    PUT/PATCH: Update a post
    DELETE: Delete a post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'  # Use slug instead of pk for URL lookup
