# Generated by Django 3.2.4 on 2021-09-30 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartclock', '0007_automatedtask_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartclock.device'),
        ),
    ]
