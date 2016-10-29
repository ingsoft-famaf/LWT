from django.conf.urls import url

from app.xmlparsing import views

urlpatterns = [
        url(r'^form/$', views.Form),
        url(r'^parse/$', views.Parse),
]
