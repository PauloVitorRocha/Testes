# Generated by Django 2.1.1 on 2018-09-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=255)),
                ('modelo', models.CharField(max_length=255)),
                ('placa', models.CharField(max_length=7)),
                ('local', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
    ]