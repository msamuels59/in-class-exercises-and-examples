# Generated by Django 4.0.3 on 2022-03-15 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_ingredient_amounts_alter_recipe_directions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient_amounts',
        ),
    ]
