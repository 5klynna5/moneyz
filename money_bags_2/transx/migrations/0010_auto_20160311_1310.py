# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0009_auto_20160310_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_received',
            name='date_payment_sent',
            field=models.DateField(blank=True, null=True),
        ),
    ]
