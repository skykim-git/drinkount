# Generated by Django 4.2.10 on 2024-02-13 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinker',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='drinker',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
