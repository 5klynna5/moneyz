# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0014_auto_20160311_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice_received',
            name='date_payment_cashed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
