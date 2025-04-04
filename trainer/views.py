from django.shortcuts import render
from .models import Trainer

# Create your views here.

# def home(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     mobile = request.POST['mobile']
    #     subject = request.POST['subject']
    #     Trainer(name=name, mobile=mobile, subject=subject).save()
    # return render(request,'trainer.html')
        
# def add_trainer(request):
#      if request.method == 'POST':
#         name = request.POST['name']
#         mobile = request.POST['mobile']
#         subject = request.POST['subject']
#         er = Trainer(name=name, mobile=mobile, subject=subject)
#         er.save()
#         msg = "Trainer Added Successfully"
#         data = Trainer.objects.all()
#         return render(request,'trainer.html',{'data':data, 'msg':msg})
#      else:
#         return render(request,'trainer.html')
    

# Create your views here.

def add_trainer(request):
    data = Trainer.objects.all()  # Fetch all trainers *before* the if/else
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        subject = request.POST['subject']
        er = Trainer(name=name, mobile=mobile, subject=subject)
        er.save()
        msg = "Trainer Added Successfully"
        data = Trainer.objects.all() # Fetch all trainers again after adding new trainer
        return render(request,'trainer.html',{'data':data, 'msg':msg})
    else:
        return render(request,'trainer.html',{'data':data})
