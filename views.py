from django.http import HttpResponse
from django.contrib.auth import logout,login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate


def index(request):
    return  HttpResponse("hello world")

def login_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        if(username == ""):return  HttpResponse("no username")
        if (password == ""): return HttpResponse("no password")
        user=authenticate(username=username,password=password)
        if(user is None):
            return HttpResponse("unauthorized")
        else:
            login(request, user)
            return redirect('/')
        return HttpResponse('your username is:' +username)
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        email=request.POST['email']
        if(username == ""):return  HttpResponse("no username")
        if (password == ""): return HttpResponse("no password")
        if (email == ""): return HttpResponse("no email")
        User.objects.create_user(username=username,password=password,email=email)
        user = authenticate(username=username, password=password)
        if (user is None):
            return HttpResponse("unauthorized")
        else:
            login(request,user)
            return redirect('/')

    return render(request,'register.html')



def dashboard(request):
    if not request.user.username=='admin':
        return HttpResponse("unauthorized")
    return HttpResponse("<h1>Dashboard</h1>")

def username(request):
    return HttpResponse("your username is: " +request.user.username )

def logout_user(request):
    logout(request)
    return HttpResponse("Successfully logged out")


"""@login_required(login_url='/login_user')
def edit_user(request):
    if request.method=='POST':
        user=request.user
        phone=request.POST['phone']
        address = request.POST['address']
        profile,created=Profile.objects.get_or_create(user=request,user)
        user.profile.phone=phone
        user.profile.address=address
        user.save()
    return render(request,'edituser.html')"""
