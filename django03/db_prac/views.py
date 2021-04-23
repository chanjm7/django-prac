from db_prac.models import MyClass
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    classes = MyClass.objects.all()
    print(type(classes))
    context = {
        'classes': classes
    }
    return render(request, 'index.html', context)