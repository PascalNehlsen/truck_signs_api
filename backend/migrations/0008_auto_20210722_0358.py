# Generated by Django 2.2.8 on 2021-07-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20210722_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='max_amount_of_lettering_items',
            field=models.IntegerField(default=-1),
        ),
    ]
