# Generated by Django 4.2b1 on 2023-04-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppKaren', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='cant_dias',
            field=models.CharField(max_length=20),
        ),
    ]
