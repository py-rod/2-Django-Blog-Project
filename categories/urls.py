from django.urls import path
from . import views


urlpatterns = [
    path("new_category", views.create_new_category, name="new_category"),
    path("all_categories", views.all_categories, name="all_categories"),
    path("<title>/<slug>/update", views.update_category, name="update_category"),
    path("<title>/<slug>/delete", views.delete_category, name="delete_category"),
]
