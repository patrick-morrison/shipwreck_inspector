# Generated by Django 3.2.12 on 2022-02-20 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrecks', '0007_publication_reports'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='site',
        ),
        migrations.AddField(
            model_name='publication',
            name='site',
            field=models.ManyToManyField(to='wrecks.Site'),
        ),
    ]
