from django.urls import path
from . import views

urlpatterns = [
    #Floor
    path('floor', views.floor, name='floor'),
    path('unit', views.unit, name='unit'),
    path('tenant', views.tenant, name='tenant'),
    path('edit-tenant/<int:id>', views.edit_tenant, name='edit_tenant'),
    path('delete-tenant/<int:id>', views.delete_tenant, name='delete_tenant'),

    #Employee
    path('add-employee', views.add_employee, name='add_employee'),
    path('edit-employee/<int:id>', views.edit_employee, name='edit_employee'),
    path('delete-employee/<int:id>', views.delete_employee, name='delete_employee'),

    #Salary
    path('employee-salary', views.employee_salary, name='employee_salary'),
    path('edit-salary/<int:id>', views.edit_salary, name='edit_salary'),
    path('delete-salary/<int:id>', views.delete_salary, name='delete_salary'),
    path('view-salary/<int:id>', views.view_salary, name='view_salary'),


    #all ajax calls
    path('employee-ajax', views.employee_ajax, name='employee_ajax'),
    path('floor-ajax', views.floor_ajax, name='floor_ajax'),
    path('floor-ajax1', views.floor_ajax1, name='floor_ajax1'),
    path('unit-ajax', views.unit_ajax, name='unit_ajax'),
    path('status-ajax', views.status_ajax, name='status_ajax'),
    path('assign-ajax', views.assign_ajax, name='assign_ajax'),


    # Rent  
    path('rent', views.rent, name='rent'),
    path('rent-list', views.rent_list, name='rent_list'),
    path('update-rent/<int:id>', views.update_rent, name='update_rent'),
    path('delete-rent/<int:id>', views.delete_rent, name='delete_rent'),
    path('print-invoice/<int:id>', views.print_invoice, name='print_invoice'),

    # Maintenance
    path('maintenance', views.maintenance, name='maintenance'),
    path('update-maintenance/<int:id>', views.update_maintenance, name='update_maintenance'),
    path('delete-maintenance/<int:id>', views.delete_maintenance, name='delete_maintenance'),

    # Management
    path('management', views.management, name='management'),
    path('edit-management/<int:id>', views.edit_management, name='edit_management'),
    path('delete-management/<int:id>', views.delete_management, name='delete_management'),

    # Bill Deposit 
    path('bill', views.bill, name='bill'),
    path('edit-bill/<int:id>', views.edit_bill, name='edit_bill'),
    path('delete-bill/<int:id>', views.delete_bill, name='delete_bill'),

    # Complain
    path('complain', views.complain, name='complain'),
    path('update-solution/<int:id>', views.update_solution, name='update_solution'),
    path('view-owner-complain/<int:id>', views.view_owner_complain, name='view_owner_complain'),
    path('view-tenant-complain/<int:id>', views.view_tenant_complain, name='view_tenant_complain'),
    path('delete-complain/<int:id>', views.delete_complain, name='delete_complain'),
    path('complainData/', views.complainData.as_view()), 
    path('viewComplain/', views.viewComplain, name='viewComplain'), 

    #Visitor
    path("visitor", views.visitor, name="visitor"),
    path('edit-visitor/<int:id>', views.edit_visitor, name='edit_visitor'),
    path('delete-visitor/<int:id>', views.delete_visitor, name='delete_visitor'),
    
    #Rental reports
    path("report/rental-report", views.rental_report, name="rental_report"),
    path("report/rental-report/view-result", views.view_result, name="view_result"),
   
    #Tenant reports
    path("report/tenant-report", views.tenant_report, name="tenant_report"),
    path("report/tenant-result", views.tenant_result, name="tenant_result"),

    #visitor reports
    path("report/visitor-report", views.visitor_report, name="visitor_report"),
    path("report/visitor-result", views.visitor_result, name="visitor_result"),

    #complain reports
    path("report/complain-report", views.complain_report, name="complain_report"),
    path("report/complain-result", views.complain_result, name="complain_result"),

    #unit reports
    path("report/unit-report", views.unit_report, name="unit_report"),
    path("report/unit-result", views.unit_result, name="unit_result"),

    #bill reports
    path("report/bill-report", views.bill_report, name="bill_report"),
    path("report/bill-result", views.bill_result, name="bill_result"),

    #salary reports
    path("report/salary-report", views.salary_report, name="salary_report"),
    path("report/salary-result", views.salary_result, name="salary_result"),

]