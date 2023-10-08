from django.shortcuts import render, redirect
from categories.models import Categories
from courses.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
# Create your views here.


def index(request):
    categories = Categories.objects.all()
    return render(request, "index.html", {
        "objects": categories
    })
