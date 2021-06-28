from django.shortcuts import render, HttpResponse, redirect

import random

def index(request):
    
    if 'number' not in request.session:
        request.session['number'] = random.randint(1,100)
    if 'result' not in request.session:
        request.session['result'] = 'Guess a number'
    if 'guess' not in request.session:
        request.session['guess'] = '...'
    if 'count' not in request.session:
        request.session['count'] = 0
    
    context = {
        'result': request.session['result'],
        'guess': request.session['guess'],
        'count': request.session['count']
    }
    return render(request, 'index.html', context)

def process(request):
    if request.POST['guess'] == '':
        return redirect('/')
    
    request.session['guess'] = int(request.POST['guess'])
    guess = int(request.POST['guess'])
    num = request.session['number']
    count = int(request.session['count'])
    
    print('this is the guess', guess)
    print('this is the num', num)
    
    if guess < 0 or guess > 100:
        result = 'Number must be between 1 and 100'
    
    elif guess == num:
        result = 'Correct!'
    
    elif guess > num and guess < 101:
        result = 'Try a lower number'
    
    elif guess < num and guess > 0:
        result = 'Try a higher number'

    if guess != num:
        count = count + 1
        request.session['count'] = count
    
    print('this is the result', result)
    request.session['result'] = result
    
    
    return redirect('/')

def clear(request):
    request.session.clear()
    
    return redirect('/')


