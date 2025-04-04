from django.http import HttpResponse
from django.shortcuts import render
from trainer.models import Trainer
# Create your views here.

# def home(request):
#     data = Trainer.objects.all()
#     return render(request,'trainer.html',{'data':data})
    
def home(request):
    data = Trainer.objects.all().count()
    return render(request, 'index.html', {'data': data})