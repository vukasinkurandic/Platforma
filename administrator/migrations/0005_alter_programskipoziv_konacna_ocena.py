# Generated by Django 3.2.6 on 2021-08-14 12:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_auto_20210814_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programskipoziv',
            name='konacna_ocena',
            field=models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
