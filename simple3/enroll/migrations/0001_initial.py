# Generated by Django 4.0.2 on 2022-06-15 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_address', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=50)),
                ('Check_me_out', models.CharField(max_length=50)),
            ],
        ),
    ]
