# Generated by Django 5.1.7 on 2025-03-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZodApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
