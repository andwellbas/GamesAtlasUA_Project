# Generated by Django 4.2 on 2023-05-14 10:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_hub', '0017_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(500)]),
        ),
    ]