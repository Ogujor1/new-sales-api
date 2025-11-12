from django.db import models


# Author Model
class Author(models.Model):
    """
    Represents an author who can create posts.
    """
    fullname = models.CharField(max_length=200)  # Author's full name
    description = models.TextField()  # Author's bio or description
    thumbnail = models.ImageField(upload_to='authors/thumbnails/')  # Author's profile picture
    timestamp = models.DateTimeField(auto_now_add=True)  # Date and time when author was created

    def __str__(self):
        return self.fullname

    class Meta:
        ordering = ['-timestamp']  # Order by most recent first


# Post Model
class Post(models.Model):
    """
    Represents a blog post or article written by an author.
    """
    title = models.CharField(max_length=250)  # Post title
    slug = models.SlugField(max_length=250, unique=True)  # URL-friendly version of title
    description = models.TextField()  # Post content
    timestamp = models.DateTimeField(auto_now_add=True)  # Date and time when post was created
    last_updated = models.DateTimeField(auto_now=True)  # Date and time of last update
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')  # Post author

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']  # Order by most recent first
