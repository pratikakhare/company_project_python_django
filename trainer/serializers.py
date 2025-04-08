from rest_framework import serializers
from .models import Trainer, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'code', 'name', 'description']

class TrainerSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    subject_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Subject.objects.all(), write_only=True, source='subjects'
    )

    class Meta:
        model = Trainer
        fields = ['id', 'emp_id', 'name', 'email', 'phone', 'subjects', 'subject_ids']
