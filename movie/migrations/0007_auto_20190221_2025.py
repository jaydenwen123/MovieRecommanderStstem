# Generated by Django 2.1.3 on 2019-02-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20190221_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='movie_profile',
            field=models.CharField(max_length=1024),
        ),
    ]