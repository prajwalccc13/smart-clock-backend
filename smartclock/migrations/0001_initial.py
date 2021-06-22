# Generated by Django 3.2.4 on 2021-06-22 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('status', models.BooleanField(choices=[(True, 'On'), (False, 'Off')], default=False, verbose_name='Device status')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartclock.room')),
            ],
        ),
    ]
