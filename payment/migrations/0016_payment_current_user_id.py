# Generated by Django 2.2.1 on 2019-10-14 10:49

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0015_auto_20191009_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='current_user_id',
            field=models.IntegerField(default=builtins.id),
        ),
    ]
