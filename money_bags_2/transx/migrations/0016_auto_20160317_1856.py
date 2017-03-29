# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0015_invoice_received_date_payment_cashed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment_made',
            options={'ordering': ['-date_paid']},
        ),
    ]
