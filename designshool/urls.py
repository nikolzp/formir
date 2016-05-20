from django.conf.urls import url
from designshool import views

urlpatterns = [
	url(r'^$', views.det, name='detail'),
]