# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20150902_0857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='sku_first',
            new_name='sku',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='sku_second',
            new_name='sku',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Name',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='123', unique=True, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='Name',
            field=models.CharField(unique=True, max_length=250),
        ),
    ]
