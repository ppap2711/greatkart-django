# Generated by Django 3.2.9 on 2022-02-24 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categroy_name',
            new_name='category_name',
        ),
    ]
