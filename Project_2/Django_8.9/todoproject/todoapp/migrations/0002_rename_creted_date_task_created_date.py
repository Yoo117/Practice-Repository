# Generated by Django 5.1 on 2024-08-09 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='creted_date',
            new_name='created_date',
        ),
    ]
