from django.conf.urls import url
from buhshool import views

urlpatterns = [
	url(r'^$', views.det, name='buhshool'),
]