from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def article_list(request):
    articles = BlogPost.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(BlogPost, pk=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

