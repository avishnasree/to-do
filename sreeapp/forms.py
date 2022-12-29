from django import forms

from sreeapp.models import Todo



class DateInput(forms.DateInput):
    input_type = 'date'




class Todoform(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model=Todo
        fields=('content','date')
