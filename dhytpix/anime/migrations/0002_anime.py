# Generated by Django 4.1.4 on 2022-12-23 01:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('thumb', models.ImageField(upload_to='thumbs')),
                ('description', models.TextField(max_length=10000)),
                ('link', models.URLField()),
                ('category', models.CharField(choices=[('ACAO', 'Ação'), ('AVENTURA', 'Aventura'), ('DRAMA', 'Drama'), ('COMÉDIA', 'Comédia'), ('ROMANCE', 'Romance'), ('SCI-FI', 'Sci-Fi'), ('TERROR', 'Terror'), ('MISTERIO', 'Mistério'), ('SHONEN', 'Shōnen'), ('SHOUNEN', 'Shounen'), ('SEINEN', 'Seinen'), ('SHOJO', 'Shōjo'), ('JOSEI', 'Josei'), ('KODOMO', 'Kodomo'), ('UNDEFINED', 'Indefinido'), ('SEINEN/TERROR', 'Seinen/Terror'), ('MYSTERY/TERROR', 'Mistério/Terror')], max_length=1000)),
                ('views', models.IntegerField(default=0)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]