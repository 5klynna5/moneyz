# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0016_auto_20160317_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time_entry',
            name='account',
        ),
        migrations.RemoveField(
            model_name='time_entry',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='time_entry',
            name='person',
        ),
        migrations.DeleteModel(
            name='Time_entry',
        ),
    ]
