from django.urls import path
from .views import *

urlpatterns = [
    path("posts/", PostListCreateAPI.as_view()),
    path("posts/<int:pk>/", PostRetrieveUpdateDestroyAPI.as_view()),
    path("posts/<int:pk>/comments/", CommentCreateAPI.as_view()),
    path("posts/<int:pk>/comments/<int:comment_pk>/", CommentRetrieveUpdateDestroyAPI.as_view()),
    path("messages/", MessageApi.as_view()),
]