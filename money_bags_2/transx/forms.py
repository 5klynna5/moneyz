from django import forms
from .models import Invoice, Invoice_received, Payment_made
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget 
from functools import partial
from datetime import datetime
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ('account', 'date_submitted', 'total_amount', 'date_payment_received',)


class ReceivedForm(forms.ModelForm):

    class Meta:
        model = Invoice_received
        fields = ('account', 'submitted_by', 'date_submitted', 'total_amount', 'date_payment_sent', 'date_payment_cashed',)

class PaymentForm(forms.ModelForm):

	 class Meta:
	 	model = Payment_made
	 	fields = ('date_paid', 'payee', 'amount', 'account', 'reimbursement',)


class DateRangeForm(forms.Form):
    
    class Meta:
        fields = ('start_date', 'end_date')
        widgets = {
        'start_date': DateInput(),
        'end_date': DateInput(),
        }
    '''
    year = datetime.today().year
    YEAR_LIST = range(year, year -10, -1)
    start_date = forms.DateField(widget=SelectDateWidget(years = YEAR_LIST))
    end_date = forms.DateField(widget=SelectDateWidget(years = YEAR_LIST))

    '''