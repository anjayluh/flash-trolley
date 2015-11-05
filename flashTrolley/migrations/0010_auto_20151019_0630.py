# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flashTrolley', '0009_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 19, 3, 30, 16, 299000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to=b'media/products/images'),
        ),
    ]
