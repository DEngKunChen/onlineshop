# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20170826_1201'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='goodscategorybrand',
            table='goods_goodsbrand',
        ),
    ]
