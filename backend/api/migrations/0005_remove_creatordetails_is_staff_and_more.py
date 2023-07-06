# Generated by Django 4.2.2 on 2023-07-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_creatordetails_website_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creatordetails',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='creatordetails',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='creatordetails',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='creatordetails',
            name='password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='creatordetails',
            name='username',
            field=models.CharField(max_length=250),
        ),
    ]