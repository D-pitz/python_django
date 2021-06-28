from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def login(request):
    return render(request, 'login.html')

def create_user(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_pw
    )
    messages.info(request, 'Account was successfully created ')  
    return redirect('/')

def user_login(request):
    try:
        user = User.objects.get(email = request.POST['email'])
    except:
        messages.error(request, 'This email does not exist')
        return redirect('/')
    
    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, 'Password Incorrect')
        return redirect('/')
    request.session['user_id'] = user.id
    request.session['user_email'] = user.email
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')


    
