# Generated by Django 3.1.4 on 2021-06-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='is_employed',
            field=models.BooleanField(default=False),
        ),
    ]
