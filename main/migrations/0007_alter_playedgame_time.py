# Generated by Django 3.2.9 on 2021-12-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_playedgame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playedgame',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]