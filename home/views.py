
from multiprocessing import context
from .models import*
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django_serverside_datatable.views import ServerSideDatatableView
from django.http import JsonResponse
from django.contrib import messages
import os


#############################################################################

@login_required
def floor(request):
    floors = Floor.objects.all()
    context = {'floors':floors}
    if request.method == 'POST':
        input = request.POST['input']
        #########SHIPPING LINE
        if input == 'delete_floor':
            id = request.POST['id']
            Floor.objects.filter(id=id).delete()
            messages.success(request, f'Floor deleted successfully! ')
            return redirect('floor')
        if input == 'update_floor':
            id = request.POST['id']
            name = request.POST['name']
            Floor.objects.filter(id=id).update(name=name)
            messages.success(request, f'Floor "{name}" updated successfully! ')
            return redirect('floor')
        if input == 'save_floor':
            name = request.POST['name']
            checkCode = Floor.objects.filter(name=name)
            if not checkCode:
                Floor(name=name).save()
                messages.success(request, f' New Floor "{name}" Created successfully! ')
                return redirect('floor')
            else:
                messages.warning(request, f' This Floor Number "{name}" Already Exists ')
    return render(request, 'floor/floor.html', context)


###############################################################################
@login_required
def unit(request):
    floors = Floor.objects.all()
    units = Unit.objects.all()
    context = {'floors':floors,
                'units':units}
    if request.method == 'POST':
        input = request.POST['input']
        
        if input == 'delete_unit':
            id = request.POST['id']
            Unit.objects.filter(id=id).delete()
            messages.success(request, f'Flat deleted successfully! ')
            return redirect('unit')
        if input == 'update_unit':
            id = request.POST['id']
            floor = request.POST['floor_id']
            unit_no = request.POST['unit_no']
            status = request.POST['status']
            Unit.objects.filter(id=id).update(
                unit_no=unit_no,
                floor_id=floor,
                status=status
                
                )
            messages.success(request, f'Flat "{unit_no}" updated successfully! ')
            return redirect('unit')
        if input == 'save_unit':
            floor = request.POST['floor_id']
            unit_no = request.POST['unit_no']
            status = request.POST['status']
            checkCode = Unit.objects.filter(unit_no=unit_no)
            if not checkCode:
                Unit(floor_id=floor, 
                unit_no=unit_no,
                status=status
                ).save()
                messages.success(request, f' New Flat "{unit_no}" Created successfully! ')
                return redirect('unit')
            else:
                messages.warning(request, f' This Flat No "{unit_no}" Already Exists ')

    return render(request, 'unit/unit.html', context)

@login_required
def tenant(request):
    floors = Floor.objects.all()
    units = Unit.objects.all()
    tenants = Tenant.objects.all()
    context = {'floors':floors,'units':units, 'tenants':tenants}
    if request.method == 'POST':
        ten = Tenant()
        ten.name = request.POST['name']
        ten.address = request.POST['address']
        ten.national_id = request.POST['national_id']
        ten.floor_id = request.POST['floor']
        ten.unit_id = request.POST.get('unit')
        ten.advance_rent = request.POST['advance_rent']
        ten.rent_per_month = request.POST['rent_per_month']
        ten.issue_date = request.POST['issue_date']
        ten.rent_month = request.POST['rent_month']
        ten.rent_year= request.POST['rent_year']
        ten.status = request.POST['status']
        if len(request.FILES) != 0:
            ten.image = request.FILES['image']
        ten.save()
        messages.success(request, f' New Tenant Added successfully! ')
        return redirect('tenant')
    return render(request, 'tenant/tenant.html', context)


@login_required
def edit_tenant(request, id):
    ten = Tenant.objects.get(id=id)
    if request.method == 'POST':
        if len(request.FILES)!=0:
            if len(ten.image) > 0:
                os.remove(ten.image.path)
            ten.image = request.FILES['image']
        ten.name = request.POST['name']
        ten.address = request.POST.get('address')
        ten.national_id = request.POST['national_id']
        ten.floor_id = request.POST.get('floor')
        ten.unit_id = request.POST.get('unit')
        ten.advance_rent = request.POST['advance_rent']
        ten.rent_per_month = request.POST['rent_per_month']
        ten.issue_date = request.POST['issue_date']
        ten.rent_month = request.POST['rent_month']
        ten.rent_year= request.POST['rent_year']
        ten.status = request.POST['status']
        ten.save()
        messages.success(request, f'Tenant "{ten.name}" Updated successfully!!!')
        return redirect('tenant')
    return render(request, 'tenant/tenant.html')

@login_required
def delete_tenant(request, id):
    Tenant.objects.filter(id=id).delete()
    messages.success(request, f'Tenant "{id}" Deleted successfully!!!')
    return redirect('tenant')

def add_employee(request):
    employees = Employee.objects.all()
    context = {'employees':employees}
    if request.method == 'POST':
        emp = Employee()
        emp.name = request.POST['name']
        emp.email = request.POST['email']
        emp.password = request.POST['password']
        emp.contact = request.POST['contact']
        emp.address = request.POST['address']
        emp.national_id = request.POST['national_id']
        emp.designation= request.POST['designation']
        emp.join_date = request.POST['join_date']
        emp.end_date = request.POST['end_date']
        emp.salary_per_month = request.POST['salary_per_month']
        emp.status = request.POST['status']
        if len(request.FILES) != 0:
            emp.image = request.FILES['image']
        emp.save()
        messages.success(request, f' New Employee "{emp.name}" Added successfully! ')
        return redirect('add_employee')
    return render(request, 'employee/employee.html', context)

@login_required
def edit_employee(request, id):
    emp = Employee.objects.get(id=id)
    if request.method == 'POST':
        if len(request.FILES)!=0:
            if len(emp.image) > 0:
                os.remove(emp.image.path)
            emp.image = request.FILES['image']
        emp.name = request.POST['name']
        emp.email = request.POST['email']
        emp.password = request.POST['password']
        emp.contact = request.POST['contact']
        emp.address = request.POST['address']
        emp.national_id = request.POST['national_id']
        emp.designation= request.POST['designation']
        emp.join_date = request.POST['join_date']
        emp.end_date = request.POST['end_date']
        emp.salary_per_month = request.POST['salary_per_month']
        emp.status = request.POST['status']
        emp.save()
        messages.success(request, f'Employee "{emp.name}" Updated successfully! ')
        return redirect('add_employee')
    return render(request, 'employee/employee.html')


@login_required
def delete_employee(request, id):
    Employee.objects.filter(id=id).delete()
    messages.success(request, f'Employee "{id}" Deleted successfully!!!')
    return redirect('add_employee')

@login_required
def employee_salary(request):
    employees = Employee.objects.all()
    salaries = Employee_Salary.objects.all()
    context = {'employees':employees, 'salaries':salaries,}
    if request.method == 'POST':
        employee = request.POST.get('employee')
        designation = request.POST['designation']
        salary_month = request.POST['salary_month']
        salary_year = request.POST['salary_year']
        salary_per_month = request.POST['salary_per_month']
        issue_date = request.POST['issue_date']
        Employee_Salary(
            employee_id=employee,
            designation=designation,
            salary_month=salary_month,
            salary_year=salary_year,
            salary_per_month=salary_per_month,
            issue_date=issue_date,
        ).save()
        messages.success(request, f'Employee Salary Added successfully! ')
        return redirect('employee_salary')
    return render(request, 'employee/employee_salary.html', context)


@login_required
def edit_salary(request, id):
    if request.method == 'POST':
        employee = request.POST.get('employee')
        designation = request.POST['designation']
        salary_month = request.POST['salary_month']
        salary_year = request.POST['salary_year']
        salary_per_month = request.POST['salary_per_month']
        issue_date = request.POST['issue_date']
        Employee_Salary.objects.filter(id=id).update(
            employee_id=employee,
            designation=designation,
            salary_month=salary_month,
            salary_year=salary_year,
            salary_per_month=salary_per_month,
            issue_date=issue_date,
        )
        messages.success(request, f'Employee Salary Updated successfully! ')
        return redirect('employee_salary')
    return render(request, 'employee/employee_salary.html')



@login_required
def delete_salary(request, id):
    Employee_Salary.objects.filter(id=id).delete()
    messages.success(request, f'Employee "{id}" Salary Deleted successfully!!!')
    return redirect('employee_salary')



@login_required
def view_salary(request, id):
    salaries = Employee_Salary.objects.filter(employee_id=id)
    salaro = Employee_Salary.objects.filter(employee_id=id)
    for empsalary in salaro:
        emp = empsalary
    context = {
        'salaries':salaries,
        'emp':emp,
    }
    return render(request, 'employee/single_salary.html', context)


####################################################################################


@login_required
def employee_ajax(request):
    queryset = Employee.objects.filter(id=request.POST.get('emp')).values()
    return JsonResponse({"data": list(queryset)})

@login_required
def floor_ajax(request):
    queryset = Unit.objects.filter(floor_id=request.POST.get('emp'), status='available').values()
    return JsonResponse({'data':list(queryset)}, safe=False)

@login_required
def floor_ajax1(request):
    queryset = Unit.objects.filter(floor_id=request.POST.get('emp')).values()
    return JsonResponse({'data':list(queryset)}, safe=False)

@login_required
def unit_ajax(request):
    queryset = Tenant.objects.filter(unit_id=request.POST.get('emp')).values()
    return JsonResponse({"data": list(queryset)})


@login_required
def status_ajax(request):
    status = request.POST.get('emp')
    id = request.POST.get('id')
    if request.method=='POST':
        update = Complain.objects.filter(id=id).update(status=status)
        return JsonResponse({"data": update})


@login_required
def assign_ajax(request):
    employee = request.POST.get('emp')
    id = request.POST.get('id')
    if request.method=='POST':
        update = Complain.objects.filter(id=id).update(employee_id=employee)
        return JsonResponse({"data": update})


####################################################################################

@login_required
def rent(request):
    floors = Floor.objects.all()
    context = {'floors':floors}
    if request.method == 'POST':
        floor = request.POST['floor']
        unit = request.POST['unit']
        hidden_tenant = request.POST['tenant_id']
        rent = request.POST['rent']
        rent_month = request.POST['rent_month']
        rent_year = request.POST['rent_year']
        water_bill = request.POST['water_bill']
        electric_bill = request.POST['electric_bill']
        gas_bill = request.POST['gas_bill']
        security_bill = request.POST['security_bill']
        utility_bill = request.POST['utility_bill']
        other_bill = request.POST['other_bill']
        total_rent = request.POST['total_rent']
        bill_paid_date = request.POST['bill_paid_date']
        status = request.POST['status']
        Rent(
            floor_id=floor,
            unit_id=unit,
            tenant_id = hidden_tenant,
            rent=rent,
            rent_month=rent_month,
            rent_year=rent_year,
            water_bill=water_bill,
            electric_bill=electric_bill,
            gas_bill=gas_bill,
            security_bill=security_bill,
            utility_bill=utility_bill,
            other_bill=other_bill,
            total_rent=total_rent,
            bill_paid_date=bill_paid_date,
            status=status,
        ).save()
        messages.success(request, f'Rent Paid successfully! ')
        return redirect('rent_list')
    return render(request, 'rent/rent.html', context)


@login_required
def update_rent(request, id):
    if request.method == 'POST':
        floor = request.POST['floor']
        unit = request.POST['unit']
        hidden_tenant = request.POST['tenant_id']
        rent = request.POST['rent']
        rent_month = request.POST['rent_month']
        rent_year = request.POST['rent_year']
        water_bill = request.POST['water_bill']
        electric_bill = request.POST['electric_bill']
        gas_bill = request.POST['gas_bill']
        security_bill = request.POST['security_bill']
        utility_bill = request.POST['utility_bill']
        other_bill = request.POST['other_bill']
        total_rent = request.POST['total_rent']
        bill_paid_date = request.POST['bill_paid_date']
        status = request.POST['status']
        Rent.objects.filter(id=id).update(
            floor_id=floor,
            unit_id=unit,
            tenant_id = hidden_tenant,
            rent=rent,
            rent_month=rent_month,
            rent_year=rent_year,
            water_bill=water_bill,
            electric_bill=electric_bill,
            gas_bill=gas_bill,
            security_bill=security_bill,
            utility_bill=utility_bill,
            other_bill=other_bill,
            total_rent=total_rent,
            bill_paid_date=bill_paid_date,
            status=status,
        )
        messages.success(request, f'Rent Info Updated successfully! ')
        return redirect('rent_list')
    return render(request, 'rent/rent.html')

@login_required
def delete_rent(request, id):
    Rent.objects.filter(id=id).delete()
    messages.success(request, f'Rent Deleted successfully!!!')
    return redirect('rent_list')


@login_required
def rent_list(request):
    floors = Floor.objects.all()
    rentList = Rent.objects.all()
    context = {
        'rentList':rentList,
        'floors':floors,
    }
    return render(request, 'rent/rent_list.html', context)

@login_required
def print_invoice(request, id):
    Invoice = Rent.objects.filter(id=id).last()
    context = {
        'invoice':Invoice
    }
    return render(request, 'rent/print_invoice.html', context)


@login_required
def maintenance(request):
    maintenance = Maintenance.objects.all()
    context = {
        "maintenance":maintenance
    }
    if request.method == 'POST':
        main = Maintenance()
        main.date = request.POST['date']
        main.month = request.POST['month']
        main.year = request.POST['year']
        main.title = request.POST['title']
        main.amount = request.POST['amount']
        main.details = request.POST['details']
        main.save()
        messages.success(request, f'Maintenance Info Added successfully! ')
        return redirect('maintenance')
    
    return render(request, 'maintenance/maintenance.html', context)


@login_required
def update_maintenance(request, id):
    if request.method == 'POST':
        date = request.POST['date']
        month = request.POST['month']
        year = request.POST['year']
        title = request.POST['title']
        amount = request.POST['amount']
        details = request.POST['details']
        Maintenance.objects.filter(id=id).update(
            date = date,
            month=month,
            year=year,
            title=title,
            amount=amount,
            details=details
        )
        messages.success(request, f'Maintenance Info Updated successfully! ')
        return redirect('maintenance')
    return render(request, 'maintenance/maintenance.html')


@login_required
def delete_maintenance(request, id):
    Maintenance.objects.filter(id=id).delete()
    messages.success(request, f'Maintenance Info Deleted successfully!!!')
    return redirect('maintenance')


@login_required
def management(request):
    management = Management.objects.all()
    context = {'management':management}
    if request.method == 'POST':
        man = Management()
        man.name = request.POST['name']
        man.email = request.POST['email']
        man.password = request.POST['password']
        man.contact = request.POST['contact']
        man.address = request.POST['address']
        man.national_id = request.POST['national_id']
        man.designation= request.POST['designation']
        man.join_date = request.POST['join_date']
        man.end_date = request.POST['end_date']
        man.status = request.POST['status']
        if len(request.FILES) != 0:
            man.image = request.FILES['image']
        man.save()
        messages.success(request, f' New Member "{man.name}" Added successfully! ')
        return redirect('management')
    return render(request, 'management/management.html', context)

@login_required
def edit_management(request, id):
    man = Management.objects.get(id=id)
    if request.method == 'POST':
        if len(request.FILES)!=0:
            if len(man.image) > 0:
                os.remove(man.image.path)
            man.image = request.FILES['image']
        man.name = request.POST['name']
        man.email = request.POST['email']
        man.password = request.POST['password']
        man.contact = request.POST['contact']
        man.address = request.POST['address']
        man.national_id = request.POST['national_id']
        man.designation= request.POST['designation']
        man.join_date = request.POST['join_date']
        man.end_date = request.POST['end_date']
        man.status = request.POST['status']
        man.save()
        messages.success(request, f'Member "{man.name}" Updated successfully! ')
        return redirect('management')
    return render(request, 'management/management.html')


@login_required
def delete_management(request, id):
    Management.objects.filter(id=id).delete()
    messages.success(request, f'Member "{id}" Deleted successfully!!!')
    return redirect('management')



@login_required
def bill(request):
    bills = Bill.objects.all()
    context = {
        'bills':bills
    }
    if request.method == 'POST':
        bill = Bill()
        bill.bill_type = request.POST['bill_type']
        bill.deposit_date = request.POST['deposit_date']
        bill.bill_month = request.POST['bill_month']
        bill.bill_year = request.POST['bill_year']
        bill.total_amount = request.POST['total_amount']
        bill.deposit_method = request.POST['deposit_method']
        bill.details = request.POST['details']
        bill.save()
        messages.success(request, f'Bill Deposit Added Successfully')
        return redirect('bill')
    return render(request, 'bill/bill.html', context)

@login_required
def edit_bill(request, id):
    bill = Bill.objects.get(id=id)
    if request.method == 'POST':
        bill.bill_type = request.POST['bill_type']
        bill.deposit_date = request.POST['deposit_date']
        bill.bill_month = request.POST['bill_month']
        bill.bill_year = request.POST['bill_year']
        bill.total_amount = request.POST['total_amount']
        bill.deposit_method = request.POST['deposit_method']
        bill.details = request.POST['details']
        bill.save()
        messages.success(request, f'Bill Deposit Info Updated Successfully')
        return redirect('bill')
    return render(request, 'bill/bill.html')


@login_required
def delete_bill(request, id):
    Bill.objects.filter(id=id).delete()
    messages.success(request, f'Bill Removed Successfully')
    return redirect('bill')


@login_required
def complain(request):
    complain = Complain.objects.all()
    employee = Employee.objects.all()
    context = {
        'complain':complain,
        'employee':employee,
    }
    if request.method == 'POST':
        comp = Complain()
        comp.title = request.POST['title']
        comp.description = request.POST['description']
        comp.date = request.POST['date']
        comp.tenant_id = request.POST['tenant_id']
        comp.save()

        getComplainId = Complain.objects.last()
        setComplain = getComplainId.id
        Notify(complain_by_id = request.POST['tenant_id'], complain_id_id=setComplain).save()
    


        messages.success(request, 'Complain added successfully')
        return redirect('complain')
    return render(request, 'complain/complain.html', context)

    
@login_required(login_url = 'login')
def update_solution(request, id):
    comp = Complain.objects.get(id=id)
    if request.method == 'POST':
        comp.solution = request.POST['solution']
        comp.save()
        messages.success(request, f'Solution Added Successfully')
        return redirect('complain')
    return render(request, 'complain/complain.html')




    
@login_required(login_url = 'login')
def viewComplain(request):
    return render(request, 'complain/viewComplain.html')


    
@login_required(login_url = 'login')
def delete_complain(request,id):
    Complain.objects.filter(id=id).delete()
    messages.success(request, f'Complain Removed Successfully')
    return redirect('complain')



class complainData(ServerSideDatatableView):
    queryset = Complain.objects.all()
    columns = ['id','title', 'date', 'status', 'employee_id']


    
@login_required(login_url = 'login')
def view_owner_complain(request, id):
    Notify.objects.filter(complain_id=id).update(seen=True)
    comp = Complain.objects.filter(id=id)
    for i in comp:
        comp = i
    context = {
        'comp':comp
    }
    return render(request, 'complain/viewOwnerComplain.html', context)

    
@login_required(login_url = 'login')
def view_tenant_complain(request, id):
    comp = Complain.objects.filter(id=id)
    for i in comp:
        comp = i
    context = {
        'comp':comp
    }
    return render(request, 'complain/viewTenantComplain.html', context)


    
@login_required(login_url = 'login')
def visitor(request):
    visitors = Visitor.objects.all()
    floors = Floor.objects.all()
    units = Unit.objects.all()
    context = {
        'visitors': visitors,
        'floors': floors,
        'units': units,
    }

    if request.method == 'POST':
        v = Visitor()
        v.entry_date = request.POST['entry_date']
        v.name = request.POST['name']
        v.number = request.POST['number']
        v.address = request.POST['address']
        v.floor_id = request.POST['floor']
        v.unit_id = request.POST['unit']
        v.in_time = request.POST['in_time']
        v.out_time = request.POST['out_time']
        v.save()
        messages.success(request, f'Visitor Added Successfully')
        return redirect('visitor')
    return render(request, 'visitor/visitor.html', context)

    
@login_required(login_url = 'login')
def edit_visitor(request, id):
    if request.method == 'POST':
        entry_date = request.POST['entry_date']
        name = request.POST['name']
        number = request.POST['number']
        address = request.POST['address']
        floor_id = request.POST['floor']
        unit_id = request.POST['unit']
        in_time = request.POST['in_time']
        out_time = request.POST['out_time']
        Visitor.objects.filter(id=id).update(
            entry_date = entry_date,
            name=name,
            number=number,
            address = address,
            floor_id = floor_id,
            unit_id=unit_id,
            in_time=in_time,
            out_time=out_time,
        )
        messages.success(request, f'Visitor Updated Successfully')
        return redirect('visitor')
    return render(request, 'visitor/visitor.html', context)


    
@login_required(login_url = 'login')
def delete_visitor(request,id):
    Visitor.objects.filter(id=id).delete()
    messages.success(request, f'Visitor Removed Successfully')
    return redirect('visitor')


    
@login_required(login_url = 'login')
def rental_report(request):
    floors = Floor.objects.all()
    context = {
        'floors': floors
    }
    return render(request, 'reports/rental_report.html', context)


    
@login_required(login_url = 'login')
def view_result(request): 
    totalAll = Rent.objects.filter(floor_id=request.POST.get('floor'), unit_id=request.POST.get('unit'), rent_year=request.POST.get('year'), rent_month=request.POST.get('month'), status=request.POST.get('status'))
    print(totalAll)
    context = {
        'totalAll': totalAll,
    }
    return render(request, 'reports/view_result.html', context)

    
@login_required(login_url = 'login')
def tenant_report(request):
    return render(request, 'reports/tenant_report.html')


    
@login_required(login_url = 'login')
def tenant_result(request):
    total = Tenant.objects.filter(status=request.POST.get('status')) 
    print(total)
    context = {
        'total':total
    }
    return render(request, 'reports/tenant_result.html',context)

    
@login_required(login_url = 'login')
def visitor_report(request):
    return render(request, 'reports/visitor_report.html')

    
@login_required(login_url = 'login')
def visitor_result(request):
    total = Visitor.objects.filter(entry_date=request.POST.get('year')) 
    print(total)
    context = {
        'total':total
    }
    return render(request, 'reports/visitor_result.html',context)

    
@login_required(login_url = 'login') 
def complain_report(request):
    return render(request, 'reports/complain_report.html')
    
@login_required(login_url = 'login')
def complain_result(request):
    total = Complain.objects.filter(status=request.POST.get('status')) 
    print(total)
    context = {
        'total':total
    }
    return render(request, 'reports/complain_result.html',context)

    
@login_required(login_url = 'login') 
def unit_report(request):
    return render(request, 'reports/unit_report.html')
    
@login_required(login_url = 'login')
def unit_result(request):
    total = Unit.objects.filter(status=request.POST.get('status')) 
    print(total)
    context = {
        'total':total
    }
    return render(request, 'reports/unit_result.html',context)

    
@login_required(login_url = 'login')   
def bill_report(request):
    return render(request, 'reports/bill_report.html')


@login_required(login_url = 'login')
def bill_result(request):
    total = Bill.objects.filter(bill_type=request.POST.get('bill_type')) 
    print(total)
    context = {
        'total':total
    }
    return render(request, 'reports/bill_result.html',context)

@login_required(login_url = 'login')
def salary_report(request):
    employee = Employee.objects.all()
    context = {
        'employee': employee,
    }
    return render(request, 'reports/salary_report.html', context)

@login_required(login_url = 'login')
def salary_result(request):
    total = Employee_Salary.objects.filter(employee_id=request.POST.get('employee'), salary_month=request.POST.get('month'), salary_year=request.POST.get('year')) 
    print(total)
    context = {
        'total':total
    }
    return render(request, 'reports/salary_result.html',context)