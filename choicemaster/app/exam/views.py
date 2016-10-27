from django.shortcuts import render, redirect
from .models import Report, Question
from django.contrib.auth.decorators import login_required
from .forms import EditForm
# Create your views here.

@login_required
def report(request):
    if request.user.is_superuser:
        report_list = Report.objects.all()
        context = {'report_list': report_list}
        return render(request, 'report.html', context)
    else:
        return redirect('/')

@login_required
def delete(request, question_id):
    if request.user.is_superuser:
        question = Question.objects.get(id = question_id)
        question.delete()
        return redirect('/exam/adminreport')
    else:
        return redirect('/')

@login_required
def edit(request, question_id, report_id):
    if request.user.is_superuser:
        question = Question.objects.get(id = question_id)
        report = Report.objects.get(id = report_id)
        context = {'question': question, 'report': report}
        return render(request, 'edit.html', context)
    else:
        return redirect('/')

@login_required
def edit_question(request, question_id, report_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                q = Question.objects.get(id = question_id)
                text = form.cleaned_data['edit_text']
                q.question_text = text
                q.save()
                r = Report.objects.get(id = report_id)
                r.delete()
                return redirect('/exam/adminreport')
        else:
            form = EditForm()
    else:
        return redirect('/')
    return redirect('/exam/adminreport')


