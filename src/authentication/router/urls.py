from django.contrib.auth.views import LogoutView
from django.urls import path

from authentication.views.change_password import change_password_view
from authentication.views.login import login_view
from authentication.views.register import register_view

urlpatterns = [
    path('register', register_view, name='auth-register'),
    path('login', login_view, name='auth-login'),
    path('logout', LogoutView.as_view(next_page='home'), name='auth-logout'),
    path('change_password', change_password_view, name='auth-change_password')
]
