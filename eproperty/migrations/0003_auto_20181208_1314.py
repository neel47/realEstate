# Generated by Django 2.1.3 on 2018-12-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eproperty', '0002_auto_20181208_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='userName',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
