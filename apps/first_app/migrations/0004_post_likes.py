# Generated by Django 3.0.4 on 2020-04-16 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='first_app.User'),
        ),
    ]
