from django.shortcuts import render
from .models import Report, Question
# Create your views here.
def report(request):
    report_list = Report.objects.all()
    question_list = []
    for report in report_list:
        question = Question.objects.get(id = report.question.id)
        question_list.append(question)
    print(question_list)
    context = {'report_list': report_list, 'question_list': question_list}
    return render(request, 'report.html', context)
