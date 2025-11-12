from rest_framework import generics
from .models import Feature, Project, About
from .serializers import FeatureSerializer, ProjectSerializer, AboutSerializer


# Feature Views
class FeatureListCreateView(generics.ListCreateAPIView):
    """
    GET: List all features
    POST: Create a new feature
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class FeatureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single feature
    PUT/PATCH: Update a feature
    DELETE: Delete a feature
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


# Project Views
class ProjectListCreateView(generics.ListCreateAPIView):
    """
    GET: List all projects
    POST: Create a new project
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single project
    PUT/PATCH: Update a project
    DELETE: Delete a project
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# About Views
class AboutListCreateView(generics.ListCreateAPIView):
    """
    GET: List all about entries
    POST: Create a new about entry
    """
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single about entry
    PUT/PATCH: Update an about entry
    DELETE: Delete an about entry
    """
    queryset = About.objects.all()
    serializer_class = AboutSerializer
