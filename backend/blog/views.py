from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


class ArticleList(ListView):
    template_name = 'blog/article_list'
    model = Article

    def get_queryset(self):
        return Article.objects.filter(status=True)

