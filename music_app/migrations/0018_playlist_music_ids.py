# Generated by Django 2.2.5 on 2021-05-25 17:03

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0017_remove_playlist_music_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='music_ids',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), default=0, max_length=10100, size=100),
            preserve_default=False,
        ),
    ]
