from django.urls import path

from authentication.views import login_view, register_view

urlpatterns = [
    path('register', register_view, name='auth_register'),
    path('login', login_view, name='auth_login'),
]
