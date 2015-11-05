# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flashTrolley', '0007_customer_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='confirm_password',
            field=models.CharField(default=datetime.datetime(2015, 9, 25, 15, 10, 33, 325000, tzinfo=utc), max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(verbose_name=b'Phone number'),
        ),
    ]
