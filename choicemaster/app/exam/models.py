from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    is_reported = False


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    is_correct = False


class Report(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    report_text = models.CharField(max_length=300)
