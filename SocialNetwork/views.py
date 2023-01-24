from django.shortcuts import render
from django.http import HttpResponse
from forms import NewUserForm

# Create your views here.
def index(request):
    return HttpResponse('SocialApp')

def login(request):
    return HttpResponse()
