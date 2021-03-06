# Generated by Django 3.1 on 2022-02-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrecks', '0023_auto_20220223_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='publications/%Y'),
        ),
        migrations.AlterField(
            model_name='report',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='reports/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='site',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='site_images/'),
        ),
    ]
