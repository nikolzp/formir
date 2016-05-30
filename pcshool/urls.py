from django.conf.urls import url
from pcshool import views

urlpatterns = [
	url(r'^$', views.det, name='pcshool'),
]