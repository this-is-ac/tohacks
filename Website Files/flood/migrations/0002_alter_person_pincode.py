# Generated by Django 3.2.2 on 2021-05-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
