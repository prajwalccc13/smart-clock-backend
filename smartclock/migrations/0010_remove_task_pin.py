# Generated by Django 3.2.4 on 2021-09-30 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartclock', '0009_alter_task_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='pin',
        ),
    ]
