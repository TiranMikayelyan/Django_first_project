# Generated by Django 5.0 on 2023-12-09 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='pname',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='text',
        ),
    ]