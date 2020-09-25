# Generated by Django 3.1.1 on 2020-09-21 11:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_remove_answer_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.ManyToManyField(related_name='answer_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]