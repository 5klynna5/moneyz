# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0007_auto_20160310_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='time_period',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
