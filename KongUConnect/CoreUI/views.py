from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request): return render(request, 'home.html')

def authenticator(request):
    if request.method == "POST":
        userauth = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if userauth: 
            login(request, userauth)
            return render(request, 'login.html', {'LoginSuccess': True})
        else: return render(request, 'login.html', {'WrongUsernameOrPwd': True})
    else: logout(request)
# Create your views here.
