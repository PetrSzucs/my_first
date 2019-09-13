# Generated by Django 2.1.7 on 2019-02-28 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=200)),
                ('rezie', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='Zanr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev_zanru', models.CharField(max_length=80)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviebook.Film')),
            ],
        ),
    ]