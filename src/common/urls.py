from django.urls import path

from common.views.home import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
