# Generated by Django 2.1.3 on 2019-02-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20190221_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='movie_date',
            field=models.CharField(max_length=64),
        ),
    ]
