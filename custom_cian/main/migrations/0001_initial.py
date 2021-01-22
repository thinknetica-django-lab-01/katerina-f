# Generated by Django 3.1.5 on 2021-01-22 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('space', models.IntegerField(verbose_name='Площадь')),
                ('published_at', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, verbose_name='Ссылка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name': 'Объект недвижимости',
                'verbose_name_plural': 'Объекты недвижимости',
                'ordering': ['-published_at'],
            },
        ),
        migrations.CreateModel(
            name='Saller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('registered_at', models.DateField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Продавец',
                'verbose_name_plural': 'Продавцы',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, verbose_name='Ссылка')),
                ('realty_list', models.ManyToManyField(related_name='realty_list', to='main.Realty')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='realty',
            name='saller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.saller'),
        ),
        migrations.AddField(
            model_name='realty',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='main.Tag'),
        ),
    ]
