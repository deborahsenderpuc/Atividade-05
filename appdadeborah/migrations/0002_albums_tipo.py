# Generated by Django 3.2.13 on 2023-09-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdadeborah', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='tipo',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Band')], default='', max_length=1),
        ),
    ]
