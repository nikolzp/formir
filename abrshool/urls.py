from django.conf.urls import url
from abrshool import views

urlpatterns = [
	url(r'^$', views.det, name='abrshool'),
]