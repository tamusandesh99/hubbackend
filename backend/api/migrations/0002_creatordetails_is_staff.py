# Generated by Django 4.2.9 on 2024-01-29 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatordetails',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]