from django.shortcuts import render, HttpResponse, redirect
import random

def home(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'act' not in request.session:
        request.session['act'] = []
    context = {
        'gold': request.session['gold'],
        'act': request.session['act']
    }
    return render(request, 'home.html', context)

def process_gold(request):

    if request.POST['click'] == 'farm':
        x = random.randint(10,20)
        request.session['gold'] += x
        request.session['act'].append(f'You went to the farm and left with {x} gold')
    elif request.POST['click'] == 'cave':
        x = random.randint(5,10)
        request.session['gold'] += x
        request.session['act'].append(f'You went to the cave and left with {x} gold')
    elif request.POST['click'] == 'house':
        x = random.randint(2,5)
        request.session['gold'] += x
        request.session['act'].append(f'You went to the house and left with {x} gold')
    elif request.POST['click'] == 'casino':
        x = random.randint(-50,50)
        request.session['gold'] += x
        request.session['act'].append(f'You went to the casino and left with {x} gold')
    return redirect('/')

def clear(request):
    request.session.clear()
    
    return redirect('/')
