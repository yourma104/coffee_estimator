# Generated by Django 4.2.1 on 2023-10-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='altitude_mean_meters',
            field=models.IntegerField(),
        ),
    ]
