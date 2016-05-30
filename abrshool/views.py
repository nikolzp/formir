from django.shortcuts import render
from django.http import HttpResponse
from abrshool.models import AbrShoolDet, AbrShoolMain

def det(request):
	zagl = AbrShoolMain.objects.all()

	return render(request, 'abrshool/detail.html', {'det':det, 'zagl':zagl})
