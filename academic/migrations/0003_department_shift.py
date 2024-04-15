# Generated by Django 4.2.1 on 2024-04-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_curriculumsubject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the Department', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the Shift', max_length=100)),
            ],
        ),
    ]
