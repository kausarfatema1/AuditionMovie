# Generated by Django 3.2.4 on 2021-07-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='status',
            field=models.CharField(choices=[('F', 'FAIL'), ('P', 'PASS')], default='F', max_length=1),
        ),
    ]
