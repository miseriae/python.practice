# Generated by Django 2.2.2 on 2019-06-19 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 15, 27, 21, 805615), verbose_name='date published'),
        ),
    ]
