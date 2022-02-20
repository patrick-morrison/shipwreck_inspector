# Generated by Django 3.2.12 on 2022-02-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrecks', '0011_auto_20220220_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hero_images/'),
        ),
        migrations.AddField(
            model_name='site',
            name='image_caption',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
