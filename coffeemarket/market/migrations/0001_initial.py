# Generated by Django 2.2.1 on 2019-10-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsertRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('userId', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
