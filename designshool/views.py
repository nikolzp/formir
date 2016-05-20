from django.shortcuts import render
from django.http import HttpResponse
from designshool.models import DesignShool


def det(request):
	resp = DesignShool.objects.all()
	li = []
	for a in DesignShool.objects.get().name_course(id=id+1):
		li.append(a)
	return render(request, 'designshool/detail.html', {'resp':resp, 'li':li})