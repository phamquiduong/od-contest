from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView, TokenVerifyView

from authentication.views.api.change_password import ChangePasswordView

urlpatterns = [
    path('login', TokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('verify', TokenVerifyView.as_view()),
    path('logout', TokenBlacklistView.as_view()),
    path('change-password', ChangePasswordView.as_view()),
]
