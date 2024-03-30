from django.contrib import admin
from .models import GradeLevel, SchoolYear, Subject


admin.site.register(GradeLevel)
admin.site.register(SchoolYear)
admin.site.register(Subject)