# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0017_auto_20160329_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='budget_external',
            field=models.DecimalField(default=0, max_digits=10, blank=True, decimal_places=2),
        ),
        migrations.AddField(
            model_name='account',
            name='total_budget',
            field=models.DecimalField(default=0, max_digits=10, blank=True, decimal_places=2),
        ),
    ]
