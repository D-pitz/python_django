from django.shortcuts import render, redirect
from .models import User

def home(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'home.html', context)

def create_user(request):
    User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        age = request.POST['age']
    )
    return redirect('/')