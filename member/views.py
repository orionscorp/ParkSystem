from django.shortcuts import render
from django.http import HttpResponse
from .forms import signupForm

# Create your views here.

def index(request):
    return HttpResponse("HomeView")

def signup(request):
    form = signupForm()
    return render(request, 'member/signup.html', {'form':form})