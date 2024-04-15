from django.contrib import admin
from .models import GradeLevel, SchoolYear, Subject, Section, Curriculum, CurriculumSubject, Department, Shift, SchoolClass,\
		ClassStudent, Instructor


admin.site.register(GradeLevel)
admin.site.register(SchoolYear)
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(Curriculum)
admin.site.register(CurriculumSubject)
admin.site.register(Shift)
admin.site.register(Department)
admin.site.register(SchoolClass)
admin.site.register(ClassStudent)
admin.site.register(Instructor)