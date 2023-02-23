# Generated by Django 4.1.3 on 2022-11-14 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_house_product_is_featured_house_product_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike_product',
            name='city',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bike_product',
            name='location',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bike_product',
            name='state',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='car_product',
            name='city',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='car_product',
            name='location',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='car_product',
            name='state',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='furn_product',
            name='city',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='furn_product',
            name='location',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='furn_product',
            name='state',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='other_product',
            name='city',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='other_product',
            name='location',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='other_product',
            name='state',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='house_product',
            name='city',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='house_product',
            name='location',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='house_product',
            name='state',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True),
        ),
    ]