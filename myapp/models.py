from django.db import models

#https://ssungkang.tistory.com/entry/Django-media-%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C%ED%95%98%EA%B8%B0
# Create your models here.
class Screen(models.Model):
    screen_id=models.IntegerField( primary_key=True)
    
    user=models.CharField(max_length=200, default="none")
    day_problem=models.CharField(max_length=200, default="none")
    day=models.CharField(max_length=200, default="none")
    problem=models.CharField(max_length=200, default="none")
    time=models.FloatField(null=True, blank=True, default=0.0)
    pic=models.ImageField(upload_to="image")
    
    gaming=models.IntegerField(default=-1)
    gaming_type=models.TextField(default="non gaming")
    

    def __str__(self):
        return str(self.screen_id)