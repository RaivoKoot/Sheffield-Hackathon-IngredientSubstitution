# Generated by Django 2.1.2 on 2018-10-27 20:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181027_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 27, 20, 33, 41, 733991, tzinfo=utc)),
        ),
    ]