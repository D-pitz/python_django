from django.shortcuts import render, redirect
from app_login.models import User
from app_wall.models import Message, Comment
from django.contrib import messages

def the_wall(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('/')
    
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'posts': Message.objects.all().order_by('-created_at'),
        'comments': Comment.objects.all().order_by('created_at')
    }
    return render(request, 'the_wall.html', context)

def post_message(request):
    errors = Message.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    Message.objects.create(
        message= request.POST['message'],
        user= User.objects.get(id=request.session['user_id'])
    )
    return redirect('/wall')

def post_comment(request, post_id):
    errors = Comment.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    Comment.objects.create(
        comment= request.POST['comment'],
        user=User.objects.get(id=request.session['user_id']),
        message= Message.objects.get(id=post_id)
    )
    return redirect('/wall')

def destroy_message(request, post_id):
    message_to_delete= Message.objects.get(id=post_id)
    message_to_delete.delete()
    return redirect('/wall')

def destroy_comment(request, comment_id):
    comment_to_delete= Comment.objects.get(id=comment_id)
    comment_to_delete.delete()
    return redirect('/wall')



