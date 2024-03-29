# Generated by Django 3.2.4 on 2021-09-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartclock', '0005_device_pin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('hour', models.IntegerField()),
                ('minute', models.IntegerField()),
                ('monday', models.BooleanField()),
                ('tuesday', models.BooleanField()),
                ('wednesday', models.BooleanField()),
                ('thursday', models.BooleanField()),
                ('friday', models.BooleanField()),
                ('saturday', models.BooleanField()),
                ('sunday', models.BooleanField()),
                ('active', models.BooleanField()),
            ],
        ),
    ]
