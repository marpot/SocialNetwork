from django.shortcuts import render
from django.views import View
from .models import Post

class Index(View):
    def get(self, request):
        return render(request, 'landing/index.html')

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-created_on')
        context = {'post_list': posts}
        return render(request, 'post-lists/post-list.html', context)

class LoginView(View):
    def get(self, request):
        return render(request, 'login-page/login.html')

class TemplateView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
