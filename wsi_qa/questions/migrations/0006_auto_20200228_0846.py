# Generated by Django 2.2.10 on 2020-02-28 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20200226_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='exam',
        ),
        migrations.AddField(
            model_name='questions',
            name='answer',
            field=models.ManyToManyField(to='questions.Answer'),
        ),
        migrations.AddField(
            model_name='questions',
            name='choice',
            field=models.ManyToManyField(to='questions.Choice'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='createdDate',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Created Date'),
        ),
    ]
