# Generated by Django 3.0.3 on 2020-05-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]