# Generated by Django 5.0.1 on 2024-01-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomaizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]