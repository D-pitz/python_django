from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'visits' not in request.session:
        request.session['visits'] = 0
    
    request.session['visits'] += 1

    if 'counter_1' not in request.session:
        request.session['counter_1'] = 0
    if 'counter_2' not in request.session:
        request.session['counter_2'] = 0
    if 'counter_3' not in request.session:
        request.session['counter_3'] = 0

    return render(request, 'index.html')

def counter(request, counter_id):
    
    if counter_id == 1:
        request.session['counter_1'] += 1
    elif counter_id == 2:
        request.session['counter_2'] += 1
    elif counter_id == 3:
        request.session['counter_3'] += 1
    
    return redirect('/')

def destroy_session(request):
    del request.session['visits']
    del request.session['counter_1']
    del request.session['counter_2']
    del request.session['counter_3']
    return redirect('/')

    


