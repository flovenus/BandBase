# Generated by Django 4.2 on 2023-04-29 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0007_alter_album_rating_alter_song_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='email',
        ),
    ]
