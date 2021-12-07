# Generated by Django 3.2.9 on 2021-12-07 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211207_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayedGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('time', models.TimeField()),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.skyscraperspuzzle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
