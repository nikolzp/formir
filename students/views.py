from django.shortcuts import render

def add(request):
	a = 1
	return render(request, 'students/detail.html', {'a': a})