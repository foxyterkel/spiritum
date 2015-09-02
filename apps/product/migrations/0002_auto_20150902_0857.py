# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='sku_first',
            field=models.CharField(default='', max_length=250, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='sku_second',
            field=models.CharField(default='', max_length=250, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=250, blank=True),
        ),
    ]
