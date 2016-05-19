from django.shortcuts import render
from django.http import HttpResponse
from designshool.models import DesignShool


def det(request):
	resp = DesignShool.objects.all()
	return render(request, 'detail.html', {'resp':resp})