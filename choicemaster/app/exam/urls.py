from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^adminreport/$', views.report, name='report'),
    url(r'^adminreport/(?P<question_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^adminreport/(?P<report_id>[0-9]+)/(?P<question_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^adminreport/(?P<report_id>[0-9]+)/(?P<question_id>[0-9]+)/(?P<choice_id>[0-9]+)/edited/$', views.edit_question, name='edit_question'),
    url(r'^create_exam/$', views.create_exam),
    url(r'^do/(?P<exam_id>[0-9]+)/(?P<question_id>[0-9]+)/$', views.doexam, name='doingexam'),
    url(r'^answer_result/(?P<exam_id>[0-9]+)/(?P<question_id>[0-9]+)/$', views.doexam, name='answer_result'),
    url(r'^something_went_wrong/', views.sth_wrong, name='wrong'),
]
