# Generated by Django 4.2.2 on 2023-07-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_creatordetails_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatordetails',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='creatordetails',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='creatordetails',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]