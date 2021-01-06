from django.db import models
import time
#https://ssungkang.tistory.com/entry/Django-media-%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C%ED%95%98%EA%B8%B0
# Create your models here.
class Screen(models.Model):
    screen_num=models.IntegerField( default="0")
    screen_id=models.CharField(max_length=200, default="none",primary_key=True)
    # screen_num=models.IntegerField
    
    user=models.CharField(max_length=200, default="none")
    problem_id=models.CharField(max_length=200, default="none")
    expected=models.CharField(max_length=200, default="none")
    game_name=models.CharField(max_length=200,default="MangoShop")
    
    #newly added
    answer_log=models.CharField(max_length=1000, default="none")
    time_log=models.CharField(max_length=1000, default="none")
    actions=models.CharField(max_length=1000, default="none")

    #old
    # day_problem=models.CharField(max_length=200, default="none")
    # day=models.CharField(max_length=200, default="none")
    # problem=models.CharField(max_length=200, default="none")
    # time=models.FloatField(null=True, blank=True, default=0.0)
    # pic=models.ImageField(upload_to="image")

    def __str__(self):
        return self.screen_id

class Result(models.Model):
    
    #id정보
    result_id = models.AutoField(primary_key=True)
    coder_id=models.CharField(max_length=200, default="kmz")
    screen_id=models.CharField(max_length=200, default="none")
    #problem_id=models.CharField(max_length=200, default="none")

    #timestamp
    result_time=models.CharField(max_length=200, default="0000")#timestamp

    #주요정보
    game_name=models.CharField(max_length=200,default="MangoShop")
    gaming=models.IntegerField(default=-1)
    gaming_type=models.TextField(default="non gaming")

    #old
    #rapid_guessing=models.IntegerField(default=-1)
    #system_abuse=models.IntegerField(default=-1)
    

    def __str__(self):
        return str(self.screen_id)

class Coder(models.Model):

    coder_id=models.CharField(max_length=200, primary_key=True, default='kmz_MangoShop') #'kmz_MangoShop'
    recent_screen_id=models.CharField(max_length=200, default="none")
    created=models.CharField(max_length=200, default="0000")

    def __str__(self):
        return self.coder_id