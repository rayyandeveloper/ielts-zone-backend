# Generated by Django 5.0.6 on 2024-07-05 06:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_exam_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
