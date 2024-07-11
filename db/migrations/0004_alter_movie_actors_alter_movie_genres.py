# Generated by Django 4.0.2 on 2024-07-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_cinemahall_moviesession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(null=True, related_name='actors', to='db.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(null=True, related_name='genres', to='db.Genre'),
        ),
    ]
