from django.shortcuts import render
from django.http import HttpResponse
from buhshool.models import BuhShoolDet, BuhShoolMain

def det(request):
	zagl = BuhShoolMain.objects.all()

	return render(request, 'buhshool/detail.html', {'det':det, 'zagl':zagl})
