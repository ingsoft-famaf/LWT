from django.shortcuts import render, redirect
from .models import Report, Question, Choice, ExamModel, Selected_question
from django.contrib.auth.decorators import login_required
from .forms import EditForm, ExamForm
import random
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

@login_required
def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            topic = form.cleaned_data['topic']
            timer = form.cleaned_data['timer']
            nquestions = form.cleaned_data['number_of_questions']
            exam = ExamModel(subject=subject, topic=topic, time=timer, number_of_questions=nquestions)
            exam.save()
            question_list = Question.objects.filter(subject=subject, topic=topic)
            if len(question_list) >= nquestions:
                ran_questions = random.sample(question_list, nquestions)
                for q in ran_questions:
                    sq = Selected_question(question=q, exam=exam)
                    sq.save()
            else:
                return redirect('/exam/something_went_wrong')
            context = {'exam': exam, 'ran_questions': ran_questions}
            return render(request, 'doingexam.html', context)
        else:
            form = ExamForm()
            return render(request,'create_exam.html',{
            'form': form,
            })
    else:
        form = ExamForm()
        return render(request,'create_exam.html',{
        'form': form,
        })

@login_required
def doexam (request, exam_id, question_id):
    exam = ExamModel.objects.get(id=exam_id)
    if request.method == 'POST':
        if request.POST.get('report') is not None:
            q = Question.objects.get(id=question_id)
            sel_qs = Selected_question.objects.filter(exam=exam)
            report_text = request.POST['report']
            q = Question.objects.get(id=question_id)
            r = Report(question=q, report_text=report_text)
            r.save()
            if sel_qs.exists():
                ran_questions = []
                for sel_q in sel_qs:
                    ran_questions.append(sel_q.question)
                context = {'exam': exam, 'ran_questions': ran_questions}
                return render(request, 'doingexam.html', context)
            else:
                result = exam.final_result()
                nq = exam.nquestions()
                context = {'result': result, 'nq': nq}
                exam.delete()
                return render(request, 'result.html', context)
        else:
            question = Question.objects.get(id=question_id)
            sq = Selected_question.objects.get(exam= exam, question=question)
            sq.delete()
            choice_id = request.POST['choice']
            answer = Choice.objects.get(id=choice_id)
            if answer.correct():
                exam.correct()
                exam.save()
            context = {'exam': exam, 'question': question, 'answer': answer}
            return render(request, 'answer_result.html', context)
    else:
        sel_qs = Selected_question.objects.filter(exam=exam)
        if sel_qs.exists():
            ran_questions = []
            for sel_q in sel_qs:
                ran_questions.append(sel_q.question)
            context = {'exam': exam, 'ran_questions': ran_questions}
            return render(request, 'doingexam.html', context)
        else:
            result = exam.final_result()
            nq = exam.nquestions()
            context = {'result': result, 'nq': nq}
            exam.delete()
            return render(request, 'result.html', context)

@login_required
def sth_wrong(request):
    return render(request, 'sth_wrong.html')
