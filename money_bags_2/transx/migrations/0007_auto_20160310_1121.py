# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0006_auto_20160310_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_contact',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
