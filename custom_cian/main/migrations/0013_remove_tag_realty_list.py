# Generated by Django 3.1.5 on 2021-03-01 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210301_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='realty_list',
        ),
    ]