from django.urls import path
from . import views


app_name = 'beetle'

urlpatterns = [
    path('beetle/', views.home, name='beetle_home'),
]