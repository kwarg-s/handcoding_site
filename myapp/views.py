from django.shortcuts import render,redirect
from .models import Screen
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
  return render(request,'home.html')

def finish(request):
  return render(request,'base.html')


def detail(request,screen_id): 
  #https://tutorial.djangogirls.org/ko/extend_your_application/
  #https://ssungkang.tistory.com/entry/Django-06pk-path-converter-getobjector404%EB%9E%80?category=320582
  try:
    screen_detail=get_object_or_404(Screen,pk=screen_id)
    next_screen_id=screen_id+1
    before_screen_id=screen_id-1
    return render(request,'new.html',{'screen':screen_detail,'next_screen_id':next_screen_id,'before_screen_id':before_screen_id})
  except Exception as e:
    print('오류메시지시작')
    print(e.args)
    print('오류메시지끝')
    return finish(request)

def update(request,screen_id):
  try:
    #https://rednooby.tistory.com/90
    
    post=request.POST
    screen=Screen.objects.get(pk=screen_id-1)

    if 'gaming' in post.keys():
      screen.gaming=1
      screen.save()
      print(post)
      s=""
      if 'rapid_guessing' in post.keys():
        s+="rapid_guessing "
      if 'system_abuse' in post.keys():
        s+="system_abuse "
      screen.gaming_type=s
      screen.save()
    else:
      screen.gaming=0
      screen.save()
    
    # screen.gaming_type=request.POST['gaming_type']
    screen.save()
    return redirect('/screen/'+str(screen_id))
  except Exception as e:
    print('오류메시지시작')
    print(e.args)
    print('오류메시지끝')
    return render(request,'home.html')
