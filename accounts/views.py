from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("home")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


class CustomLoginView(LoginView):

    template_name = "accounts/login.html"

    authentication_form = LoginForm


@login_required
def profile(request):

    return render(request, "accounts/profile.html")


def logout_view(request):

    logout(request)

    return redirect("home")