from turtle import back
from django.shortcuts import render, redirect, get_object_or_404
from home.views import tenant
from .forms import *
from .models import Account, UserProfile
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from home.models import *
from django.contrib.auth.hashers import make_password
from django.db.models import Sum


# def register(request):
#     if request.user.is_authenticated:
#         return redirect('dashboard')
#     else:
#         if request.method == 'POST':
#             form = RegistrationForm(request.POST)
#             if form.is_valid():
#                 if Account.user_type == 'Employee':
#                     first_name = form.cleaned_data['first_name']
#                     last_name = form.cleaned_data['last_name']
#                     phone_number = form.cleaned_data['phone_number']
#                     model_choice = form.cleaned_data['model_choice']
#                     user_type = form.cleaned_data['user_type']
#                     email = form.cleaned_data['email']
#                     password = form.cleaned_data['password']
#                     username = email.split("@")[0]
#                     user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
#                     user.phone_number = phone_number
#                     user.user_type = user_type
#                     user.tenant_id = model_choice
#                     user.save()
#                     messages.success(request, f'User successfully registered')
#                     return redirect('login')
#                 elif Account.user_type == 'Tenant':
#                     first_name = form.cleaned_data['first_name']
#                     last_name = form.cleaned_data['last_name']
#                     phone_number = form.cleaned_data['phone_number']
#                     user_type = form.cleaned_data['user_type']
#                     model_choice = form.cleaned_data['model_choice']
#                     email = form.cleaned_data['email']
#                     password = form.cleaned_data['password']
#                     username = email.split("@")[0]
#                     user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
#                     user.phone_number = phone_number
#                     user.user_type = user_type
#                     user.tenant_id = model_choice
#                     user.save()
#                     messages.success(request, f'User successfully registered')
#                     return redirect('login')
#                 else:
#                     return redirect('register')
#         else:
#             form = RegistrationForm()
#         context = {
#             'form': form,
#         }
#     return render(request, 'accounts/register.html', context)

def t_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            user_type = request.POST['user_type'] #form.cleaned_data['user_type']
            select_tenant = form.cleaned_data['select_tenant']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.user_type = user_type
            user.tenant_id = select_tenant 
            user.save()
            print(user.save())
            messages.success(request, f'User successfully registered')
            return redirect('t_login')
        else:
            print('something went wrong')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/t_register.html', context)


def e_register(request):
    if request.method == 'POST':
        form = RegistrationForm1(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            user_type = request.POST['user_type'] #form.cleaned_data['user_type']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.user_type = user_type
            user.save()
            print(user.save())
            messages.success(request, f'Employee successfully registered')
            return redirect('e_login')
        else:
            messages.warning(request, f'there is some problem')
    else:
        form = RegistrationForm1()
    context = {
        'form': form,
    }
    return render(request, 'accounts/e_register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['user_type']

        user = auth.authenticate(email=email, password=password, user_type=user_type)
        if user is not None:
            if user.is_superadmin:
                auth.login(request, user)
                messages.success(request, f'You are now logged in.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('login')
        else:
            messages.error(request, 'there Is Some Error')
            return redirect('login')
    return render(request, 'accounts/login.html')

def e_login(request):
    if request.user.is_authenticated:
        return redirect('e_dashboard')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['user_type']

        user = auth.authenticate(email=email, password=password, user_type=user_type)
        if user is not None:
            if user.user_type == 'Employee':
                auth.login(request, user)
                messages.success(request, f'You are now logged in.')
                return redirect('e_dashboard')
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('e_login')
        else:
            messages.error(request, 'there Is Some Error')
            return redirect('login')
    return render(request, 'accounts/e_login.html')

def t_login(request):
    if request.user.is_authenticated:
        return redirect('t_dashboard')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['user_type']

        user = auth.authenticate(email=email, password=password, user_type=user_type)
        if user is not None:
            if user.user_type == 'Tenant':
                auth.login(request, user)
                messages.success(request, f'You are now logged in.')
                return redirect('t_dashboard')
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('t_login')
        else:
            messages.error(request, 'there Is Some Error')
            return redirect('login')
    return render(request, 'accounts/t_login.html')


@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

@login_required(login_url = 't_login')
def t_logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('t_login')

@login_required(login_url = 'e_login')
def e_logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('e_login')


@login_required(login_url='login')
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }
    return render(request, 'accounts/edit_profile.html', context)





###################################################################################
@login_required(login_url = 'login')
def dashboard(request):
    floors = Floor.objects.count()
    units = Unit.objects.count()
    tenants = Tenant.objects.count()
    employees = Employee.objects.count()
    complains = Complain.objects.count()
    totalRent = Rent.objects.aggregate(Sum('total_rent'))
    mainten = Maintenance.objects.aggregate(Sum('amount'))
    totalSalary = Employee_Salary.objects.aggregate(Sum('salary_per_month'))
    totalBill = Bill.objects.raw(''' SELECT SUM(total_amount) as id, bill_month FROM home_bill GROUP BY bill_month ORDER BY id ''')

    lastComplains = Complain.objects.all().order_by('-id')[:5][::-1]
    lastVisitors = Visitor.objects.all().order_by('-id')[:5][::-1]

    

    context = {
        'floors':floors,
        'units':units,
        'tenants':tenants,
        'employees':employees,
        'totalRent':totalRent,
        'mainten':mainten,
        'totalSalary':totalSalary,
        'complains':complains,
        'lastComplains':lastComplains,
        'lastVisitors':lastVisitors,
        'totalBill':totalBill,
    }
    
    return render(request, 'accounts/dashboard.html', context)
###################################################################################
@login_required(login_url = 'e_login')
def e_dashboard(request):
    return render(request, 'accounts/e_dashboard.html')
###################################################################################
@login_required(login_url = 't_login')
def t_dashboard(request):
    totalRent = Rent.objects.filter(tenant_id=request.user.tenant_id).aggregate(Sum('total_rent'))
    com = Complain.objects.filter(tenant_id=request.user.tenant_id).count()
    context = {
        'total':totalRent,
        'com':com
    }
    return render(request, 'accounts/t_dashboard.html', context)

@login_required(login_url = 't_login')
def tenant_details(request):
    totalRent = Account.objects.filter(tenant_id=request.user.tenant_id)
    context = {
        'total':totalRent
    }
    return render(request, 'accounts/tenant_details.html', context)

@login_required(login_url = 'login')
def update_account(request, id):
    if request.method == 'POST':
        username = request.POST.get('username'),
        email = request.POST.get('email'),
        phone_number = request.POST.get('phone_number'),
        Account.objects.filter(id=id).update(
            username = username,
            email=email,
            phone_number=phone_number,
        )
        messages.success(request, f'Account Updated Successfully')
        return redirect('/')
    return render(request, 'account/dashboard.html')


# def update_account(request, id):
#     a = Account.objects.get(id=id)
#     if request.method == 'POST':
#         a.username = request.POST.get('username'),
#         a.email = request.POST.get('email'),
#         a.phone_number = request.POST.get('phone_number'),
#         a.save()
#         messages.success(request, f'Account Updated Successfully')
#         return redirect('/')
#     return render(request, 'account/dashboard.html')
