from django.conf.urls import url, include
from django.contrib import admin


from app.register.views import RegisterUser

urlpatterns = [
    url(r'^$', RegisterUser.as_view(), name="register")

]
