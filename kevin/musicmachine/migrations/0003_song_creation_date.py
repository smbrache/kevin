# Generated by Django 2.2.14 on 2020-08-27 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicmachine', '0002_auto_20200827_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='creation_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
