from django.shortcuts import render
from .models import Screen
# Create your views here.

def home(request):
    screens=Screen.objects
    return render(request, 'home.html',{'screens':screens})

def create(request):
  # 생략
  profile.photo = request.FILES['photo']