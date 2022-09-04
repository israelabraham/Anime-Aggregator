# Generated by Django 3.0.7 on 2022-09-04 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_auto_20200810_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Anime Categories',
                'db_table': 'anime_categories',
            },
        ),
        migrations.CreateModel(
            name='SavedAnime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_src', models.URLField()),
                ('image_alt', models.CharField(max_length=255)),
                ('anime_link', models.URLField()),
                ('released', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Saved Animes',
                'db_table': 'saved_animes',
            },
        ),
        migrations.AlterModelOptions(
            name='search',
            options={'verbose_name_plural': 'Searched Anime'},
        ),
        migrations.RenameField(
            model_name='search',
            old_name='search',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='search',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterModelTable(
            name='search',
            table='searches',
        ),
    ]