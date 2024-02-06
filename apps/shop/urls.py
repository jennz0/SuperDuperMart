from django.urls import path
from .views import *

urlpatterns = [
    path("products/", products_list),
    path("products/<int:pk>/", products_detail),
    path("orders/", orders_list),
    # path("posts/<int:pk>/", PostRetrieveUpdateDestroyAPI.as_view()),
    # path("posts/<int:pk>/comments/", CommentCreateAPI.as_view()),
    # path("posts/<int:pk>/comments/<int:comment_pk>/", CommentRetrieveUpdateDestroyAPI.as_view()),
    path("messages/", MessageApi.as_view()),
]