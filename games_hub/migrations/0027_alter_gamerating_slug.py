# Generated by Django 4.2 on 2023-06-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_hub', '0026_gamerating_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamerating',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
