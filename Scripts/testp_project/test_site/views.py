from django.shortcuts import render
from django.http import HttpResponse

from .models import test_model
# Create your views here.

def index(request):
    return HttpResponse("Here will be index.")
    
def export_pdf(request):
    q=test_model.objects.filter(export_to_pdf__isnull=True)
    result=''
    for i in q:
        result+=i.firma
    context={'result':result}
    return render(request,'test_site/export_pdf.html',context)    
