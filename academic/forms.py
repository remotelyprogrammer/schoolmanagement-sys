from django import forms
from .models import SchoolYear, GradeLevel, Subject


class SchoolYearForm(forms.ModelForm):
    class Meta:
        model = SchoolYear
        fields = ('__all__')


class GradeLevelForm(forms.ModelForm):
    class Meta:
        model = GradeLevel
        fields = ('__all__')


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('__all__')
        