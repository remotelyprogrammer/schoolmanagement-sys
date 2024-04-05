from django.db import models


class GradeLevel(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="The name of the grade level")
    order = models.PositiveIntegerField(help_text="The order in which the grade level appears")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class SchoolYear(models.Model):
    start_year = models.PositiveSmallIntegerField(help_text="The start year of the school year, e.g., 2024")
    end_year = models.PositiveSmallIntegerField(help_text="The end year of the school year, e.g., 2025")
    is_current = models.BooleanField(default=False, help_text="Indicates if this is the current school year")

    class Meta:
        ordering = ['-start_year']  # Orders the school years in descending order by start year
        unique_together = (('start_year', 'end_year'),)  # Ensures the combination of start and end year is unique

    def __str__(self):
        return f"{self.start_year}-{self.end_year}"

    def save(self, *args, **kwargs):
        if self.is_current:
            # Ensure no other SchoolYear is marked as current
            SchoolYear.objects.filter(is_current=True).update(is_current=False)
        super(SchoolYear, self).save(*args, **kwargs)


class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True, help_text="Unique code for the subject, e.g., MATH101")
    name = models.CharField(max_length=100, help_text="Name of the subject, e.g., Mathematics")
    description = models.TextField(blank=True, help_text="A brief description of the subject")

    def __str__(self):
        return f"{self.code} - {self.name}"


class Section(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Section Name")
    grade_level = models.ForeignKey(GradeLevel, related_name='section', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.grade_level} - {self.name}" 


class Curriculum(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the Curriculum")

    def __str__(self):
        return f"{self.name}" 