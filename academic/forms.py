from django import forms
from .models import SchoolYear, GradeLevel, Subject, Section, Curriculum


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


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('__all__')


class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ('__all__')
        