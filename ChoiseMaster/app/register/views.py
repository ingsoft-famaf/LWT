from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
#from django.core.urlresolver import reverse_lazy
from app.register.forms import RegisterForm
class RegisterUser(CreateView):
    models = User
    template_name = "register.html"
    form_class = RegisterForm
#   success_url = reverse_lazy(login)
