# Generated by Django 3.2.13 on 2022-11-17 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('adult', models.BooleanField()),
                ('poster_path', models.TextField()),
                ('actor', models.TextField()),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('release_date', models.DateField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('genre', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
    ]
