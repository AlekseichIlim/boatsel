# Generated by Django 5.0.7 on 2024-08-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='цена'),
        ),
    ]
