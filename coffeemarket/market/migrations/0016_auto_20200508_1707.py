# Generated by Django 3.0.3 on 2020-05-08 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0015_coffeebeans_beans_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeebeans',
            name='beans_image',
        ),
        migrations.AddField(
            model_name='beansimage',
            name='coffee_beans',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='market.CoffeeBeans'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beansimage',
            name='beans_image',
            field=models.ImageField(blank=True, null=True, upload_to='market/'),
        ),
        migrations.AlterField(
            model_name='coffeebeans',
            name='place_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.PlaceCategory'),
        ),
    ]