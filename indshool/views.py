from django.shortcuts import render
from django.http import HttpResponse
from indshool.models import IndShoolMain

def det(request):
	zagl = IndShoolMain.objects.all()

	return render(request, 'indshool/detail.html', {'det':det, 'zagl':zagl})
