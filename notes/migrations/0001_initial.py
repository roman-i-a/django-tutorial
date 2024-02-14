# Generated by Django 5.0.1 on 2024-01-30 07:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_text', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('tags', models.ManyToManyField(to='notes.tag')),
            ],
        ),
    ]
