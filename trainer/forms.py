from django import forms
from .models import Trainer, Subject

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['emp_id', 'name', 'email', 'phone', 'subjects']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple()
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['code', 'name', 'description']