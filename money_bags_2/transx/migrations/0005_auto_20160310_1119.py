# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0004_auto_20160310_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='client_contact',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
