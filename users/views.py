from django.shortcuts import render, redirect

# Forms
from .forms import UserCreationForm, AuthenticationForm, UserUpdateForm


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import user_not_authenticated
from django.contrib.auth import get_user_model

# Create your views here.


@user_not_authenticated
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("signin")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {
        "form": form
    })


@user_not_authenticated
def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {user.username} :D")
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "signin.html", {
        "form": form
    })


@login_required(login_url="signin")
def close_session(request):
    logout(request)
    messages.info(request, "You have logged out")
    return redirect("home")


@login_required(login_url="signin")
def profile(request, username, id):
    if request.method == "POST":
        user = request.user
        print(user)
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, "Profile has been updated")
            # El request.path, sirve para hacer un redireccionamiento a la misma vista
            return redirect(request.path)
        else:
            for error in list(form.errors.values()).pop():
                messages.error(request, error)
    user = get_user_model().objects.filter(id=id).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(request, "profile.html", {
            "form": form
        })
