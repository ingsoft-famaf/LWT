from django import forms

class EditForm(forms.Form):
    edit_text = forms.CharField(label='Edit', max_length=300)
