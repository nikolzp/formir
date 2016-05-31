from django.conf.urls import url
from indshool import views

urlpatterns = [
	url(r'^$', views.det, name='indshool'),
]