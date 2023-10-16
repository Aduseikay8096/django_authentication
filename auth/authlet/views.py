from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Example view function that renders an HTML template
def index(request):
    return render(request, 'index.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2'] 
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exist')
                return redirect('register_user')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'Username Already Exist')
                return redirect('register_user')
            else:
                user = User.objects.create_user(username = username, email= email , password = password )
                user.save()
                return redirect('login_user')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register_user')
    else:
        return render(request, 'register_user.html')
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username , password= password )
        
        if user is not None:
            auth.login(request ,user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('login_user')
    return render(request, 'login_user.html')

def logout_user(request):
    auth.logout(request)
    return redirect('/')
