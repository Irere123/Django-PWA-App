# Generated by Django 3.1.2 on 2020-10-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/profile_pics'),
        ),
    ]
