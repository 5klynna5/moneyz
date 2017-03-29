# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0010_auto_20160311_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_made',
            name='contractor',
            field=models.ForeignKey(to='transx.Contractor', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment_made',
            name='invoice_no',
            field=models.ForeignKey(to='transx.Invoice_received', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment_made',
            name='non_contractor_payee',
            field=models.ForeignKey(to='transx.Payee', blank=True, null=True),
        ),
    ]
