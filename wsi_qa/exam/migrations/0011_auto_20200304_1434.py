# Generated by Django 2.2.5 on 2020-03-04 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_auto_20200304_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exams',
            name='timeDuration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
