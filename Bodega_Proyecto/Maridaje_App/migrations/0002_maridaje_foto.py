# Generated by Django 5.0.6 on 2024-06-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maridaje_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maridaje',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='maridajes/'),
        ),
    ]
