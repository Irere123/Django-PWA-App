# Generated by Django 3.1.2 on 2020-10-07 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_usersession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersession',
            old_name='activate',
            new_name='active',
        ),
    ]