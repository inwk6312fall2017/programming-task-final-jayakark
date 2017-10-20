from django.conf.urls import url
from .views import homeview
urlpatterns = [url(r'^$',homeview.as_view(),name='home'),]

