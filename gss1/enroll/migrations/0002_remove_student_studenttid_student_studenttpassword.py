# Generated by Django 4.0.2 on 2022-05-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='studenttid',
        ),
        migrations.AddField(
            model_name='student',
            name='studenttpassword',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]