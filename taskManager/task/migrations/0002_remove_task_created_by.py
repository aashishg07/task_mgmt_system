# Generated by Django 4.2.1 on 2023-05-04 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_by',
        ),
    ]