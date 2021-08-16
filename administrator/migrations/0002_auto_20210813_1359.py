# Generated by Django 3.2.6 on 2021-08-13 11:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anketa',
            name='naziv',
            field=models.CharField(max_length=125, unique=True),
        ),
        migrations.AlterField(
            model_name='anketapitanje',
            name='ponudjeni_odgovor',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'Slazem se'), (1, 'Ne slazem se'), (2, 'Ne znam')], null=True),
        ),
        migrations.AlterField(
            model_name='rad',
            name='godina',
            field=models.PositiveIntegerField(help_text='Use the following format: YYYY', validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]),
        ),
    ]
