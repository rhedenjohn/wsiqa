# Generated by Django 2.2.10 on 2020-03-05 03:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0001_initial'),
        ('exam', '0011_auto_20200304_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_Date', models.DateField(default=datetime.datetime.now)),
                ('expire_Date', models.DateField(default=datetime.datetime.now)),
                ('score', models.IntegerField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ApplicantExam_applicant', to='applicants.Applicants')),
                ('exam', models.ManyToManyField(related_name='ApplicantExam_exam', to='exam.Exams')),
            ],
        ),
    ]
