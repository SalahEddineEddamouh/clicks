# Generated by Django 4.2.4 on 2023-08-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='market',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='objectif',
            field=models.CharField(max_length=255),
        ),
    ]
