# Generated by Django 2.0 on 2017-12-17 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20171217_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.User'),
        ),
        migrations.AlterField(
            model_name='rentmovies',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Movie'),
        ),
        migrations.AlterField(
            model_name='rentmovies',
            name='rent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Rent'),
        ),
    ]
