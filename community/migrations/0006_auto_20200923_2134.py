# Generated by Django 3.1.1 on 2020-09-23 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_auto_20200923_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='owner',
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.question'),
        ),
    ]
