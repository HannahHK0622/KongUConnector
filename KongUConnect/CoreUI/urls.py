# CoreUI/urls.py

from django.urls import path
from . import views

app_name = 'CoreUI'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.authenticator, name='login'),
]