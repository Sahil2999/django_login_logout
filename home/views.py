from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect ("/login")
    return render(request, 'index.html')


def loginUser(request):
    if request.method=="POST":
        Username = request.POST.get('Username')
        password = request.POST.get('password')
        user = authenticate(username=Username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            return render(request, 'login.html')


    return render(request, 'login.html')
def logoutUser(request):
    logout(request)
    return redirect ("/login")