# Generated by Django 2.0.1 on 2018-02-19 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0007_auto_20180219_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]