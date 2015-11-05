# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flashTrolley', '0010_auto_20151019_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=datetime.datetime(2015, 10, 19, 17, 24, 54, 968000, tzinfo=utc), upload_to=b'media/products/images'),
            preserve_default=False,
        ),
    ]
