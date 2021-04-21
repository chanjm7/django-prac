from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

students = ['이찬민', '이민찬', '찬민이', '민찬이']

def index(request):
    context = {
        'user_name': 'chan min'
    }
    return render(request, 'index.html', context)

def result(request):
    
    if request.method == 'POST':
        context = {'is_user_authenticated': False}
        if request.POST['username'] in students:
            context = {'is_user_authenticated': True}

    return render(request, 'result.html', context)