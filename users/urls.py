from django.urls import path
from . import views


urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("logout", views.close_session, name="logout"),
    path("profile/<username>=<id>", views.profile, name="profile"),
    path("password_reset", views.password_reset, name="password_reset"),
    path("reset/<uidb64>/<token>", views.password_reset_confirm,
         name="password_reset_confirm")
]
