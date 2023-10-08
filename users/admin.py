from django.contrib import admin
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff",
                    "is_superuser", "is_active")
    list_display_links = ("id", "username", "email")
    list_filter = ("is_staff", "is_superuser", "is_active")
    list_per_page = 20
    search_fields = ("id", "username", "email", "first_name", "last_name")
    ordering = ("-id",)
