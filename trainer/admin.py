from django.contrib import admin
from .models import Trainer, Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'description']

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['emp_id', 'name', 'email', 'phone', 'get_subjects']

    def get_subjects(self, obj):
        return ", ".join([subject.name for subject in obj.subjects.all()])
    get_subjects.short_description = 'Subjects'
