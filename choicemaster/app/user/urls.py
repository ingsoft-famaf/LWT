from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from app.user.views import RegisterUser

urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'login.html', 'redirect_authenticated_user': True}, name='login'),
    url(r'^register/', RegisterUser.as_view(), name="register"),
    url(r'^logout/', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]
