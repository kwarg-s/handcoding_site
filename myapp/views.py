from django.shortcuts import render,redirect
from .models import Screen,Result,Coder
from django.shortcuts import get_object_or_404
import time
# Create your views here.

def home(request):
  return render(request,'home.html')

def finish(request):
  return render(request,'finish.html')

def selection(request,game_name):
  return render(request, 'selection.html')


def submit_coder(request,game_name):
  try:
    print('어딨어')
    post=request.POST
    coder_id=post['coder_id']
    coder_id=coder_id+'_'+game_name
    print(post)
    try:

      created=time.ctime()
      coder=Coder(coder_id=coder_id,created=created)
      screen_id=game_name+'_1'
      coder.save()
    except:
      coder=get_object_or_404(Coder,pk=coder_id)
      screen_id=coder.recent_screen_id.split('_')[1]
      screen_id=game_name+'_'+str(int(screen_id)+1)
    if coder_id=="_"+game_name:
      return redirect('/'+coder_id+'/'+game_name+'_1'+'/')
    return redirect('/'+coder_id+'/'+screen_id+'/')
  except Exception as e:
    print('여기야?')
    print(e.args)

  


def detail(request,screen_id,coder_id): 
  #https://tutorial.djangogirls.org/ko/extend_your_application/
  #https://ssungkang.tistory.com/entry/Django-06pk-path-converter-getobjector404%EB%9E%80?category=320582
  try:
    # screen_detail=get_object_or_404(Screen,screen_id=screen_id,game_name=game_name)
    screen_detail=get_object_or_404(Screen,pk=screen_id)
    game_name,screen_num=screen_id.split("_")[0],int(screen_id.split("_")[1])
    next_screen_id=game_name+'_'+str(screen_num+1)
    before_screen_id=game_name+'_'+str(screen_num-1)
    print(next_screen_id)
    print(before_screen_id)

    
    return render(request,'new.html',{'screen':screen_detail,'screen_num':screen_id,\
      'coder_id':coder_id,
      'next_screen_id':next_screen_id,'before_screen_id':before_screen_id})
  except Exception as e:
    print('111오류메시지시작')
    print(e.args)
    print('111오류메시지끝')
    return finish(request)



def update(request,screen_id,coder_id):
  try:
    #https://rednooby.tistory.com/90

    post=request.POST

    #최초로 투표하는 경우, DB에 저장된 Choice객체가 없기 때문에 Choice를 새로 생성합니다
    # result=Result(result_id=)

    # choice = Choice(poll_id = poll.id, candidate_id = selection, votes = 1)
    # choice.save()

    if 'gaming' in post.keys():
      gaming=1
      s=""
      if 'rapid_guessing' in post.keys():
        s+="rapid_guessing "
      if 'system_abuse' in post.keys():
        s+="system_abuse "
    else:
      gaming=0
      s="non-gaming"

    screen_id_to_update=screen_id.split('_')[0]+'_'+str(int(screen_id.split('_')[1])-1)
    result_time=time.ctime()
    result=Result(screen_id=screen_id_to_update,gaming=gaming,gaming_type=s,result_time=result_time,coder_id=coder_id)
    result.save()
    coder=get_object_or_404(Coder,pk=coder_id)
    coder.recent_screen_id=screen_id_to_update
    coder.save()



    return redirect('/'+coder_id+'/'+screen_id)
  
  except Exception as e:
    print('222오류메시지시작')
    print(e.args)
    print('222오류메시지끝')
    return render(request,'home.html')



