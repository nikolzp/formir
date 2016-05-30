from django.conf.urls import url
from graphshool import views

urlpatterns = [
	url(r'^$', views.det, name='graphshool'),
]