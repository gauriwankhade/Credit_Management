# Generated by Django 3.0.8 on 2020-08-31 15:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creditapp', '0008_auto_20200827_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferhistory',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='transferhistory',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 31, 15, 42, 10, 595146)),
        ),
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
