from django.contrib import admin

# Register your models here.
from .models import Screen,Result
admin.site.register(Screen)
admin.site.register(Result)