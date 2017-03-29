from django.conf.urls import url
from . import views
from transx.models import Invoice


urlpatterns = [
    url(r'^$', views.home_page, name = 'home_page'),
    url(r'^unpaid_invoices/', views.unpaid_invoice_list, name='unpaid_invoice_list'),
    url(r'^invoice/(?P<pk>\d+)/$', views.manage_invoice, name='manage_invoice'),
    url(r'^to_pay/$', views.invoices_to_pay, name='invoices_to_pay'),
    url(r'^invoice_received/(?P<pk>\d+)/$', views.manage_invoice_received, name='manage_invoice_received'),
    url(r'^reimburse/$', views.to_be_reimbursed_list, name='to_be_reimbursed_list'),
    url(r'^manage_payment/(?P<pk>\d+)/$', views.manage_payment, name='manage_payment'),
    url(r'^payments_accounts/$', views.payments_accounts, name = 'payments_accounts'),
    url(r'^select_date/$', views.select_date, name = 'select_date'),
    #url(r'^select_date/?start_date_month=[0-9]&start_date_day=[0-9]&start_date_year=[0-9]{4}&end_date_month=[0-9]&end_date_day=[0-9]&end_date_year=[0-9]{4}$', views.income, name = 'income'),
    url(r'^income_time/$', views.income_time, name = 'income_time'),
    url(r'^income_month/', views.income_month, name = 'income_month'),
    url(r'^income_last_month/', views.income_last_month, name = 'income_last_month'),
    url(r'^contract_list/', views.contract_list, name = 'contract_list')
]