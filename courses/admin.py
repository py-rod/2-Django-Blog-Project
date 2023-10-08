from django.contrib import admin
from .models import Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ["title", "series", "author", "image",
              "description", "content", "modified"]
    list_display = ("id", "title", "series", "author")
    list_display_links = ("id", "title", )
    list_filter = ("series", )
    list_per_page = 20
    search_fields = ("id", "title")
    ordering = ("-id",)
