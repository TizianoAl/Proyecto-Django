# Generated by Django 2.2 on 2020-05-14 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ejemplares',
            field=models.ManyToManyField(to='biblioteca.Ejemplar'),
        ),
    ]
