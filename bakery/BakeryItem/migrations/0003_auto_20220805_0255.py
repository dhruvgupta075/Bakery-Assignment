# Generated by Django 3.1.1 on 2022-08-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakeryItem', '0002_auto_20220805_0113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='quantity',
            new_name='percentage',
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(to='BakeryItem.Ingredient'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]