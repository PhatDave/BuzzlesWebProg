# Generated by Django 3.2.9 on 2021-12-06 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_skyscraperspuzzle_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=32),
            preserve_default=False,
        ),
    ]
