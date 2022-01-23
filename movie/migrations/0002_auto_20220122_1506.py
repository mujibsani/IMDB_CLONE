# Generated by Django 3.2.11 on 2022-01-22 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('RA', 'RECENTLY'), ('MW', 'MOST WATCHES'), ('TR', 'TOP RATED'), ('CS', 'COMING SOON')], max_length=2),
        ),
        migrations.CreateModel(
            name='MovieLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'DOWNLOAD LINK'), ('W', 'WATCH LINK')], max_length=1)),
                ('link', models.URLField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='movie.movie')),
            ],
        ),
    ]
