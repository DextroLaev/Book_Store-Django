# Generated by Django 2.2.1 on 2019-09-20 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]