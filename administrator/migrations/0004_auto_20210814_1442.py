# Generated by Django 3.2.6 on 2021-08-14 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_remove_programskipoziv_rad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anketa',
            old_name='oblast',
            new_name='oblasti',
        ),
        migrations.RenameField(
            model_name='rad',
            old_name='oblast',
            new_name='oblasti',
        ),
    ]
