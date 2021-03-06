"""formiruem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from formiruem.views import index

urlpatterns = [
    url(r'^$', index, name='index'), 
	url(r'^admin/', admin.site.urls),
	url(r'^designshool/', include('designshool.urls')),
	url(r'^pcshool/', include('pcshool.urls')),
    url(r'^graphshool/', include('graphshool.urls')),
    url(r'^abrshool/', include('abrshool.urls')),
    url(r'^buhshool/', include('buhshool.urls')),
    url(r'^langshool/', include('langshool.urls')),
    url(r'^indshool/', include('indshool.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^summernote/', include('django_summernote.urls')),

]
