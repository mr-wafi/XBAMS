from .models import Complain, Notify

from accounts.models import Account
def main(request):
    context = {
        'ownerNoti':Notify.objects.all()[:5][::-1]
    }
    return context

def tenantNotify(request):
    if request.user.is_authenticated:    
        tNotify = Notify.objects.filter(seen=1, tenant_id=request.user.tenant_id)[:5][::-1]
        return {
            'tNotify':tNotify
        }
    
    return {} 

    
def AccountInfo(request):
    if request.user.is_authenticated:    
        Info = Account.objects.filter(id=request.user.id)
        for i in Info:
            Info = i
        return {
            'Info': Info
        }
    
    return {} 