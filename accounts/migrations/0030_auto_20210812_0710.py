# Generated by Django 3.2.4 on 2021-08-12 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_alter_recruter_rec_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruterapp',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.district'),
        ),
        migrations.AddField(
            model_name='recruterapp',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Male', max_length=10),
        ),
        migrations.AddField(
            model_name='recruterapp',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.province'),
        ),
        migrations.AddField(
            model_name='recruterapp',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.sector'),
        ),
    ]