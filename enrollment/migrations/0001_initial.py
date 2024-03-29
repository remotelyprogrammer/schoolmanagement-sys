# Generated by Django 4.2.1 on 2024-03-29 14:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0005_alter_address_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the grade level', max_length=50, unique=True)),
                ('order', models.PositiveIntegerField(help_text='The order in which the grade level appears')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Unique code for the subject, e.g., MATH101', max_length=10, unique=True)),
                ('name', models.CharField(help_text='Name of the subject, e.g., Mathematics', max_length=100)),
                ('description', models.TextField(blank=True, help_text='A brief description of the subject')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.PositiveSmallIntegerField(help_text='The start year of the school year, e.g., 2024')),
                ('end_year', models.PositiveSmallIntegerField(help_text='The end year of the school year, e.g., 2025')),
                ('is_current', models.BooleanField(default=False, help_text='Indicates if this is the current school year')),
            ],
            options={
                'ordering': ['-start_year'],
                'unique_together': {('start_year', 'end_year')},
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_number', models.IntegerField()),
                ('enrollment_date', models.DateField(default=django.utils.timezone.now)),
                ('grade_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enrollments', to='enrollment.gradelevel')),
                ('school_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='enrollments', to='enrollment.schoolyear')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='student.student')),
            ],
            options={
                'unique_together': {('school_year', 'enrollment_number')},
            },
        ),
    ]
