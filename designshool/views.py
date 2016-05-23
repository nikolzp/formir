from django.shortcuts import render
from django.http import HttpResponse
from designshool.models import DesignShool


def det(request):
	resp = DesignShool.objects.all()
	return render(request, 'designshool/detail.html', {'resp':resp})

def zagl(request):
	res = DesignShool.objects.all()
	li = res.get(id=2)
	return render(request, 'designshool/detail.html', {'li':li})