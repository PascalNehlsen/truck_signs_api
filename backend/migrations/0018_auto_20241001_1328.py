# Generated by Django 2.2.8 on 2024-10-01 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_auto_20210724_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='only_on_default_color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_color_default',
        ),
    ]