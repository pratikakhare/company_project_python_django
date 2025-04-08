from rest_framework import generics
from .models import Trainer, Subject
from .serializers import TrainerSerializer, SubjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404,redirect
from .forms import TrainerForm, SubjectForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages


# ─── Trainer Views ────────────────────────────────

class TrainerListCreateView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerDetailView(generics.RetrieveDestroyAPIView):
    lookup_field = 'emp_id'
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerBySubjectView(APIView):
    def get(self, request, subject):
        trainers = Trainer.objects.filter(subjects__name__iexact=subject)
        serializer = TrainerSerializer(trainers, many=True)
        return Response(serializer.data)

# ─── Subject Views ────────────────────────────────

class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailWithTrainers(APIView):
    def get(self, request, id):
        subject = get_object_or_404(Subject, pk=id)
        trainers = subject.trainers.all()
        trainer_serializer = TrainerSerializer(trainers, many=True)
        subject_serializer = SubjectSerializer(subject)
        return Response({
            "subject": subject_serializer.data,
            "trainers": trainer_serializer.data
        })

class SubjectDetailDeleteView(generics.RetrieveDestroyAPIView):
    lookup_field = 'pk'
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

from django.shortcuts import render, redirect
from .forms import TrainerForm

# ─── Frontend Views ─────────────────────────────

def home(request):
    total_trainers = Trainer.objects.count()
    total_subjects = Subject.objects.count()
    return render(request, 'trainer/home.html', {
        'total_trainers': total_trainers,
        'total_subjects': total_subjects,
    })

def trainer_list(request):
    query = request.GET.get('q', '')
    trainers = Trainer.objects.all()

    if query:
        trainers = trainers.filter(
            Q(name__icontains=query) | Q(email__icontains=query) | Q(phone__icontains=query)
        )

    paginator = Paginator(trainers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'trainer/trainer_list.html', {
        'page_obj': page_obj,
        'query': query,
    })


from django.contrib import messages
from .models import Trainer, Subject

def add_trainer(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject_id = request.POST.get('subject')

        # Check if emp_id already exists
        if Trainer.objects.filter(emp_id=emp_id).exists():
            messages.error(request, f"A trainer with Employee ID '{emp_id}' already exists.")
            subjects = Subject.objects.all()
            return render(request, 'trainer/add_trainer.html', {'subjects': subjects})

        trainer = Trainer.objects.create(emp_id=emp_id, name=name, email=email, phone=phone)
        
        if subject_id:
            trainer.subjects.add(subject_id)

        messages.success(request, "Trainer added successfully!")
        return redirect('trainer-list')

    subjects = Subject.objects.all()
    return render(request, 'trainer/add_trainer.html', {'subjects': subjects})



def subject_list(request):
    query = request.GET.get('q')
    subjects = Subject.objects.all()

    if query:
        subjects = subjects.filter(
            Q(name__icontains=query) | Q(code__icontains=query) | Q(description__icontains=query)
        )

    paginator = Paginator(subjects, 6)  # Show 5 subjects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'trainer/subject_list.html', {'page_obj': page_obj, 'query': query})



def add_subject(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        description = request.POST.get('description')

        # Check if subject code already exists
        if Subject.objects.filter(code=code).exists():
            messages.error(request, f"A subject with code '{code}' already exists.")
            return render(request, 'trainer/add_subject.html')

        Subject.objects.create(code=code, name=name, description=description)
        messages.success(request, "Subject added successfully!")
        return redirect('subject-list')

    return render(request, 'trainer/add_subject.html')



# View Trainer Details
def view_trainer(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    return render(request, 'trainer/view_trainer.html', {'trainer': trainer})

# Delete Trainer
def delete_trainer(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    trainer.delete()
    return redirect('trainer-list')


# View Subject Details
def view_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'trainer/view_subject.html', {'subject': subject})

# Delete Subject
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('subject-list')
