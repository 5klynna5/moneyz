from django.contrib import admin
from .models import Client, Account, Contractor, Expense_type, Invoice, Invoice_received, Payee, Payment_made
from django.http import HttpResponse
from django.core import serializers

import csv
from django.http import HttpResponse, HttpResponseForbidden
from django.template.defaultfilters import slugify
##from django.db.models.loading import get_model
try:
    from django.apps import apps
    get_model = apps.get_model
except:
    from django.db.models.loading import get_model


def export(modeladmin, request, queryset):
    model = queryset.model
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % slugify(model.__name__)
    writer = csv.writer(response)
    # Write headers to CSV file
    headers = []
    for field in model._meta.fields:
    	headers.append(field.name)
    writer.writerow(headers)
    # Write data to CSV file
    for obj in queryset:
        row = []
        for field in headers:
            if field in headers:
                val = getattr(obj, field)
                if callable(val):
                    val = val()
                row.append(val)
        writer.writerow(row)
    # Return CSV file to browser as download
    return response


admin.site.add_action(export, 'export_selected')

admin.site.register(Client)
admin.site.register(Account)
admin.site.register(Contractor)
admin.site.register(Expense_type)
admin.site.register(Invoice)
admin.site.register(Invoice_received)
admin.site.register(Payee)
admin.site.register(Payment_made)