from django.shortcuts import render
from django.http import HttpResponse
from graphshool.models import GraphShoolDet, GraphShoolMain

def det(request):
	zagl = GraphShoolMain.objects.all()

	return render(request, 'graphshool/detail.html', {'det':det, 'zagl':zagl})
