# Generated by Django 3.2 on 2022-03-08 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='RestaurantAPP.restaurant'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]
