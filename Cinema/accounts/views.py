from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not all((username, email, password1, password2)):
            raise ValueError("An intentional error occurred!")

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1
                )
                user.save()
                messages.success(request, "Account created successfully")
                return redirect("login")
        else:
            messages.error(request, "Passwords do not match")
    return render(request, "accounts/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("rooms")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("rooms")
