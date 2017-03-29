# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0013_remove_payment_made_invoice_no'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice_received',
            options={'ordering': ['-date_submitted']},
        ),
        migrations.AddField(
            model_name='payment_made',
            name='reimbursement',
            field=models.CharField(blank=True, null=True, max_length=15, choices=[('NO_REIMBURSE', 'Does not need to be reimbursed'), ('NEEDS_REIMBURSE', 'Needs to be reimbursed'), ('REIMBURSED', 'Already reimbursed')]),
        ),
    ]
