# Generated by Django 2.2.2 on 2019-06-05 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_content', models.TextField()),
                ('post_published', models.DateTimeField(default=datetime.datetime(2019, 6, 5, 15, 2, 58, 361078), verbose_name='date published')),
                ('post_slug', models.CharField(default=1, max_length=200)),
            ],
        ),
    ]
