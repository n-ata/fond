# Generated by Django 3.2.6 on 2021-08-27 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0003_auto_20210827_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='goal',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='raised',
        ),
    ]
