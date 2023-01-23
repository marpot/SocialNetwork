from django.urls import path, include
from landing.views import Index

from . import views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    
]