# Generated by Django 2.1.3 on 2018-11-29 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='eamil',
            new_name='email',
        ),
    ]
