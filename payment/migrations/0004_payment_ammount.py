# Generated by Django 3.2.4 on 2021-08-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_payment_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='ammount',
            field=models.IntegerField(default=0),
        ),
    ]
