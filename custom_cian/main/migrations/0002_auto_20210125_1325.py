# Generated by Django 3.1.5 on 2021-01-25 13:10

from django.db import migrations, models


def fill_is_mortgage_available_field(apps, schema_editor):
    Realty = apps.get_model("main", "Realty")

    for r in Realty.objects.all():
        r.is_mortgage_available = False
        r.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realty',
            name='is_mortgage_available',
            field=models.BooleanField(verbose_name='Возможность ипотеки', null=True)
        ),
        migrations.RunPython(fill_is_mortgage_available_field),
        migrations.AlterField(
            model_name='realty',
            name='is_mortgage_available',
            field=models.BooleanField(verbose_name='Возможность ипотеки', blank=False)
        ),
    ]
