from django.contrib import admin
from .models import GradeLevel, SchoolYear, Subject, Section, Curriculum, CurriculumSubject


admin.site.register(GradeLevel)
admin.site.register(SchoolYear)
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(Curriculum)
admin.site.register(CurriculumSubject)