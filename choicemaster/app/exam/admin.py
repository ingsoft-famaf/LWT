from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice, Report, ExamModel, Selected_question

admin.site.register(Question)

admin.site.register(Choice)

admin.site.register(Report)

admin.site.register(ExamModel)

admin.site.register(Selected_question)
