# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0008_invoice_time_period'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ['-date_submitted']},
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_payment_received',
            field=models.DateField(blank=True, null=True),
        ),
    ]
