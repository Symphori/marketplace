# Generated by Django 4.2.13 on 2024-06-27 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_product_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
