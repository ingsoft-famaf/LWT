from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def home(request):
    if request.user.is_superuser:
        return render(request, 'home_admin.html')
    else:
        return render(request, 'home.html')


def init(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        return redirect('/accounts/login')

"""
modelo de xml
<materia>
    subject
  <pregunta>
    ¿ca?
    <resp1>r A</resp1>
    <resp2>r B</resp2>
    <resp3>r C</resp3>
  </pregunta>
    <pregunta2>
    ¿ser o no ser ?
    <resp1>r A</resp1>
    <resp2>r B</resp2>
    <resp3>r C</resp3>
  </pregunta2>
    <pregunta3>
    ¿a?
    <resp1>r A</resp1>
    <resp2>r B</resp2>
    <resp3>r C</resp3>
  </pregunta3>
</materia> 
"""
