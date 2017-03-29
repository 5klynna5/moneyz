from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice, Invoice_received, Payment_made, Account
from .forms import InvoiceForm, ReceivedForm, PaymentForm, DateRangeForm
from django.db.models import Sum
from datetime import datetime
from django.views.generic.dates import MonthArchiveView

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from graphos.renderers.gchart import LineChart
from graphos.renderers.gchart import BarChart
from graphos.sources.model import ModelDataSource


def home_page(request):
    return render(request, 'transx/home_page.html')

@login_required(login_url='/login/')
def payments_accounts(request):
    payment_accounts = Payment_made.objects.all().aggregate(Sum('account'))
    return render(request, 'transx/payments_accounts.html', {'payment_accounts' : payment_accounts})

@login_required(login_url='/login/')
def unpaid_invoice_list(request):
	unpaid = Invoice.objects.filter(date_payment_received__isnull=True).order_by('date_submitted')
	return render(request, 'transx/unpaid_invoice_list.html', { 'unpaid' : unpaid})

@login_required(login_url='/login/')
def invoices_to_pay(request):
	to_pay = Invoice_received.objects.filter(date_payment_cashed__isnull=True).order_by('date_submitted')
	return render(request, 'transx/to_pay_invoice_list.html', {'to_pay' : to_pay})

@login_required(login_url='/login/')
def to_be_reimbursed_list(request):
    to_be_reimbursed = Payment_made.objects.filter(reimbursement='NEEDS_REIMBURSE').order_by('date_paid')
    return render(request, 'transx/to_be_reimbursed_list.html', {'to_be_reimbursed' : to_be_reimbursed})

@login_required(login_url='/login/')
def manage_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == "POST":
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.save()
            return redirect('unpaid_invoice_list')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'transx/manage_invoice.html', {'form': form})

@login_required(login_url='/login/')
def manage_invoice_received(request, pk):
    received = get_object_or_404(Invoice_received, pk=pk)
    if request.method == "POST":
        form = ReceivedForm(request.POST, instance=received)
        if form.is_valid():
            received = form.save(commit=False)
            received.save()
            return redirect('invoices_to_pay')
    else:
        form = ReceivedForm(instance=received)
    return render(request, 'transx/manage_invoice_received.html', {'form': form})

@login_required(login_url='/login/')
def manage_payment(request, pk):
    payment = get_object_or_404(Payment_made, pk=pk)
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.save()
            return redirect('to_be_reimbursed_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'transx/manage_payment.html', {'form': form})

def select_date(request):
    if request.method == "POST":
        f = DateRangeForm(request.POST)
        my_data = request.POST
        ###TODO we need to figure out this next - how to get the start date and end date into this view from the jquery ui 
        ######django select widget already works (has been commented out in lines 39 on in forms.py)
        start_date_from_user = my_data['start_date_year'] + '-' + my_data['start_date_month'] + '-' + my_data['start_date_day']
        end_date_from_user = my_data['end_date_year'] + '-' + my_data['end_date_month'] + '-' + my_data['end_date_day']
        income_month = Invoice.objects.filter(date_payment_received__range=[start_date_from_user, end_date_from_user])
        total_income_month = income_month.aggregate(Sum('total_amount'))
        invoices_paid_out_month = Invoice_received.objects.filter(date_payment_cashed__range=[start_date_from_user, end_date_from_user])
        total_invoices_paid_month = invoices_paid_out_month.aggregate(Sum('total_amount'))
        payments_month = Payment_made.objects.filter(date_paid__range=[start_date_from_user, end_date_from_user], reimbursement='NO_REIMBURSE')
        total_payments_month = payments_month.aggregate(Sum('amount'))
        return render(request, 'transx/income_month.html', {'income_month': income_month, 'invoices_paid_out_month' : invoices_paid_out_month, 'payments_month': payments_month, 'total_income_month' : total_income_month, 'total_invoices_paid_month': total_invoices_paid_month, 'total_payments_month' : total_payments_month})
    else:
        f = DateRangeForm()
        args = {}
        #args.update(csrf(request))
        args['form'] = f
    return render(request, 'transx/select_date.html', {'form': f})



@login_required(login_url='/login/')
def income_month(request):
    month = datetime.now().month
    year = datetime.now().year
    income_month = Invoice.objects.filter(date_payment_received__month=month).filter(date_payment_received__year=year)
    total_income_month = income_month.aggregate(Sum('total_amount'))
    invoices_paid_out_month = Invoice_received.objects.filter(date_payment_cashed__month=month).filter(date_payment_cashed__year=year)
    total_invoices_paid_month = invoices_paid_out_month.aggregate(Sum('total_amount'))
    payments_month = Payment_made.objects.filter(date_paid__month=month).filter(reimbursement='NO_REIMBURSE').filter(date_paid__year=year)
    total_payments_month = payments_month.aggregate(Sum('amount'))
    return render(request, 'transx/income_month.html', {'income_month': income_month, 'invoices_paid_out_month' : invoices_paid_out_month, 'payments_month': payments_month, 'total_income_month' : total_income_month, 'total_invoices_paid_month': total_invoices_paid_month, 'total_payments_month' : total_payments_month})

@login_required(login_url='/login/')
def income_last_month(request):
    month = datetime.now().month - 1
    year = datetime.now().year
    income_month = Invoice.objects.filter(date_payment_received__month=month).filter(date_payment_received__year=year)
    total_income_month = income_month.aggregate(Sum('total_amount'))
    invoices_paid_out_month = Invoice_received.objects.filter(date_payment_cashed__month=month).filter(date_payment_cashed__year=year)
    total_invoices_paid_month = invoices_paid_out_month.aggregate(Sum('total_amount'))
    payments_month = Payment_made.objects.filter(date_paid__month=month, reimbursement='NO_REIMBURSE').filter(date_paid__year=year)
    total_payments_month = payments_month.aggregate(Sum('amount'))
    return render(request, 'transx/income_last_month.html', {'income_month': income_month, 'invoices_paid_out_month' : invoices_paid_out_month, 'payments_month': payments_month, 'total_income_month' : total_income_month, 'total_invoices_paid_month': total_invoices_paid_month, 'total_payments_month' : total_payments_month})

def income_time(request):
    queryset = Invoice.objects.all()
    data_source = ModelDataSource(queryset, fields=['time_period', 'total_amount'])
    chart = LineChart(data_source)
    context = {'chart': chart}
    return render(request, 'transx/income_time.html', context)

def contract_list(request):
    contracts = Account.objects.filter(status = 'CURRENT')
    for item in contracts:
        item.payment = Payment_made.objects.filter(account = item).aggregate(Sum('amount')).get('amount__sum', 0.00)
        item.invoiced = Invoice.objects.filter(account = item).aggregate(Sum('total_amount')).get('total_amount__sum', 0.00)
    return render(request, 'transx/contract_list.html', { 'contracts' : contracts })



