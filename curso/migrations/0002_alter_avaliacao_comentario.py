# Generated by Django 4.2.12 on 2024-05-07 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='comentario',
            field=models.TextField(blank=True, default=''),
        ),
    ]
