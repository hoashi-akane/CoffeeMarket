# Generated by Django 3.0.3 on 2020-04-23 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_cartinfo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartinfo',
            unique_together=set(),
        ),
    ]
