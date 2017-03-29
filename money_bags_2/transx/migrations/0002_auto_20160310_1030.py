# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(serialize=False, primary_key=True)),
                ('client_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Time_entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'ordering': ['entry_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='expense_type',
            options={'ordering': ['expense_category']},
        ),
        migrations.AlterField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(to='transx.Client'),
        ),
        migrations.AddField(
            model_name='time_entry',
            name='activities',
            field=models.ManyToManyField(to='transx.Expense_type'),
        ),
        migrations.AddField(
            model_name='time_entry',
            name='client',
            field=models.ForeignKey(to='transx.Client'),
        ),
    ]
