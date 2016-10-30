from django.conf.urls import url

from app.xmlparsing import views

urlpatterns = [
        url(r'^form/$', views.Form),
        url(r'^parse/$', views.Parse),
        url(r'^something_went_wrong/$', views.Sth_wrong_admin),
        url(r'^success/$', views.Success),
]
