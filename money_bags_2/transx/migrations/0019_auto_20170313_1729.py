# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0018_auto_20170313_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={},
        ),
        migrations.AddField(
            model_name='account',
            name='status',
            field=models.CharField(max_length=10, choices=[('PAST', 'Past'), ('CURRENT', 'Current')], blank=True, null=True),
        ),
    ]
