from django.conf.urls import include, url
from django.contrib import admin
from weather import urls as weatherurls
urlpatterns=[url(r'^weather/',include(weatherurls)),url(r'^admin/',admin.site.urls),]
