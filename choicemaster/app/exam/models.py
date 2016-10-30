from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=100, default='Type subject')
    topic = models.CharField(max_length=100, default ='Type topic')
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

    def correct(self):
        return self.is_correct

class Report(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    report_text = models.CharField(max_length=300)

    def __str__(self):
        return self.report_text

    def text(self):
        return self.report_text

    def question_reported(self):
        return self.question

class ExamModel(models.Model):
    subject = models.CharField(max_length=100, default='Type Subject')
    topic = models.CharField(max_length=100, default='Type Topic')
    time = models.IntegerField(default=0)
    number_of_questions = models.IntegerField(default=0)
    result = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

    def correct(self):
        self.result = self.result + 1

    def final_result(self):
        return self.result

    def nquestions(self):
        return self.number_of_questions

class Selected_question(models.Model):
    """Model for Selected_question"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
