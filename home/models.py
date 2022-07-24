from datetime import date
from django.db import models

from accounts.models import Account

# Create your models here.


class Floor(models.Model):
    name = models.CharField(max_length=50)


class Unit(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    unit_no = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='available')

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    national_id = models.BigIntegerField()
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    advance_rent = models.BigIntegerField() 
    rent_per_month = models.BigIntegerField()
    issue_date = models.DateField()
    rent_month = models.CharField(max_length=250) 
    rent_year = models.CharField(max_length=250) 
    status = models.CharField(max_length=250)
    image = models.ImageField(upload_to='tenant/',)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    address = models.TextField()
    national_id = models.BigIntegerField()
    designation = models.CharField(max_length=255)
    join_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    salary_per_month = models.BigIntegerField() 
    status = models.CharField(max_length=250)
    image = models.FileField(upload_to='employee/')

class Employee_Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    salary_month = models.CharField(max_length=255)
    salary_year = models.CharField(max_length=255)
    salary_per_month = models.BigIntegerField()
    issue_date = models.DateField()
class Rent(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    rent_month = models.CharField(max_length=255)
    rent_year = models.CharField(max_length=250)
    rent = models.CharField(max_length=255)
    water_bill = models.BigIntegerField()
    electric_bill = models.BigIntegerField()
    gas_bill = models.BigIntegerField()
    security_bill = models.BigIntegerField()
    utility_bill = models.BigIntegerField()
    other_bill = models.BigIntegerField()
    total_rent = models.FloatField()
    bill_paid_date = models.DateField()
    status = models.CharField(max_length=250)



class Maintenance(models.Model):
    date = models.DateField()
    month = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    amount = models.FloatField()
    details = models.TextField()


class Management(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    address = models.TextField()
    national_id = models.BigIntegerField()
    designation = models.CharField(max_length=255)
    join_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=250)
    image = models.FileField(upload_to='management/')


class Bill(models.Model):
    bill_type = models.CharField(max_length=255)
    deposit_date = models.DateField()
    bill_month = models.CharField(max_length=255)
    bill_year = models.CharField(max_length=255)
    total_amount = models.FloatField()
    deposit_method = models.CharField(max_length=255)
    details = models.TextField()



class Complain(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    status = models.CharField(max_length=250, blank=True, null=True)
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    solution = models.CharField(max_length=255, blank=True, null=True)

class Notify(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT, verbose_name="complain by")
    assigned = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, blank=True, verbose_name="assigned to")
    complain = models.ForeignKey(Complain, on_delete=models.PROTECT, null=True, blank=True)
    seen = models.PositiveIntegerField(default=0)
    complain_date = models.DateTimeField(auto_now=True)
    

class Visitor(models.Model):
    entry_date = models.DateField()
    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    address = models.TextField() 
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    in_time = models.TimeField()
    out_time = models.TimeField()

