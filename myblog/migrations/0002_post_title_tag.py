# Generated by Django 4.1 on 2022-08-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My freakin awesome blog!', max_length=255),
        ),
    ]
