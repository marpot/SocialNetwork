from django.urls import path
from .views import Index
#from login-page.views import login
from django.urls import path, include
from .views import Index
from .views import PostListView
from .views import TemplateView
from .views import LoginView
from .views import RegisterView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('login/', LoginView.as_view(), name='login-page' ),
    path('register/', RegisterView.as_view(), name='register'),
]