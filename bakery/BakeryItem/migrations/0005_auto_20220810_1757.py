# Generated by Django 3.1.1 on 2022-08-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakeryItem', '0004_auto_20220807_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='selling_price',
        ),
        migrations.AddField(
            model_name='product',
            name='cost_price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
