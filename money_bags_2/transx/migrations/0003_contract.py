# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0002_auto_20160310_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('contract_title', models.CharField(max_length=50)),
                ('client', models.ForeignKey(to='transx.Client')),
            ],
            options={
                'ordering': ['client'],
            },
        ),
    ]
