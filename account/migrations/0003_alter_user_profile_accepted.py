# Generated by Django 3.2.6 on 2021-08-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_profile_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_accepted',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
