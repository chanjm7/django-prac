from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    if 'include_space' in request.POST:
        context = {'result':len(request.POST['text'])}
    else:
        context = {'result':len(request.POST['text'].replace(" ", ""))}
    return render(request, 'result.html', context)