from django.urls import path
from post.views import (
    AuthorListCreateView,
    AuthorRetrieveUpdateDestroyView,
    PostListCreateView,
    PostRetrieveUpdateDestroyView
)
from profiles.views import (
    FeatureListCreateView,
    FeatureRetrieveUpdateDestroyView,
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
    AboutListCreateView,
    AboutRetrieveUpdateDestroyView
)


urlpatterns = [
    # Post App URLs - Author endpoints
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),

    # Post App URLs - Post endpoints
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<slug:slug>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),

    # Profiles App URLs - Feature endpoints
    path('features/', FeatureListCreateView.as_view(), name='feature-list-create'),
    path('features/<int:pk>/', FeatureRetrieveUpdateDestroyView.as_view(), name='feature-detail'),

    # Profiles App URLs - Project endpoints
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),

    # Profiles App URLs - About endpoints
    path('about/', AboutListCreateView.as_view(), name='about-list-create'),
    path('about/<int:pk>/', AboutRetrieveUpdateDestroyView.as_view(), name='about-detail'),
]
