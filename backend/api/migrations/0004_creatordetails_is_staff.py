# Generated by Django 4.2.9 on 2024-01-31 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_creatordetails_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatordetails',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]