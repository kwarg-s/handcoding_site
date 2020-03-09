from django.db import models

#https://ssungkang.tistory.com/entry/Django-media-%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C%ED%95%98%EA%B8%B0
# Create your models here.
class Screen(models.Model):
    title=models.CharField(max_length=200)
    screen_id=models.IntegerField( primary_key=True)
    pic=models.ImageField(upload_to="image")
    gaming=models.IntegerField(default=0)
    gaming_type=models.TextField(default="non gaming")


    def __str__(self):
        return self.title