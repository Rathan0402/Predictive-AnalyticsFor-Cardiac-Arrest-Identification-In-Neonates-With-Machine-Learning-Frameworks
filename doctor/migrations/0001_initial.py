# Generated by Django 5.0.1 on 2024-02-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('passwd', models.CharField(max_length=40)),
                ('cwpasswd', models.CharField(max_length=40)),
                ('mobileno', models.CharField(default='', max_length=50)),
                ('specialization', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='', max_length=40)),
            ],
            options={
                'db_table': 'doctorregister',
            },
        ),
    ]
