from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article
from .forms import ArticleForm, UpdateArticle
from django.contrib import messages
from .decorators import user_is_superuser
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


@user_is_superuser
def create_new_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Article has been created")
            return redirect("home")
    else:
        form = ArticleForm()

    return render(request, "new_article.html", {
        "form": form,
        "type": "create"
    })


@user_is_superuser
def update_article(request, title1, title2, slug, article_slug):
    article = Article.objects.filter(
        series__slug=slug, article_slug=article_slug).first()
    if request.method == "POST":
        form = UpdateArticle(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "The article has been update :D")
            return redirect(f"home")
    else:
        form = UpdateArticle(instance=article)
    return render(request, "new_article.html", {
        "form": form,
        "type": "update",
        "article": article
    })


@user_is_superuser
def delete_article(request, slug, article_slug, title1, title2):
    article = Article.objects.filter(
        series__slug=slug, article_slug=article_slug)
    article.delete()
    messages.success(request, "The article has been delete")
    return redirect("home")
