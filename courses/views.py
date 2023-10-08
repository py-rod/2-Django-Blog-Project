from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article
# Create your views here.


def articles(request, slug: str, title: str):
    article = Article.objects.filter(series__slug=slug).all()
    paginator = Paginator(article, 20)
    page = request.GET.get("page")
    paged_articles = paginator.get_page(page)
    category_title = Article.objects.filter(series__slug=slug).first()
    return render(request, "articles.html", {
        "objects": paged_articles,
        "category_title": category_title
    })


def content_article(request, slug: str, article_slug: str, title1: str, title2: str):
    content = Article.objects.filter(
        series__slug=slug, article_slug=article_slug).first()
    return render(request, "content_article.html", {
        "object": content
    })


def search_view(request):
    search_query = request.GET.get("q", "")
    if search_query != "":
        articles = Article.objects.filter(title__icontains=search_query).all()
        paginator = Paginator(articles, 20)
        page = request.GET.get("page")
        paged_articles = paginator.get_page(page)
        return render(request, "search.html", {
            "objects": paged_articles
        })
    else:
        return render(request, "search.html", {
            "objects": False
        })
