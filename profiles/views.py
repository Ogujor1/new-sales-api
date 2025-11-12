from rest_framework import generics
from .models import Feature, Project, About
from .serializers import FeatureSerializer, ProjectSerializer, AboutSerializer
from .permissions import IsAdminOrReadOnly


# Feature Views
class FeatureListCreateView(generics.ListCreateAPIView):
    """
    GET: List all features (public access)
    POST: Create a new feature (admin only)
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admin can create, everyone can read


class FeatureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single feature (public access)
    PUT/PATCH: Update a feature (admin only)
    DELETE: Delete a feature (admin only)
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admin can modify, everyone can read


# Project Views
class ProjectListCreateView(generics.ListCreateAPIView):
    """
    GET: List all projects (public access)
    POST: Create a new project (admin only)
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admin can create, everyone can read


class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single project (public access)
    PUT/PATCH: Update a project (admin only)
    DELETE: Delete a project (admin only)
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admin can modify, everyone can read


# About Views
class AboutListCreateView(generics.ListCreateAPIView):
    """
    GET: List all about entries (public access)
    POST: Create a new about entry (admin only)
    """
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admin can create, everyone can read


class AboutRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single about entry (public access)
    PUT/PATCH: Update an about entry (admin only)
    DELETE: Delete an about entry (admin only)
    """
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admin can modify, everyone can read
