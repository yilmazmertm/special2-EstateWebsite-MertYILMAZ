# Generated by Django 3.0.3 on 2020-05-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200530_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='room_number',
            field=models.IntegerField(blank=True, choices=[('10', '1+0'), ('11', '1+1'), ('20', '2+0'), ('21', '2+1'), ('31', '3+1'), ('41', '4+1'), ('42', '4+2'), ('52', '5+2')]),
        ),
    ]
