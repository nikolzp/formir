from django.shortcuts import render
from django.http import HttpResponse
from designshool.models import DesignShoolDet, DesignShoolMain

def det(request):
	zagl = DesignShoolMain.objects.all()

	return render(request, 'designshool/detail.html', {'det':det, 'zagl':zagl})
