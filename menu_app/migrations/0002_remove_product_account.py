# Generated by Django 4.2.2 on 2023-06-14 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='account',
        ),
    ]
