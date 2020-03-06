from django.shortcuts import render,redirect
from .models import Screen
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    return render(request,'home.html')
    screen_id=1
    screen_detail=get_object_or_404(Screen,pk=screen_id)
    next_screen_id=screen_id+1
    before_screen_id=screen_id-1
    return render(request,'new.html',{'screen':screen_detail,'next_screen_id':next_screen_id,'before_screen_id':before_screen_id})


def create(request):
  # 생략
  profile.photo = request.FILES['photo']

def detail(request,screen_id): 
  #https://tutorial.djangogirls.org/ko/extend_your_application/
  #https://ssungkang.tistory.com/entry/Django-06pk-path-converter-getobjector404%EB%9E%80?category=320582
  try:
    screen_detail=get_object_or_404(Screen,pk=screen_id)
    next_screen_id=screen_id+1
    before_screen_id=screen_id-1
    return render(request,'new.html',{'screen':screen_detail,'next_screen_id':next_screen_id,'before_screen_id':before_screen_id})
  except:
    return render(request,'home.html')
    
def update(request,screen_id):
  print(request.POST['choice'])
  next_screen_id=screen_id+1
  return redirect('/screen/'+str(screen_id))
