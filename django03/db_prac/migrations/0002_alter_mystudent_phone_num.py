# Generated by Django 3.2 on 2021-04-23 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_prac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystudent',
            name='phone_num',
            field=models.CharField(max_length=30),
        ),
    ]
