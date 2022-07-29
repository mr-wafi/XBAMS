from django.urls import path
from . import views


urlpatterns = [
    # path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('e-login/', views.e_login, name='e_login'),
    path('t-login/', views.t_login, name='t_login'),
    path('logout/', views.logout, name='logout'),
    path('t-logout/', views.t_logout, name='t_logout'),
    path('e-logout/', views.e_logout, name='e_logout'),
    path('t-register/', views.t_register, name='t_register'),
    path('e-register/', views.e_register, name='e_register'),
    path('Employee-dashboard/', views.e_dashboard, name='e_dashboard'),
    path('Tenant-dashboard/', views.t_dashboard, name='t_dashboard'),
    path('Tenant-dashboard/tenant-details', views.tenant_details, name='tenant_details'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('account/update-account/<int:id>', views.update_account, name='update_account'),
    # path('', views.dashboard, name='dashboard'),
]