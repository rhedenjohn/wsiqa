# Generated by Django 2.2.10 on 2020-02-26 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20200226_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_choice', to='questions.Choice'),
        ),
    ]