# Generated by Django 5.0.8 on 2024-10-08 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_remove_recipe_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='average_rating',
            new_name='calculated_average_rating',
        ),
    ]
