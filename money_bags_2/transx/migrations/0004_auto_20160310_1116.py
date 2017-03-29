# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transx', '0003_contract'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('account_title', models.CharField(max_length=50)),
                ('client', models.ForeignKey(to='transx.Client')),
            ],
            options={
                'ordering': ['client'],
            },
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('contractor_id', models.AutoField(primary_key=True, serialize=False)),
                ('contractor_name', models.CharField(max_length=40)),
                ('w9_on_file', models.BooleanField(help_text='check this box if have w9 for this contractor')),
                ('contractor_email', models.EmailField(max_length=254, blank=True)),
                ('contractor_phone', models.CharField(max_length=12, blank=True)),
                ('contractor_address', models.TextField(blank=True)),
                ('cotractor_ein', models.CharField(max_length=12, blank=True)),
                ('contractor_ssn', models.CharField(max_length=12, blank=True)),
                ('contractor_description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice_received',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_submitted', models.DateField()),
                ('date_payment_sent', models.DateField(blank=True)),
                ('total_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('account', models.ForeignKey(to='transx.Account')),
            ],
            options={
                'ordering': ['date_submitted'],
            },
        ),
        migrations.CreateModel(
            name='Payee',
            fields=[
                ('payee_id', models.AutoField(primary_key=True, serialize=False)),
                ('payee_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_made',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('date_paid', models.DateField()),
                ('account', models.ForeignKey(to='transx.Account', blank=True)),
                ('contractor', models.ForeignKey(to='transx.Contractor', blank=True)),
                ('invoice_no', models.ForeignKey(to='transx.Invoice_received', blank=True)),
                ('non_contractor_payee', models.ForeignKey(to='transx.Payee', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='contract',
            name='client',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='client',
        ),
        migrations.RemoveField(
            model_name='time_entry',
            name='client',
        ),
        migrations.AlterField(
            model_name='expense_type',
            name='expense_category',
            field=models.CharField(max_length=40),
        ),
        migrations.DeleteModel(
            name='Contract',
        ),
        migrations.AddField(
            model_name='invoice_received',
            name='line_items',
            field=models.ManyToManyField(blank=True, to='transx.Expense_type'),
        ),
        migrations.AddField(
            model_name='invoice_received',
            name='submitted_by',
            field=models.ForeignKey(to='transx.Contractor'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='account',
            field=models.ForeignKey(null=True, to='transx.Account'),
        ),
        migrations.AddField(
            model_name='time_entry',
            name='account',
            field=models.ForeignKey(null=True, to='transx.Account'),
        ),
        migrations.AddField(
            model_name='time_entry',
            name='person',
            field=models.ForeignKey(null=True, to='transx.Contractor'),
        ),
    ]
