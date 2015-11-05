# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flashTrolley', '0008_auto_20150925_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=datetime.datetime(2015, 9, 26, 8, 3, 12, 908000, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
