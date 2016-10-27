from django.conf.urls import url

from app.exam import views

urlpatterns = [
        url(r'^form/$', views.Form),
        url(r'^upload/$', views.Upload),
]
