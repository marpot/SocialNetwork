from django.urls import path
from landing.views import Index
#from login-page.views import login
from django.urls import path, include
from landing.views import Index
from .views import PostListView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('posts', PostListView.as_view(), name='post-list'),
]