# Generated by Django 2.2.5 on 2020-03-03 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_auto_20200302_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exams',
            name='timeDuration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
