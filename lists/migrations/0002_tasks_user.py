# Generated by Django 3.1.3 on 2020-11-22 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='user',
            field=models.CharField(default='', max_length=20),
        ),
    ]
