# Generated by Django 3.2.12 on 2022-02-19 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrecks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='description',
            field=models.CharField(default='Barque', max_length=255),
            preserve_default=False,
        ),
    ]
