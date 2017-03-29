from django.db import models

class Client(models.Model):
	client_id = models.AutoField(primary_key=True)
	client_name = models.CharField(max_length=50)
	client_address = models.TextField(blank=True)
	client_contact = models.CharField(max_length=50, blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.client_name)

class Account(models.Model):
	client = models.ForeignKey('Client')
	account_title = models.CharField(max_length=50)
	total_budget = models.DecimalField(max_digits=10, decimal_places=2, blank = True, default= 0)
	budget_external = models.DecimalField(max_digits=10, decimal_places=2, blank = True, default = 0)


	STATUS_CHOICES = (
		('PAST', 'Past'),
		('CURRENT', 'Current'),
	)

	status = models.CharField(choices = STATUS_CHOICES, max_length = 10, blank=True, null=True)
	#class Meta:
		#ordering = ["client"]

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.client) + ' | ' + str(self.account_title)

class Contractor(models.Model):
	contractor_id = models.AutoField(primary_key=True)
	contractor_name = models.CharField(max_length=40)
	w9_on_file = models.BooleanField(help_text = 'check this box if have w9 for this contractor')
	contractor_email = models.EmailField(blank=True)
	contractor_phone = models.CharField(blank=True, max_length=12)
	contractor_address = models.TextField(blank=True)
	cotractor_ein = models.CharField(blank=True, max_length=12)
	contractor_ssn = models.CharField(blank=True, max_length=12)
	contractor_description = models.TextField(blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.contractor_id) + ' | ' + str(self.contractor_name)

class Expense_type(models.Model):
	expense_id = models.AutoField(primary_key=True)
	expense_category = models.CharField(max_length = 40)

	class Meta:
		ordering = ["expense_category"]

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.expense_id) + ' ' + str(self.expense_category)


class Invoice(models.Model):
	invoice_id = models.AutoField(primary_key=True)
	account = models.ForeignKey('Account', null=True)
	date_submitted = models.DateField()
	time_period = models.CharField(max_length = 50, blank=True)
	date_payment_received = models.DateField(blank=True, null=True)
	line_items = models.ManyToManyField('Expense_type', blank = True)
	total_amount = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		ordering = ["-date_submitted"]

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.account) + ' ' + str(self.date_submitted)

class Invoice_received(models.Model):
	invoice_id = models.AutoField(primary_key=True)
	account = models.ForeignKey('Account')
	submitted_by = models.ForeignKey('Contractor')
	date_submitted = models.DateField()
	date_payment_sent = models.DateField(blank=True, null=True)
	date_payment_cashed = models.DateField(blank=True, null=True)
	line_items = models.ManyToManyField('Expense_type', blank = True)
	total_amount = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		ordering = ["-date_submitted"]

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.submitted_by) + ' ' + str(self.account) + ' ' + str(self.date_submitted)

class Payee(models.Model):
	payee_id = models.AutoField(primary_key=True)
	payee_name = models.CharField(max_length=50)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.payee_name)

class Payment_made(models.Model):
	payment_id = models.AutoField(primary_key=True)
	account = models.ForeignKey('Account', blank=True)
	payee = models.ForeignKey('Payee', blank=True, null=True)
	amount = models.DecimalField(max_digits=10, decimal_places = 2)

	REIMBURSE_CHOICES = (
		('NO_REIMBURSE', 'Does not need to be reimbursed'),
		('NEEDS_REIMBURSE', 'Needs to be reimbursed'),
		('REIMBURSED', 'Already reimbursed'),
	)

	reimbursement = models.CharField(choices=REIMBURSE_CHOICES, max_length=15, blank=True, null=True)
	date_paid = models.DateField()

	class Meta:
		ordering = ["-date_paid"]

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.payee) + ' ' + str(self.date_paid) + ' | ' + str(self.amount)