from django.contrib import admin

# Register your models here.
from .models import Screen,Result,Coder
admin.site.register(Screen)
admin.site.register(Result)
admin.site.register(Coder)