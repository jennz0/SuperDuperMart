from django.urls import path
from .views import SignUpView, MyTokenObtainPairView
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.getRoutes),
    path("signup/", views.signup),
    path("login/", views.login),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path("signup/", SignUpView.as_view(), name="signup"),
]