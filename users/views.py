from django.shortcuts import render, redirect

# Forms
from .forms import UserCreationForm, AuthenticationForm, UserUpdateForm, SetPasswordForm

# FOR LOGIN
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# MESSAGES
from django.contrib import messages
from .decorators import user_not_authenticated

# RESET PASSWORD
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .token import account_activation_token

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


@user_not_authenticated
def password_reset(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user_associated = get_user_model().objects.filter(Q(email=email)).first()
            if user_associated:
                subjet = "Password Reset request"
                message = render_to_string("password_reset_email.html", {
                    "user": user_associated,
                    "domain": get_current_site(request).domain,
                    "uid": urlsafe_base64_encode(force_bytes(user_associated.pk)),
                    "token": account_activation_token.make_token(user_associated),
                    "protocol": "https" if request.is_secure() else "http"
                })
                email = EmailMessage(subjet, message, to=[
                    user_associated.email
                ])
                if email.send():
                    messages.success(
                        request, "Check your email for reset password")
                    return redirect("home")
    else:
        form = PasswordResetForm()
    return render(request, "password_reset_form.html", {
        "form": form,
        "type": "reset"
    })


def password_reset_confirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Your password has been set, yo may go to signin")
                return redirect("home")
        else:
            form = SetPasswordForm(user)
        return render(request, "password_reset_form.html", {
            "form": form,
            "type": "confirm"
        })
    else:
        messages.error(request, "Link is expired")
        return redirect("home")
