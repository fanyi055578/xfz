from django.shortcuts import render
from .models import Payinfo

# Create your views here.

def payinfo(request):
    info =Payinfo.objects.all()
    context = {
        'infos':info
    }
    return render(request,'payinfo/payinfo.html',context=context)


