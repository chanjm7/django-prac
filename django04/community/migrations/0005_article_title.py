# Generated by Django 3.2 on 2021-04-23 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_alter_article_category_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]