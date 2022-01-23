# Generated by Django 3.2.11 on 2022-01-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20220122_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('action', 'ACTIONS'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('germany', 'GERMAN')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('recently', 'RECENTLY'), ('mostwaches', 'MOST WATCHES'), ('toprated', 'TOP RATED'), ('comingsoon', 'COMING SOON')], max_length=10),
        ),
    ]