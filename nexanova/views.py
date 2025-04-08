from django.http import HttpResponse
from django.shortcuts import render
from trainer.models import Trainer, Subject
# Create your views here.

# def home(request):
#     data = Trainer.objects.all()
#     return render(request,'trainer.html',{'data':data})
    
def home(request):
    data1 = Trainer.objects.all().count()
    data2 = Subject.objects.all().count()
    return render(request, 'index.html', {'data1': data1, 'data2':data2})

