# Generated by Django 3.1 on 2022-03-09 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrecks', '0034_auto_20220226_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
