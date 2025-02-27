from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_form(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    form = UserCreationForm()
    context = {"form": form, "form_title": "Register"}
    return render(request=request, template_name="form.html", context=context)


def login_form(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect("/")
            else:
                print("User not found")
    form = AuthenticationForm()
    context = {"form": form, "form_title": "Login"}
    return render(request, "form.html", context=context)


def logout_form(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")


def home(request):
    return render(request, "base.html")
