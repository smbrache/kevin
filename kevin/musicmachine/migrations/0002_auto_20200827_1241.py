# Generated by Django 2.2.14 on 2020-08-27 19:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicmachine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='tempo',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(300)], verbose_name='Tempo'),
        ),
    ]
