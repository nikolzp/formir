from django.shortcuts import render
from django.http import HttpResponse
from langshool.models import LangShoolDet, LangShoolMain

def det(request):
	zagl = LangShoolMain.objects.all()

	return render(request, 'langshool/detail.html', {'det':det, 'zagl':zagl})
