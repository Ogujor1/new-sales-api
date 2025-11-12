from django.db import models


# Feature Model
class Feature(models.Model):
    """
    Represents a feature or service offered.
    Contains details about the feature with a link to more information.
    """
    name = models.CharField(max_length=200)  # Feature name
    title = models.CharField(max_length=250)  # Feature title/heading
    url = models.URLField(max_length=500)  # Link to feature details or external resource
    timestamp = models.DateTimeField(auto_now_add=True)  # Date and time when feature was created

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']  # Order by most recent first


# Project Model
class Project(models.Model):
    """
    Represents a project or portfolio item.
    Contains project details and thumbnail image.
    """
    title = models.CharField(max_length=250)  # Project title
    description = models.TextField()  # Project description/details
    timestamp = models.DateTimeField(auto_now_add=True)  # Date and time when project was created
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')  # Project thumbnail image

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']  # Order by most recent first


# About Model
class About(models.Model):
    """
    Represents information about the organization or individual.
    Contains about details, mission statement, and thumbnail image.
    """
    title = models.CharField(max_length=250)  # About section title
    description = models.TextField()  # About description/overview
    mission = models.TextField()  # Mission statement or goals
    timestamp = models.DateTimeField(auto_now_add=True)  # Date and time when about entry was created
    thumbnail = models.ImageField(upload_to='about/thumbnails/')  # About section thumbnail image

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']  # Order by most recent first
