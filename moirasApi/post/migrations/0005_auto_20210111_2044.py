# Generated by Django 3.1.5 on 2021-01-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210111_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='urlContent',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='UrlКонтент'),
        ),
    ]
