# Generated by Django 3.1.1 on 2020-09-21 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_answer_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='likes',
        ),
    ]
