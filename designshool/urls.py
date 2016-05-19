from django.conf.urls import url
from designshool.views import det

urlpatterns = [
	url(r'^$', det, name='detail'),
]