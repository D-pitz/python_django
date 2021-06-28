from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'index.html')

def survey(request):
	print('Post Info ****************************************************')
	print(request.POST)
	context = {
		'name': request.POST['name'],
		'location': request.POST['location'],
		'language': request.POST['language'],
		'comment': request.POST['comment'],
		'codingdojo': request.POST['codingdojo'],
		'checkbox': request.POST.getlist('checkbox')
	}

	return render(request,'survey.html', context)
