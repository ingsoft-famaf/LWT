from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    subject = models.CharField(max_length=100, default='Sin materia')
    topic = models.CharField(max_length=100, default ='Sin tema')
    question_text = models.CharField(max_length=200)
    is_reported = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

    def text(self):
        return self.question_text

    def question_is_reported(self):
        return self.is_reported

    def set_reported(self):
        report = Report.object.get(question = self)
        if report is not None:
            self.is_reported = True
        else:
            self.is_reported = False

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

class Report(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    report_text = models.CharField(max_length=300)

    def __str__(self):
        return self.report_text

    def text(self):
        return self.report_text

    def question_reported(self):
        return self.question
