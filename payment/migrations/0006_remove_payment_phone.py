# Generated by Django 2.2.1 on 2019-11-13 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20191113_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='phone',
        ),
    ]