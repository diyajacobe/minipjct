# Generated by Django 4.1.3 on 2022-11-14 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house_product',
            name='place',
        ),
        migrations.RemoveField(
            model_name='house_product',
            name='state',
        ),
        migrations.RemoveField(
            model_name='house_product',
            name='street',
        ),
    ]
