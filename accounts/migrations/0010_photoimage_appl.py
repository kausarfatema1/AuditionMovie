# Generated by Django 3.2.4 on 2021-07-23 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_alter_photographerapplication_email'),
        ('accounts', '0009_remove_photoimage_appl'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoimage',
            name='appl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='applications.photographerapplication'),
        ),
    ]
