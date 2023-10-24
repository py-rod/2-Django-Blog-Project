from django.shortcuts import render, redirect
from .models import Categories
from .forms import NewCategoryForm, UpdateCategory
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .decorators import user_is_superuser
from django.contrib import messages
# Create your views here.


def all_categories(request):
    categories = Categories.objects.all()
    paginator = Paginator(categories, 10)
    page = request.GET.get("page")
    paged_categories = paginator.get_page(page)
    return render(request, "all_categories.html", {
        "categories": paged_categories
    })


@user_is_superuser
def create_new_category(request):
    if request.method == "POST":
        form = NewCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NewCategoryForm()

    return render(request, "new_category.html", {
        "form": form,
        "type": "create"
    })


@user_is_superuser
def delete_category(request, title, slug):
    category = Categories.objects.filter(title=title, slug=slug)
    category.delete()
    messages.success(request, "The category has been delete")
    return redirect("all_categories")


@user_is_superuser
def update_category(request, title, slug):
    category = Categories.objects.filter(title=title, slug=slug).first()
    if request.method == "POST":
        form = UpdateCategory(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "The category has been updated :D")
            return redirect("all_categories")
    else:
        form = UpdateCategory(instance=category)
    return render(request, "new_category.html", {
        "form": form,
        "category": category,
        "type": "update"
    })
