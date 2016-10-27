from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^adminreport/$', views.report, name='report'),
    url(r'^adminreport/(?P<question_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^adminreport/(?P<report_id>[0-9]+)/(?P<question_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^adminreport/(?P<report_id>[0-9]+)/(?P<question_id>[0-9]+)/edited/$', views.edit_question, name='edit_question'),
]
