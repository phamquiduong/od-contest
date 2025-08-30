from django.contrib.auth.views import LogoutView
from django.urls import path

from authentication.views import change_password_view, login_view, register_view

urlpatterns = [
    path('register', register_view, name='auth_register'),
    path('login', login_view, name='auth_login'),
    path('logout', LogoutView.as_view(next_page='home'), name='auth_logout'),
    path('change-password', change_password_view, name='auth_change-password')
]
