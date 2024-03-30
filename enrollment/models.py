from django.db import models
from student.models import Student
from django.utils import timezone
from django.db.models import Max
from academic.models import SchoolYear, GradeLevel


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    school_year = models.ForeignKey(SchoolYear, on_delete=models.PROTECT, related_name='enrollments')
    enrollment_number = models.IntegerField()
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.SET_NULL, null=True, blank=True, related_name='enrollments')
    enrollment_date = models.DateField(default=timezone.now)

    class Meta:
        unique_together = (('school_year', 'enrollment_number'),)

    @property
    def school_year_reg(self):
        # Extract the last two digits of the start and end years
        year_prefix = f"{str(self.school_year.start_year)[-2:]}{str(self.school_year.end_year)[-2:]}"
        return f"{year_prefix}-{self.enrollment_number:07d}"

    def __str__(self):
        # Same logic in the __str__ method
        year_prefix = f"{str(self.school_year.start_year)[-2:]}{str(self.school_year.end_year)[-2:]}"
        return f"{year_prefix}-{self.enrollment_number:07d}"

    def save(self, *args, **kwargs):
        # If this is a new enrollment (i.e., it doesn't have an ID yet)
        if not self.id:
            # Get the current maximum enrollment number for the school year
            current_max = Enrollment.objects.filter(school_year=self.school_year).aggregate(Max('enrollment_number'))['enrollment_number__max']
            
            # If there are no enrollments yet for the school year, start at 1. Otherwise, increment by 1.
            self.enrollment_number = 1 if current_max is None else current_max + 1
        
        super(Enrollment, self).save(*args, **kwargs)