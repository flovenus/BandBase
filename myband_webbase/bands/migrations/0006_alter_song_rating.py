# Generated by Django 4.2 on 2023-04-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0005_remove_album_band_band_albums_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='rating',
            field=models.IntegerField(blank=True),
        ),
    ]
