# Generated by Django 3.1.1 on 2022-08-04 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakeryItem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
