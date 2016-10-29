from django import forms

class EditForm(forms.Form):
    edit_text = forms.CharField(label='Edit', max_length=300)

class ExamForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    topic = forms.CharField(max_length=100, required=True)
    timer = forms.IntegerField(required=True)
    number_of_questions = forms.IntegerField(required=True)
