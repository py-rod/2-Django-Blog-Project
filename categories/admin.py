from django.contrib import admin
from .models import Categories
# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    fields = ["title", "bg_color",
              "author", "image", "created", "modified"]
    list_display = ("id", "title", "author", "created")
    list_display_links = ("id", "title")
    list_per_page = 20
    search_fields = ("id", "title")
    ordering = ("-id",)
    readonly_fields = ("created", "modified")
