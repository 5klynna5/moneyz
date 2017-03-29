# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0012_auto_20160311_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_made',
            name='invoice_no',
        ),
    ]
