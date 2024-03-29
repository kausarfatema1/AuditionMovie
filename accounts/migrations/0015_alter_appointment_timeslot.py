# Generated by Django 3.2.4 on 2021-07-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_appointment_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='timeslot',
            field=models.IntegerField(choices=[('09:00 – 09:30', '09:00 – 09:30'), ('10:00 – 10:30', '10:00 – 10:30'), ('11:00 – 11:30', '11:00 – 11:30'), ('12:00 – 12:30', '12:00 – 12:30'), ('13:00 – 13:30', '13:00 – 13:30'), ('14:00 – 14:30', '14:00 – 14:30'), ('15:00 – 15:30', '15:00 – 15:30'), ('16:00 – 16:30', '16:00 – 16:30'), ('17:00 – 17:30', '17:00 – 17:30')], null=True),
        ),
    ]
