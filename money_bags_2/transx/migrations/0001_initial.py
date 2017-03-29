# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense_type',
            fields=[
                ('expense_id', models.AutoField(serialize=False, primary_key=True)),
                ('expense_category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(serialize=False, primary_key=True)),
                ('client', models.CharField(choices=[('AHS', 'Animal Humane Society'), ('ALLIANCE', 'Alliance Housing'), ('IMA', 'Institute for Mathematics and its Applications'), ('CORNERHOUSE', 'CornerHouse'), ('TERRALUNA_OMAHA', 'MHC OPS - Terraluna'), ('OTHER', 'Other')], max_length=15)),
                ('date_submitted', models.DateField()),
                ('date_payment_received', models.DateField(blank=True)),
                ('total_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('line_items', models.ManyToManyField(blank=True, to='transx.Expense_type')),
            ],
            options={
                'ordering': ['date_submitted'],
            },
        ),
    ]
