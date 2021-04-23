from django.contrib import admin
from .models import MyClass, MyStudent

# Register your models here.
admin.site.register(MyClass)
admin.site.register(MyStudent)
