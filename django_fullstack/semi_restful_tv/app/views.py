from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from app.models import Show

def toshow(request):
    return redirect('/shows')

def shows(request):
    context = {
        'show': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new_show(request):
    return render(request, 'new_show.html')

def create_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    
    else:
        new_show =Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        desc = request.POST['desc'],
        )
        id = new_show.id
        return redirect(f'/shows/{id}')

def display_show(request, show_id):
    context = {
        'this_show': Show.objects.get(id=show_id)
    }
    return render(request, 'display_show.html', context)

def destroy(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/shows')

def edit(request, show_id):
    context = {
        'this_show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    
    else:
        update_show = Show.objects.get(id=show_id)
        update_show.title = request.POST['title']
        update_show.network= request.POST['network']
        update_show.release_date= request.POST['release_date']
        update_show.desc= request.POST['desc']
        update_show.save()
        return redirect(f'/shows/{show_id}')



