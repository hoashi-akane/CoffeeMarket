# Generated by Django 2.2.1 on 2019-10-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insertregister',
            name='id',
        ),
        migrations.AlterField(
            model_name='insertregister',
            name='userId',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
