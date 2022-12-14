# Generated by Django 4.1.3 on 2022-11-29 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('movie', models.CharField(max_length=255)),
                ('other_name', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('actor', models.CharField(max_length=255)),
                ('year', models.DateField()),
                ('rate', models.IntegerField()),
                ('first_introduction', models.CharField(max_length=255)),
            ],
        ),
    ]
