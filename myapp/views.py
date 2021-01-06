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
    print('game_name',game_name)
    #print(post)
    try:
      coder=get_object_or_404(Coder,pk=coder_id)
      screen_id=coder.recent_screen_id.split('_')[1]
      screen_id=game_name+'_'+str(int(screen_id)+1)
    except:
      created=time.ctime()
      coder=Coder(coder_id=coder_id,created=created)
      screen_id=game_name+'_1'
      coder.save()
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
    

    answer_log=screen_detail.answer_log
    time_log=screen_detail.time_log
    actions=screen_detail.actions

    print('screen_detail',screen_detail)

    if screen_detail.game_name in ['ThirtyPuzzle']:
      answer_log=answer_log[1:-1]
      answer_log=answer_log.split(",") 
      time_log=time_log[1:-1]
      time_log=time_log.split(",")
      answer_log=list(zip(answer_log,time_log))

    if screen_detail.game_name in ['FishTank']:
      answer_log=answer_log[1:-1]
      answer_log=answer_log.split("), (") 

      time_log=time_log[1:-1]
      time_log=time_log.split(",")

      #answer_log=list(zip(answer_log,time_log))

      expected_log=screen_detail.expected.split(',')

      answer_log=["%s, %s"%(answer_log[i],expected_log[i])\
                   for i in range(len(answer_log))]

      
      answer_log=["%s (%s)"%(answer_log[i][1:],time_log[i])\
                  for i in range(len(answer_log))]
      




    if screen_detail.game_name in ['NumberTrain','PatternTrain']:
      answer_log=answer_log[1:-1]
      answer_log=answer_log.split("),")

      time_log=time_log[1:-1]
      time_log=time_log.split(",")

      answer_log=list(zip(answer_log,time_log))

      print('answer_log',answer_log)

      actions=actions[1:-1]
      actions=actions.split(",")

      print('actions',actions)

      j=0
      answer_log_new=[]
      for i in range(len(actions)):
        if "Answer" not in actions[i]:
          answer_log_new.append(actions[i])
        else:
          answer_log_new.append(answer_log[j][0]+"  ("+answer_log[j][1]+")")
          j+=1

      answer_log=answer_log_new

    if screen_detail.game_name in ["MissingNumber"]:
      
      print('ssss')
      answer_log=answer_log[1:-1]
      answer_log=answer_log.split("),")

      time_log=time_log[1:-1]
      time_log=time_log.split(",")

      print('eee',answer_log,time_log)
      

      answer_log=list(zip(answer_log,time_log))

      print('answer_log',answer_log)

      actions=actions[1:-1]
      actions=actions.split(",")

      print('actions',actions)

      j=0
      answer_log_new=[]
      for i in range(len(actions)):
        if "Answer" not in actions[i]:
          answer_log_new.append(actions[i])
        else:
          answer_log_new.append(answer_log[j][0]+"  ("+answer_log[j][1]+")")
          j+=1

      answer_log=answer_log_new

    if screen_detail.game_name in ["MangoShop"]:
      answer_log=answer_log[1:-1]
      answer_log=answer_log.split(",")
      

      time_log=time_log[1:-1]
      time_log=time_log.split(",")
      
      answer_log=list(zip(answer_log,time_log))

      actions=actions[1:-1]
      actions=actions.split(",")

      j=0
      answer_log_new=[]
      for i in range(len(actions)):
        if "Answer" not in actions[i]:
          answer_log_new.append(actions[i])
        else:
          answer_log_new.append(answer_log[j][0]+"  ("+answer_log[j][1]+")")
          j+=1

      answer_log=answer_log_new

      #answer_log=screen_detail.answer_log.split("],")
      #answer_log=["".join([c for c in list(s) if c not in [']','[']]) for s in  answer_log]
      pass
    
    return render(request,'new.html',{'screen':screen_detail,'screen_num':screen_id,\
      'coder_id':coder_id,
      'answer_log':answer_log,
      'next_screen_id':next_screen_id,'before_screen_id':before_screen_id})
  except Exception as e:
    print('111오류메시지시작')
    print(e.args)
    print('111오류메시지끝')
    return finish(request)

def input_coder(request,game_name):
  return render(request,'input_coder.html',{'game_name':game_name})


def update(request,screen_id,coder_id):
  try:
    #https://rednooby.tistory.com/90

    post=request.POST

    #최초로 투표하는 경우, DB에 저장된 Choice객체가 없기 때문에 Choice를 새로 생성합니다
    # result=Result(result_id=)

    # choice = Choice(poll_id = poll.id, candidate_id = selection, votes = 1)
    # choice.save()
    print(post)
    if post['gaming']=='1':
      gaming=1
      
      if 'rapid_guessing' in post.keys():
        rg=1
      else:
        rg=0
      if 'system_abuse' in post.keys():
        sa=1
      else:
        sa=0
    elif post['gaming']=='0':
      gaming=0
      rg=-1
      sa=-1
    else:
      gaming=-1
      rg=-1
      sa=-1
  

    screen_id_to_update=screen_id.split('_')[0]+'_'+str(int(screen_id.split('_')[1])-1)
    result_time=time.ctime()

    result=Result(coder_id=coder_id,screen_id=screen_id_to_update,
    result_time=result_time,
    gaming=gaming,
      )
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



