from django.shortcuts import render
from django.http import HttpResponse
from pcshool.models import PCShoolMain

def det(request):
	zagl = PCShoolMain.objects.all()
	return render(request, 'pcshool/detail.html', {'det':det, 'zagl':zagl})
