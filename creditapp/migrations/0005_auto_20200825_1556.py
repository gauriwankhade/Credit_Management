# Generated by Django 3.0.8 on 2020-08-25 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creditapp', '0004_auto_20200820_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferhistory',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creditapp.User'),
        ),
        migrations.AlterField(
            model_name='transferhistory',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_credits', to='creditapp.User'),
        ),
    ]
