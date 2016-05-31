from django.conf.urls import url
from langshool import views

urlpatterns = [
	url(r'^$', views.det, name='langshool'),
]