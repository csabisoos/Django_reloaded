# Generated by Django 3.2.12 on 2022-03-11 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kerdes',
            name='hulyeseg',
        ),
    ]
