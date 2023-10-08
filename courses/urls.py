from django.urls import path
from . import views


urlpatterns = [
    path("<title>/<slug>/", views.articles, name="articles"),
    path("<title1>/<slug>/<title2>/<article_slug>/",
         views.content_article, name="content_article"),

    path("search/", views.search_view, name="search"),
]
