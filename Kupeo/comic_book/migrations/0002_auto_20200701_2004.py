# Generated by Django 3.0.7 on 2020-07-01 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comic_book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='au',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='cr_date',
        ),
    ]
