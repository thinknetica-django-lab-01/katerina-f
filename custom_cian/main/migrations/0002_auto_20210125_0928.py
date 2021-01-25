# Generated by Django 3.1.5 on 2021-01-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, max_length=100, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='slug',
            field=models.SlugField(editable=False, max_length=100, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(editable=False, max_length=100, unique=True, verbose_name='Ссылка'),
        ),
    ]
