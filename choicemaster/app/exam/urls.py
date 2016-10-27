from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^adminreport/$', views.report, name='report'),
]
