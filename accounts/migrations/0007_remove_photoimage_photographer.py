# Generated by Django 3.2.4 on 2021-07-23 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210617_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoimage',
            name='photographer',
        ),
    ]
