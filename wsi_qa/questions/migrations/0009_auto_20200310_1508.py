# Generated by Django 2.2.5 on 2020-03-10 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20200310_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]