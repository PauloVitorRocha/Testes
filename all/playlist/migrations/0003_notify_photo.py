# Generated by Django 2.1.1 on 2018-09-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0002_auto_20180905_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='notify',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
    ]
