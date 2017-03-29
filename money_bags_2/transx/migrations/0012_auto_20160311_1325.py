# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0011_auto_20160311_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment_made',
            old_name='non_contractor_payee',
            new_name='payee',
        ),
        migrations.RemoveField(
            model_name='payment_made',
            name='contractor',
        ),
    ]
