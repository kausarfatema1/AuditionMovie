# Generated by Django 3.2.4 on 2021-07-26 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_auto_20210724_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='is_accepted',
        ),
    ]
