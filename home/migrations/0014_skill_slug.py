# Generated by Django 4.1.12 on 2024-05-04 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_skill_module_delete_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
