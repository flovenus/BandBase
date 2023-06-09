# Generated by Django 4.2 on 2023-04-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BandMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('instruments', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='band',
            name='members',
            field=models.ManyToManyField(to='bands.bandmember'),
        ),
    ]
