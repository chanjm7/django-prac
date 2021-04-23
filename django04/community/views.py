from django.db.models.base import Model
from community import models
from django.shortcuts import render
# Create your views here.
def index(request):
    categories = models.Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context)

def article(request, category_pk):
    articles = models.Article.objects.filter(category_num = category_pk)
    context = {
        'articles': articles
    }
    return render(request, 'article.html', context)

def detail(request, article_text):
    context = {'text' : article_text}
    return render(request, 'detail.html', context)